'''
Created on Nov 26, 2015

                       OpenMark Suite
Copyright (C) 2015  Matthew Muresan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

@author: Matthew Muresan
'''

import tkinter as tk
import tkinter.ttk as ttk
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm
import os.path
from module import jsonhandle as jsloader
from app.openwindow import OpenWindow

class WelcomeWindow(OpenWindow):
    def __init__(self, warn=False):
        self.appkill = False
        self.localconfig = {}
        self.localconfig["rootlocation"] = os.path.expanduser("~")
        self.localconfig["datafoldername"] = "OpenMarkData"
        self.localconfig["datafolderloca"] = os.path.join(self.localconfig["rootlocation"], self.localconfig["datafoldername"])
        self.localconfig["repoconfig"] = os.path.join(self.localconfig["datafolderloca"], "repoconfig.json")
        self.repoconfig = {} 
            
            
        if (os.path.isfile("localconfig/userconfigs.json")):
            #check if local data exists and load it.
            jsonData = jsloader.jsonParse("localconfig/userconfigs.json")
            if jsonData:
                self.localconfig = jsonData
            
        if ("repoconfig" in self.localconfig and os.path.isfile(self.localconfig["repoconfig"])):
            if not (os.path.isfile("localconfig/userconfigs.json")):
                self.WriteLocalConfig() #create the local config file. Repo exists.
            
            jsonData = jsloader.jsonParse(self.localconfig["repoconfig"])
            if jsonData:
                self.repoconfig = jsonData
                    
            if ("mode" not in self.repoconfig):
                if not self._initWindow(warn="mode"):
                    return
    
        elif (os.path.isfile("localconfig/userconfigs.json")):
            #there's a local config file telling us there's a repository, but there's none there.
            if not self._initWindow(warn="datafolderloca"):
                return
        else:
            if not self._initWindow():
                return      
    
    def _initWindow(self, warn=False):   
        super(WelcomeWindow, self).__init__("Welcome to OpenMark!", self.localconfig, self.repoconfig, menu=False)  
           
        self.window.resizable(0,0) #block resizing for the welcome window.
        windowcontent = ttk.Frame(self.window, padding=(12,12,12,12))
        titlelbl = ttk.Label(windowcontent, text="Welcome to OpenMark", font=(17))
        textlbl = ttk.Label(windowcontent, text="Please select the program's operation mode. "
                            +"To operate in network client mode, you must specify the network (cloud) "
                            +"address of the computer containing master copies of student "
                            +"records. If you do not have this information, ask your IT "
                            +"administrator to provide it for you. You must also specify "
                            +"the username you will use to access this data. "
                            +"If this computer is to act as the server housing the data, check "
                            +"select 'server mode'. There should "
                            +"only be one server on the network."
                            ,wraplength=550, justify=tk.LEFT)
        optionscontent = ttk.LabelFrame(windowcontent, text="Select Operating Mode", padding=(12,5,12,5))
        optionfilecont = ttk.LabelFrame(windowcontent, text="Local Data Folder", padding=(12,5,12,5))
        buttonscontent = ttk.Frame(windowcontent)
        
        textfil = ttk.Label(optionfilecont, text="Please select a location where local data "
                    +"should be stored. If in network client mode, this is where cloud "
                    +"data will be stored when you sync it to your computer. "
                    +"If you are using other OpenMark "
                    +"programs ensure this location matches the locations specified in them."
                    ,wraplength=550, justify=tk.LEFT)
        buttonbrwslofo = ttk.Button(optionfilecont, text="Browse...", command=self._askDirectory)
        self.brwsloc = ttk.Entry(optionfilecont)
        self.brwsloc.insert(0, self.localconfig["datafolderloca"])
        
        ok = ttk.Button(buttonscontent, text="Okay", command=self._windowOkay)
        cancel = ttk.Button(buttonscontent, text="Cancel", command=self._windowClose)
        self.varMode = tk.StringVar()
        
        networkYframe = ttk.Frame(optionscontent, padding=(12,2,12,5))
        networkNframe = ttk.Frame(optionscontent, padding=(12,2,12,5))
        networkSframe = ttk.Frame(optionscontent, padding=(12,2,12,5))
        radioNetworkY = ttk.Radiobutton(networkYframe, text="Network Client Mode", variable=self.varMode, value='network', command=self._toggleRadioNetwork)
        self.repolbl = ttk.Label(networkYframe, text="Cloud Address")
        self.userlbl = ttk.Label(networkYframe, text="Username")
        self.repository = ttk.Entry(networkYframe)
        self.repouser = ttk.Entry(networkYframe)
        self.reposync = ttk.Checkbutton(networkYframe, text="Push any changes I make to the cloud automatically on program exit")
        radioNetworkN = ttk.Radiobutton(networkNframe, text="Local Use Only Mode", variable=self.varMode, value='local', command=self._toggleRadioNetwork)
        radioNetworkS = ttk.Radiobutton(networkSframe, text="Server Mode", variable=self.varMode, value='server', command=self._toggleRadioNetwork)
        
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
        self.reposync.grid(row=2, column=1, columnspan=5, sticky=tk.W)
        self.reposync.invoke()
        networkYframe.columnconfigure(3, weight=1)
        networkYframe.columnconfigure(0, minsize=20)
        
        networkSframe.pack(fill=tk.X)
        radioNetworkS.grid(row=0, column=0, sticky=tk.W)
        
        networkNframe.pack(fill=tk.X)
        radioNetworkN.grid(row=0, column=0, sticky=tk.W)
        
        #BUTTONS
        cancel.pack(side=tk.RIGHT)
        ok.pack(side=tk.RIGHT)
        
        #allow main window to grow/shrink if sticky
        #window.columnconfigure(0, weight=1)
        #window.rowconfigure(0, weight=1)
        
        #deal with warnings passed to users.
        if (not warn):
            pass
        elif (warn=="datafolderloca" or warn=="mode"):
            tkm.showwarning("Warning!", "Local data repository is corrupt or missing! Please re-specify folder location or input new credentials to sync data from the network.", parent=self.window)
        else:
            tkm.showwarning("Warning!", "An unknown problem occurred while loading your configuration files!", parent=self.window)
        
        self.window.mainloop()
        if self.appkill:
            return False
        else:
            return True
    def WriteLocalConfig(self):        
        #save localconfig data.
        jsloader.jsonWrite(self.localconfigloc, self.localconfig)
            
    def _askDirectory(self):
        #Calls a dialog box that asks the user to navigate to a folder to save localconfig.
        dloglocalbrws = tkf.askdirectory(title="Choose a location for OpenMarkData", initialdir=self.localconfig["rootlocation"])
        if dloglocalbrws:
            self.localconfig["rootlocation"] = dloglocalbrws #save the path.
            self.localconfig["datafolderloca"] = os.path.join(self.localconfig["rootlocation"], self.localconfig["datafoldername"])
            self.brwsloc.delete(0, tk.END)
            self.brwsloc.insert(0, self.localconfig["datafolderloca"])
    
    def _toggleRadioNetwork(self):
        if (self.varMode.get() != "network"):
            self.repository.state(["disabled"])
            self.repouser.state(["disabled"])
            self.repolbl.state(["disabled"])
            self.userlbl.state(["disabled"])
            self.reposync.state(["disabled"])
            
        if (self.varMode.get() == "network"):
            self.repository.state(["!disabled"])
            self.repouser.state(["!disabled"])
            self.repolbl.state(["!disabled"])
            self.userlbl.state(["!disabled"])
            self.reposync.state(["!disabled"])
            
    def _windowOkay(self):
        #parse the form data and check it.
        self.repoconfig["mode"] = self.varMode.get()
        if (self.repoconfig["mode"] == "network"):
            self.repoconfig["username"] = self.repouser.get()
            self.repoconfig["location"] = self.repository.get()
            if (self.repoconfig["username"] == "" or self.repoconfig["location"] == ""):
                if not tkm.askyesno("Information Missing!", "You did not specify both a username and location for networked data, but you indicated you want the program to work in network client mode. Would you like to run the program in local mode instead?", parent=self.window):
                    return
                self.repoconfig["mode"] = "local" #change the mode to local then, if username/location not specified.
        
        #save localconfig data        
        self.WriteLocalConfig()
            
        #Create the folder for non-local data
        if (not os.path.isdir(self.localconfig["datafolderloca"])):
            os.makedirs(self.localconfig["datafolderloca"])
        self.localconfig["repoconfig"] = os.path.join(self.localconfig["datafolderloca"], "repoconfig.json")
        jsloader.jsonWrite(self.localconfig["repoconfig"], self.repoconfig)
                
        
        self._windowClose(False)
    
    def _windowClose(self, appkill=True):
        #App will die if left true.
        self.window.destroy()
        if appkill:
            self.appkill = True