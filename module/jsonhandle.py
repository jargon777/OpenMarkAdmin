'''
Created on Nov 26, 2015

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
        