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


from app.openwindow import OpenWindow
import tkinter as tk
import tkinter.ttk as ttk

class MainWin(OpenWindow):
    def __init__(self, localconfig, repoconfig):
        super(MainWin, self).__init__("OpenMarkAdmin", localconfig, repoconfig) 
        self.window.minsize(800, 600)
        self._initWindow()       
        
    def _initWindow(self):
        #get the window size and shrink it a little.
        self._positionWindow(self.window)
        

        toolbarcontent = ttk.Frame(self.window, padding=(1,1,1,1))
        self._buildToolbar(toolbarcontent)
        
        mainwindow = ttk.Frame(self.window, padding=(12,12,12,12))
        self._BuildMainWindow(mainwindow)
        
        toolbarcontent.pack(fill=tk.X)
        mainwindow.pack(fill=tk.BOTH, expand=1)

        
        self.window.mainloop()
    def _BuildMainWindow(self, mainwindow):
        leftNoteFrame = ttk.Frame(mainwindow)
        leftNotebook = ttk.Notebook(leftNoteFrame)
        leftNotebook1 = ttk.Frame(leftNotebook)
        leftNotebook1Scroll = tk.Scrollbar(leftNotebook1, orient=tk.VERTICAL)
        leftNotebook2 = ttk.Frame(leftNotebook)
        leftNotebook3 = ttk.Frame(leftNotebook)
        leftNotebook.add(leftNotebook1, text="Staff")
        leftNotebook.add(leftNotebook2, text="Students")
        leftNotebook.add(leftNotebook3, text="Other")
        
        searchEnt = tk.Entry(leftNoteFrame)
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/tan/16x16/search.gif")
        searchbutton = ttk.Button(leftNoteFrame, image=img, style='Toolbutton')
        searchbutton.img = img        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/red/16x16/add.gif")
        addbutton = ttk.Button(leftNoteFrame, image=img, style='Toolbutton')
        addbutton.img = img   
        testlist = ['Muresan, Matthew', 'Muresan, Tiffany']
        leftNotebook1Listbox = tk.Listbox(leftNotebook1, xscrollcommand=leftNotebook1Scroll.set)
        leftNotebook1Scroll['command'] = leftNotebook1Listbox.yview
        for element in testlist:
            leftNotebook1Listbox.insert(tk.END, element)
        leftNotebook1Listbox.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        leftNotebook1Scroll.grid(row=0, column=1, sticky=(tk.N, tk.S))
        leftNotebook1.columnconfigure(0, weight=1)
        leftNotebook1.rowconfigure(0, weight=1)
        
        rightInfoPane = ttk.Frame(mainwindow, padding=(12,12,12,12))
        basicInfo = ttk.Labelframe(rightInfoPane, text="Basic Information", padding=(5,5,5,5))
        spaceLab = tk.Label(basicInfo, text="empty")
        testlab = tk.Label(basicInfo, text="test", relief=tk.GROOVE, background="#FFD9D9", width=20, borderwidth=1)
        testent = tk.Entry(basicInfo, relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1)
        testlab2 = tk.Label(basicInfo, text="test", relief=tk.GROOVE, background="#FFD9D9", width=20, borderwidth=1)
        testent2 = tk.Entry(basicInfo, relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1)
        testlab3 = tk.Label(basicInfo, text="test", relief=tk.GROOVE, background="#FFD9D9", width=20, borderwidth=1)
        testent3 = tk.Entry(basicInfo, relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1)
        testlab4 = tk.Label(basicInfo, text="test", relief=tk.GROOVE, background="#FFD9D9", width=20, borderwidth=1)
        testent4 = tk.Entry(basicInfo, relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1)
        
        basicInfo.pack(fill=tk.X)
        testlab.grid(row=0, column=0)
        testent.grid(row=0, column=1, sticky=(tk.E, tk.W))
        spaceLab.grid(row=0, column=2)
        testlab2.grid(row=0, column=3)
        testent2.grid(row=0, column=4, sticky=(tk.E, tk.W))
        testlab3.grid(row=1, column=0)
        testent3.grid(row=1, column=1, sticky=(tk.E, tk.W))
        testlab4.grid(row=1, column=3)
        testent4.grid(row=1, column=4, sticky=(tk.E, tk.W))
        basicInfo.columnconfigure(1, weight=2)
        basicInfo.columnconfigure(4, weight=2)
        basicInfo.columnconfigure(2, minsize=40)
        spaceLab.destroy()
        
        leftNoteFrame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        leftNotebook.pack(fill=tk.BOTH, expand=1)
        addbutton.pack(side=tk.LEFT)
        searchbutton.pack(side=tk.LEFT)
        searchEnt.pack(side=tk.LEFT, fill=tk.X, expand=1)
        
        rightInfoPane.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        mainwindow.columnconfigure(0, weight=3)
        mainwindow.columnconfigure(1, weight=7)
        mainwindow.rowconfigure(0, weight=1)
        
    def _buildEntryTable(self, frame, content):
        pass
        
    def _buildToolbar(self, toolbarcontent):
        
        rowOne = ttk.Frame(toolbarcontent)
        mainPane = ttk.Frame(rowOne, padding=(1,1,1,1))
        modePane = ttk.Frame(rowOne, padding=(5,1,1,1))
        modeSep = ttk.Separator(rowOne, orient=tk.VERTICAL)
        #bottomSep = ttk.Separator(toolbarcontent, orient=tk.HORIZONTAL)
        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/tan/16x16/save.gif")
        testbutton = ttk.Button(mainPane, image=img, style='Toolbutton')
        testbutton.img = img
        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/blue/16x16/user.gif")
        peopleButton = ttk.Button(modePane, image=img, style='Toolbutton')
        peopleButton.img = img
        peopleButton.state(['pressed'])
        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/blue/16x16/addressbook.gif")
        listsButton = ttk.Button(modePane, image=img, style='Toolbutton')
        listsButton.img = img
        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/blue/16x16/tools.gif")
        serverButton = ttk.Button(modePane, image=img, style='Toolbutton')
        serverButton.img = img
        
        rowOne.pack(expand=1, fill=tk.X)
        
        #0 = mainpane (expand), 1 = space, 2=modepane 
        mainPane.grid(row=0, column=0, sticky=tk.W)
        modeSep.grid(row=0, column=1, sticky=(tk.E,tk.N,tk.S))
        modePane.grid(row=0, column=2, sticky=tk.E)
        rowOne.columnconfigure(0, weight=1)
        
        #bottomSep.pack(fill=tk.X, expand=1)
        testbutton.pack(side=tk.LEFT)
        
        peopleButton.pack(side=tk.RIGHT)
        listsButton.pack(side=tk.RIGHT)
        serverButton.pack(side=tk.RIGHT)
        
    def _windowPreClose(self):
        self._updateConfigs() #update the config files incase they were changed
        