'''
Created on Nov 26, 2015

                       OpenMark Suite
Copyright (C) 2015  Matthew Muresan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License, version 3, as published by
the Free Software Foundation.

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
import traceback
import sys
import logging
import tkinter as tk
import os

class ErrorSend:
    def __init__(self):
        pass
        
        
    def callError(self, *args):
        logging.basicConfig(level=logging.DEBUG, filename='localconfig/error.log')
        logging.exception("An Exception Occurred")
        
        self.window = tk.Tk()        
        self.window.title("OpenMark has Crashed!")
        self.window.resizable(0,0) #block resizing for the welcome window.
        windowcontent = ttk.Frame(self.window, padding=(12,12,12,12))
        titlelbl = ttk.Label(windowcontent, text="Unfortunately OpenMark has encountered an error and needs to close.", font=(17))
        textlbl = ttk.Label(windowcontent, text=traceback.format_exc())
        buttonscontent = ttk.Frame(windowcontent)
        ok = ttk.Button(buttonscontent, text="Okay", command=self._windowClose)
        
        #GRAND LAYOUT
        windowcontent.grid(column=0, row=0)        
        titlelbl.pack(pady=5)
        textlbl.pack()
        buttonscontent.pack(fill=tk.X)
        
        #BUTTONS
        ok.pack(side=tk.RIGHT)

        self.window.wm_attributes("-topmost", 1)
        self.window.focus_force()
        self.window.mainloop()
        
        
    def _windowClose(self):
        self.window.destroy()
        os._exit(1) #emergency exit.
                    