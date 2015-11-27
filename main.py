# OPENMARKSHEET                                                #
#  OpenMarkSheet is an educational program designed to collate #
#  student and teach information, including marks, etc.        #
#                                                              #
# PYTHON DEPENDANCIES: pycrypto                                #

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

#http://www.tkdocs.com/tutorial/index.html
#www.nmt.edu/tcc/help/pubs/tkinter/

import app.openwindowwelcome as oWel
import module.errorsend as errorcontrol
import app.openwindowadmin as oAdmin
import os.path
import json

def main():
    try:
        welcome = oWel.WelcomeWindow()
        if welcome.appkill: 
            return
        
        mainWin = oAdmin.MainWin(welcome.localconfig, welcome.repoconfig)
    
    except:
        errorHandle = errorcontrol.ErrorSend()
        errorHandle.callError()
    
if __name__ == "__main__":
    main()