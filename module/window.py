import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm
import os.path
import json

class WelcomeWindow:
    def __init__(self, warn=False, localdata=False):  
        self.appkill = False
        self.localdata = {}
        self.repoconfig = {}
        if (not localdata):
            self.localdata["rootlocation"] = os.path.expanduser("~")
            self.localdata["datafoldername"] = "OpenMarkData"
            self.localdata["datafolderloca"] = os.path.join(self.localdata["rootlocation"], self.localdata["datafoldername"])
        else:
            self.localdata = localdata
        self.window = tk.Tk()        
        self.window.title("Welcome to OpenMarkAdmin!")
        self.window.resizable(0,0) #block resizing for the welcome window.
        windowcontent = ttk.Frame(self.window, padding=(12,12,12,12))
        titlelbl = ttk.Label(windowcontent, text="Welcome to OpenMarkAdmin", font=(17))
        textlbl = ttk.Label(windowcontent, text="Please select the program's operation mode. "
                            +"To operate in networked mode, you must specify the network (cloud) "
                            +"address of the computer containing master copies of student "
                            +"records. If you do not have this information, ask your IT "
                            +"administrator to provide it for you. You must also specify "
                            +"the password required to access this data." 
                            ,wraplength=550, justify=tk.LEFT)
        optionscontent = ttk.LabelFrame(windowcontent, text="Select Operating Mode", padding=(12,5,12,5))
        optionfilecont = ttk.LabelFrame(windowcontent, text="Local Data Folder", padding=(12,5,12,5))
        buttonscontent = ttk.Frame(windowcontent)
        
        textfil = ttk.Label(optionfilecont, text="Please select a location where local data "
                    +"should be stored. If in networked mode, this is where cloud "
                    +"data will be stored when you sync it to your computer. "
                    +"If you are using other OpenMark "
                    +"programs ensure this location matches the locations specified in them."
                    ,wraplength=550, justify=tk.LEFT)
        buttonbrwslofo = ttk.Button(optionfilecont, text="Browse...", command=self._askDirectory)
        self.brwsloc = ttk.Entry(optionfilecont)
        self.brwsloc.insert(0, self.localdata["datafolderloca"])
        
        ok = ttk.Button(buttonscontent, text="Okay", command=self._windowOkay)
        cancel = ttk.Button(buttonscontent, text="Cancel", command=self._windowClose)
        self.varMode = tk.StringVar()
        
        networkYframe = ttk.Frame(optionscontent, padding=(12,2,12,5))
        networkNframe = ttk.Frame(optionscontent, padding=(12,2,12,5))
        radioNetworkY = ttk.Radiobutton(networkYframe, text="Networked Mode", variable=self.varMode, value='network', command=self._toggleRadioNetwork)
        self.repolbl = ttk.Label(networkYframe, text="Cloud Address")
        self.userlbl = ttk.Label(networkYframe, text="Username")
        self.repository = ttk.Entry(networkYframe)
        self.repouser = ttk.Entry(networkYframe)
        radioNetworkN = ttk.Radiobutton(networkNframe, text="Local Use Only Mode", variable=self.varMode, value='local', command=self._toggleRadioNetwork)
        
        #GRAND LAYOUT
        windowcontent.grid(column=0, row=0)        
        titlelbl.pack(pady=5)
        textlbl.pack()
        optionscontent.pack(fill=tk.X, pady=15, padx=15)
        optionfilecont.pack(fill=tk.X, pady=15, padx=15, ipady=3)
        buttonscontent.pack(fill=tk.X)
        
        #LOCAL DATA LAYOUT
        textfil.grid(row=0, column=0, columnspan=2, pady=2)
        self.brwsloc.grid(row=1, column=0, padx=15, pady=2, sticky=(tk.W, tk.E))
        buttonbrwslofo.grid(row=1, column=1, padx=15, pady=2, sticky=tk.W)
        optionfilecont.columnconfigure(0, weight=1)
        
        #OPTIONS LAYOUT
        networkYframe.pack(fill=tk.X)
        radioNetworkY.grid(row=0, column=0, columnspan=6, sticky=tk.W)
        radioNetworkY.invoke()
        self.repolbl.grid(row=1, column=1, sticky=tk.E)
        self.repository.grid(row=1, column=2, padx=2, sticky=(tk.E, tk.W))
        self.userlbl.grid(row=1, column=4, sticky=tk.E)
        self.repouser.grid(row=1, column=5, padx=2, sticky=(tk.E, tk.W))
        networkYframe.columnconfigure(3, weight=1)
        networkYframe.columnconfigure(0, minsize=20)
        
        networkNframe.pack(fill=tk.X)
        radioNetworkN.grid(row=0, column=0, sticky=tk.W)
        
        #BUTTONS
        ok.pack(side=tk.RIGHT)
        cancel.pack(side=tk.RIGHT)
        
        #allow main window to grow/shrink if sticky
        #window.columnconfigure(0, weight=1)
        #window.rowconfigure(0, weight=1)
        
        #deal with warnings passed to users.
        if (not warn):
            pass
        elif (warn=="datafolderloca"):
            tkm.showwarning("Warning!", "Local data repository is corrupt or missing! Please re-specify folder location or input new credentials to sync data from the network.", parent=self.window)
        
        self.window.mainloop()

        
    def _askDirectory(self):
        #Calls a dialog box that asks the user to navigate to a folder to save localdata.
        dloglocalbrws = tkf.askdirectory(title="Choose a location for OpenMarkData", initialdir=self.localdata["rootlocation"])
        if dloglocalbrws:
            self.localdata["rootlocation"] = dloglocalbrws #save the path.
            self.localdata["datafolderloca"] = os.path.join(self.localdata["rootlocation"], self.localdata["datafoldername"])
            self.brwsloc.delete(0, tk.END)
            self.brwsloc.insert(0, self.localdata["datafolderloca"])
    
    def _toggleRadioNetwork(self):
        if (self.varMode.get() != "network"):
            self.repository.state(["disabled"])
            self.repouser.state(["disabled"])
            self.repolbl.state(["disabled"])
            self.userlbl.state(["disabled"])
            
        if (self.varMode.get() == "network"):
            self.repository.state(["!disabled"])
            self.repouser.state(["!disabled"])
            self.repolbl.state(["!disabled"])
            self.userlbl.state(["!disabled"])
    def _windowOkay(self):
        #first save the location of the folder.
        with open ("localconfig/userconfigs.json", 'w') as Fconfig:
            json.dump(self.localdata, Fconfig)
            
        #next create the folder.
        if (not os.path.isdir(self.localdata["datafolderloca"])):
            os.makedirs(self.localdata["datafolderloca"])
            dataconfigloc = os.path.join(self.localdata["datafolderloca"], "repoconfig.json")
            with open (dataconfigloc, 'w') as Frepoconfig:
                json.dump(self.repoconfig, Frepoconfig)
                
        
        self._windowClose(False)
    
    def _windowClose(self, appkill=True):
        #App will die if left true.
        self.window.destroy()
        if appkill:
            self.appkill = True