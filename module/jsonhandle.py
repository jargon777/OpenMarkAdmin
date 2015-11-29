'''
Created on Nov 26, 2015
                       OpenMark Suite
Copyright (C) 2015  Matthew Muresan

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

@author: Matthew Muresan
'''

import json
import os
import logging

def jsonParse(jsonFile, deleteOnError=True):
    try:
        with open (jsonFile, 'r') as readFile:
            jsonData = json.load(readFile)
            return jsonData
    except:
        if (deleteOnError):
            os.remove(jsonFile) #the file is corrupt. Remove it so it can be recreated
        return False
def jsonWrite(jsonFile, rawData):
    with open (jsonFile, 'w') as writeFile:
        try:
            json.dump(rawData, writeFile)
            return True
        except:
            logging.basicConfig(level=logging.DEBUG, filename='localconfig/error.log')
            logging.exception("A Handled Exception Occurred")
            return False
        