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
import tkinter.filedialog as tkf
import tkinter.messagebox as tkm
import module.errorsend as errorcontrol
import module.jsonhandle as jsloader
from app.opendialogabout import AboutProgramDialog

class OpenWindow:
    '''
    OpenWindow Class. Base class for all tkinter windows in OpenMarksheets
    '''
    def __init__(self, applicationName, localconfig, repoconfig, menu=True):
        self.window = False
        tk.Tk.report_callback_exception = self._callError
        self.localconfigloc = "localconfig/userconfigs.json"
        self.localconfig = localconfig
        self.repoconfig = repoconfig
        self.applicationName = applicationName
        self.menu = menu
        self._skelInit()
        
        #redirect X button to window close.
        self.window.protocol("WM_DELETE_WINDOW", self._windowClose)
    
    #inheritable class that sets up the basic tkinter window
    def _skelInit(self):
        self.window = tk.Tk()        
        self.window.title(self.applicationName)
        self.window.option_add('*tearOff', tk.FALSE) #disable menutearing
        
        #setup the menubar if asked.
        if self.menu:
            self.mainmenubar = tk.Menu(self.window)
            self.window.config(menu=self.mainmenubar)
            
            self.fileMenu = tk.Menu(self.mainmenubar)
            self.fileMenu.add_command(label="Exit", command=self._windowClose)
            
            self.helpMenu = tk.Menu(self.mainmenubar)
            self.helpMenu.add_command(label="About", command=self._showAbout)
            
            self.mainmenubar.add_cascade(label="File", menu=self.fileMenu)
            self.mainmenubar.add_cascade(label="Help", menu=self.helpMenu)
    
    def _initWindow(self):
        #get the window size and shrink it a little.
        self._positionWindow(self.window)

        self.window.mainloop()
    
    def _showAbout(self):
        AboutProgramDialog(self.window)
    
    def _positionWindow(self, window, size=False):
        window.update_idletasks()
        w = window.winfo_screenwidth()
        h = window.winfo_screenheight()

        if not size:
            scx = 0.1*w if 0.1*w < 150 else 150
            scx = 75 if scx < 75 else scx
            scy = 0.1*h if 0.1*h < 250 else 250
            scy = 150 if scy < 150 else scy
            size = (w-scx, h-scy)
        
        x = 0#w/2 - size[0]/2
        y = 0#h/2 - size[1]/2
        window.geometry("%dx%d+%d+%d" % (size + (x, y)))
    
    def _updateConfigs(self):
        '''
        Updates the local and repo config files.
        '''
        #raise
        jsloader.jsonWrite(self.localconfigloc, self.localconfig)
        jsloader.jsonWrite(self.localconfig["repoconfig"], self.repoconfig)
    
    def _windowClose(self):
        self._windowPreClose()
        self.window.destroy()
        
    def _windowPreClose(self):
        '''
        overidable inherited method to run tasks in addition to window_close.
        '''
        pass
        
    def _callError(self, *args):
        errorHandle = errorcontrol.ErrorSend()
        errorHandle.callError(*args)
        