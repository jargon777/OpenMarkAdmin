'''
Created on Nov 28, 2015

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
from app.opendialog import OpenDialog
import webbrowser

class AboutProgramDialog(OpenDialog):
    def __init__(self, parent):
        self.parent = parent
        self._initWindow()    
    
    def _initWindow(self):   
        super(AboutProgramDialog, self).__init__("About OpenMarkSheets", self.parent)  

        windowcontent = ttk.Frame(self.window, padding=(12,12,12,12))
        titlelbl = ttk.Label(windowcontent, text="OpenMarkBook", font=(17))
        textlbl = ttk.Label(windowcontent, text="Copyright 2015 Matthew Muresan\n\n"
                            +"OpenMarkBook is free software, you can redistribute it and/or modify "
                            +"it under the terms of the GNU General Public License as published by "
                            +"the Free Software Foundation, either version 3 of the License, or " 
                            +"(at your option) any later version. \n\n"
                            +"This program uses Git, a software development version control system. "
                            +"Git is distributed under the terms of the GNU General Public License "
                            +"(version 2) as published by the Free Software Foundation. "
                            +"You should have received a copy of the GNU General Public License "
                            "along with this program."
                            
                            ,wraplength=550, justify=tk.LEFT)
        gplLink = ttk.Label(windowcontent, text=r"http://www.gnu.org/licenses", foreground="#577782")
        gplLink.bind("<Button-1>", self._webLink)
        textfil = ttk.Label(windowcontent, text="\nThis program uses the Bitcons icon set, designed by P.J. Onori and released under the "
                            +"Creative Commons Attribution-Share Alike 3.0 license."
                            ,wraplength=550, justify=tk.LEFT)
        ccLink = ttk.Label(windowcontent, text=r"https://creativecommons.org/licenses/by-sa/3.0/us/", foreground="#577782")
        ccLink.bind("<Button-1>", self._webLink)
        
        buttonscontent = ttk.Frame(windowcontent)
        
        ok = ttk.Button(buttonscontent, text="Okay", command=self._windowClose)
        
        
        #GRAND LAYOUT
        windowcontent.grid(column=0, row=0)        
        titlelbl.pack(pady=5)
        textlbl.pack(fill=tk.X)
        gplLink.pack(pady=2)
        textfil.pack(pady=2, fill=tk.X)
        ccLink.pack()
        buttonscontent.pack(fill=tk.X)
        
        
        #BUTTONS
        ok.pack(side=tk.RIGHT)
        
    def _webLink(self, event):
        webbrowser.open_new(event.widget.cget("text"))