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
        mainNotebook = ttk.Notebook(mainwindow)
        notebook1 = ttk.Frame(mainNotebook)
        notebook2 = ttk.Frame(mainNotebook)
        mainNotebook.add(notebook1, text="1")
        mainNotebook.add(notebook2, text="2")
        
        textfil1 = ttk.Label(notebook1, text="Please select a location where local data "
            +"should be stored. If in network client mode, this is where cloud "
            +"data will be stored when you sync it to your computer. "
            +"If you are using other OpenMark "
            +"programs ensure this location matches the locations specified in them."
            ,wraplength=550, justify=tk.LEFT)
        textfil2 = ttk.Label(notebook2, text="Please select a location where local data "
                    +"should be stored. If in network client mode, this is where cloud "
                    +"data will be stored when you sync it to your computer. "
                    +"If you are using other OpenMark "
                    +"programs ensure this location matches the locations specified in them."
                    ,wraplength=550, justify=tk.LEFT)
        
        textfil2.pack()
        textfil1.pack()
        
        mainNotebook.pack(fill=tk.BOTH)
        
    def _buildToolbar(self, toolbarcontent):
        rowOne = ttk.Frame(toolbarcontent)
        mainPane = ttk.Frame(rowOne, padding=(1,1,1,1))
        modePane = ttk.Frame(rowOne, padding=(5,1,1,1))
        modeSep = ttk.Separator(rowOne, orient=tk.VERTICAL)
        #bottomSep = ttk.Separator(toolbarcontent, orient=tk.HORIZONTAL)
        testbutton = tk.Button(mainPane, text="T", relief=tk.FLAT)
        
        peopleButton = tk.Button(modePane, text="People", relief=tk.FLAT, borderwidth=2)
        listsButton = tk.Button(modePane, text="Lists", relief=tk.SUNKEN, borderwidth=2)
        serverButton = tk.Button(modePane, text="Server", relief=tk.FLAT, borderwidth=2)
        
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
        