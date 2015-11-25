# OPENMARKSHEET                                                #
#  OpenMarkSheet is an educational program designed to collate #
#  student and teach information, including marks, etc.        #
#                                                              #
# PYTHON DEPENDANCIES: pycrypto                                #

#http://www.tkdocs.com/tutorial/index.html
#www.nmt.edu/tcc/help/pubs/tkinter/

import module.window as oWin
import os.path
import json
import tkinter as tk
import tkinter.messagebox as tkm

        
def main():
    if (os.path.isfile("localconfig/userconfigs.json")):
        #check if local data exists
        with open ("localconfig/userconfigs.json", 'r') as config:
            localdata = json.load(config)
    else:
        welcomeWindow = oWin.WelcomeWindow()
        if welcomeWindow.appkill: 
            return
        localdata = welcomeWindow.localdata

    if ("datafolderloca" in localdata and os.path.isdir(localdata["datafolderloca"])):
        #In this scenario we can go ahead and load configuration data.
        #welcomeWindow = oWin.WelcomeWindow()
        pass
    else:
        welcomeWindow = oWin.WelcomeWindow(warn="datafolderloca")
        if welcomeWindow.appkill: 
            return
    
    
if __name__ == "__main__":
    main()