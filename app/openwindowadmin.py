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

class MainWin(OpenWindow):
    def __init__(self, localconfig, repoconfig):
        super(MainWin, self).__init__("OpenMarkAdmin", localconfig, repoconfig) 
        self._initWindow()       
        
    def _windowClose(self):
        self._updateConfigs() #update the config files incase they were changed
        self.window.destroy()
        