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


from app.openwindow import OpenWindow
import tkinter as tk
import tkinter.ttk as ttk
import json
import re
import string

class MainWin(OpenWindow):
    def __init__(self, localconfig, repoconfig):
        super(MainWin, self).__init__("OpenMarkAdmin", localconfig, repoconfig) 
        self.window.tk_strictMotif(1)
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
        tableData = {}
        self.JSONdata = tableData
        # DEFAULT TEMPLATE.
        tableData['basic'] = {}
        tableData['basic']['text'] = [0, 1, 2]
        tableData['basic']['text'][0] = {}
        tableData['basic']['text'][0]['name'] = "First Name"
        tableData['basic']['text'][0]['value'] = "Matthew"
        tableData['basic']['text'][1] = {}
        tableData['basic']['text'][1]['name'] = "Other Names"        
        tableData['basic']['text'][1]['value'] = "Iulian"
        tableData['basic']['text'][2] = {}
        tableData['basic']['text'][2]['name'] = "Last Name"
        tableData['basic']['text'][2]['value'] = "Muresan"

        tableData['basic']['list'] = [0]
        tableData['basic']['list'][0] = {}
        tableData['basic']['list'][0]['name'] = "Role"
        tableData['basic']['list'][0]['value'] = "IT"
        tableData['basic']['list'][0]['values'] = ["Teacher", "Administrative", "Support", "IT", "Other"]
        
        tableData['basic']['phone'] = [0, 1]
        tableData['basic']['phone'][0] = {}
        tableData['basic']['phone'][0]['name'] = "Primary Phone"
        tableData['basic']['phone'][0]['value'] = "(123) 456-789"
        tableData['basic']['phone'][1] = {}
        tableData['basic']['phone'][1]['name'] = "Secondary Phone"
        tableData['basic']['phone'][1]['value'] = "(123) 456-789"
        
        tableData['address'] = {}
        tableData['address']['text'] = [0, 1, 2, 3, 4]
        tableData['address']['text'][0] = {}
        tableData['address']['text'][0]['name'] = "Street Address"
        tableData['address']['text'][0]['value'] = "53 Beck Drive"
        tableData['address']['text'][1] = {}
        tableData['address']['text'][1]['name'] = "City"        
        tableData['address']['text'][1]['value'] = "Markham"
        tableData['address']['text'][2] = {}
        tableData['address']['text'][2]['name'] = "Province"
        tableData['address']['text'][2]['value'] = "Ontario"
        tableData['address']['text'][3] = {}
        tableData['address']['text'][3]['name'] = "Postal Code"
        tableData['address']['text'][3]['value'] = "N1G 5H6"
        tableData['address']['text'][4] = {}
        tableData['address']['text'][4]['name'] = "Country"
        tableData['address']['text'][4]['value'] = "Canada"
        
        tableData['personal'] = {}
        tableData['personal']['text'] = [0, 1]
        tableData['personal']['text'][0] = {}
        tableData['personal']['text'][0]['name'] = "Emergency Contact 1"
        tableData['personal']['text'][0]['value'] = "Tiffany Muresan"
        tableData['personal']['text'][1] = {}
        tableData['personal']['text'][1]['name'] = "Emergency Contact 2"
        tableData['personal']['text'][1]['value'] = "Tiffany Muresan"
        
        tableData['personal']['phone'] = [0, 1]
        tableData['personal']['phone'][0] = {}
        tableData['personal']['phone'][0]['name'] = "Emergency Phone 1"
        tableData['personal']['phone'][0]['value'] = "(123) 456-789"
        tableData['personal']['phone'][1] = {}
        tableData['personal']['phone'][1]['name'] = "Emergency Phone 2"
        tableData['personal']['phone'][1]['value'] = "(123) 456-789"
        
        tableData['personal']['csv'] = [0, 1]
        tableData['personal']['csv'][0] = {}
        tableData['personal']['csv'][0]['name'] = "Allergies"
        tableData['personal']['csv'][0]['value'] = "Peanuts, Penicillin, MSG"
        tableData['personal']['csv'][1] = {}
        tableData['personal']['csv'][1]['name'] = "Medicines"
        tableData['personal']['csv'][1]['value'] = "Comma Separated List, Like This"
        
        tableData['personal']['note'] = [0]
        tableData['personal']['note'][0] = {}
        tableData['personal']['note'][0]['name'] = "Other Medical Notes"
        tableData['personal']['note'][0]['value'] = "Just an ordinary collection of text to describe something more complex"
        
        
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
        personalInfo = ttk.Labelframe(rightInfoPane, text="Personal and Medical Information", padding=(5,5,5,5))
        addressInfo = ttk.Labelframe(rightInfoPane, text="Address", padding=(5,5,5,5))

        
        self._buildEntryTable(basicInfo, tableData['basic'])
        self._buildEntryTable(personalInfo, tableData['personal'])
        self._buildEntryTable(addressInfo, tableData['address'])
        basicInfo.pack(fill=tk.X, pady=5)
        addressInfo.pack(fill=tk.X, pady=5)
        personalInfo.pack(fill=tk.X, pady=5)
        
        leftNoteFrame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        leftNotebook.pack(fill=tk.BOTH, expand=1)
        addbutton.pack(side=tk.LEFT)
        searchbutton.pack(side=tk.LEFT)
        searchEnt.pack(side=tk.LEFT, fill=tk.X, expand=1)
        
        rightInfoPane.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        mainwindow.columnconfigure(0, weight=3)
        mainwindow.columnconfigure(1, weight=7)
        mainwindow.rowconfigure(0, weight=1)
        
    def _buildEntryTable(self, frame, tableData):
        '''
        frame->TKframe housing countent
        tableData-> Dictionary with["type"]. Sub labels include: "labels", "values", and "name"
            ->datatypes include "text", "radio", "check" with typelabel forming the labels for the radios.
        '''
        gridIndex = {}
        gridIndex['r'] = 0
        gridIndex['c'] = 0
        if 'text' in tableData:
            for item in tableData['text']:
                self._buildEntryTableSubEntry(item, 'text', frame, tableData, gridIndex)
            
        if 'phone' in tableData:
            for item in tableData['phone']:
                self._buildEntryTableSubEntry(item, 'phone', frame, tableData, gridIndex)
                
        if 'list'  in tableData:
            for item in tableData['list']:
                self._buildEntryTableSubEntry(item, 'list', frame, tableData, gridIndex)
        if 'csv' in tableData:
            for item in tableData['csv']:
                self._buildEntryTableSubEntry(item, 'csv', frame, tableData, gridIndex)
        if 'note' in tableData:
            for item in tableData['note']:
                self._buildEntryTableSubEntry(item, 'note', frame, tableData, gridIndex)
        if 'check' in tableData:
            for item in tableData['check']:
                self._buildEntryTableSubEntry(item, 'check', frame, tableData, gridIndex)
            
        #to create a space in between the two columns
        spaceLab = tk.Label(frame, text="empty")
        spaceLab.grid(row=0, column=2)
        spaceLab.destroy()
                
        frame.columnconfigure(1, weight=2)
        frame.columnconfigure(4, weight=2)
        frame.columnconfigure(2, minsize=40)
            
    def _buildEntryTableSubEntry(self, item, itemType, frame, tableData, gridIndex):
        lab = tk.Label(frame, text=item['name'], relief=tk.GROOVE, background="#FFD9D9", width=20, borderwidth=1)
        enttext = item['value']
        item['value'] = tk.StringVar()
        
        if itemType == 'phone':
            ent = tk.Entry(frame, textvariable=item['value'], relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1
                           , validate='focusout', validatecommand=lambda:self._validatePhoneNumber(ent))
            ent.insert(0, enttext)
        elif itemType == 'list':
            item['value'].set(enttext)
            ent = tk.OptionMenu(frame, item['value'], *item['values'])
            ent.configure(relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1, highlightthickness=0, pady=0, padx=0)
        elif itemType == 'text':
            ent = tk.Entry(frame, textvariable=item['value'], relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1)
            ent.insert(0, enttext)
        elif itemType == 'csv' or itemType == 'note':
            ent = tk.Text(frame, relief=tk.GROOVE, background="#FFEBEB", width=20, borderwidth=1
                            , height=3)
            ent.insert(tk.END, enttext)
            item['value'] = ent
        elif itemType == 'check':
            #not happy with check appearance, may remove
            checkoptions = tk.Frame(frame, relief=tk.GROOVE, background="#FFEBEB", borderwidth=1, padx=0, pady=0)
            check1 = tk.Checkbutton(checkoptions, text="TEST", pady=0, borderwidth=0, highlightthickness=0, background="#FFEBEB")
            check1.grid(row=0, column=0, sticky=tk.W)
            check2 = tk.Checkbutton(checkoptions, text="TEST", pady=0, borderwidth=0, highlightthickness=0, background="#FFEBEB")
            check2.grid(row=0, column=1, sticky=tk.W)
            check3 = tk.Checkbutton(checkoptions, text="TEST", pady=0, borderwidth=0, highlightthickness=0, background="#FFEBEB")
            check3.grid(row=0, column=2, sticky=tk.W)
            check4 = tk.Checkbutton(checkoptions, text="TEST", pady=0, borderwidth=0, highlightthickness=0, background="#FFEBEB")
            check4.grid(row=0, column=3, sticky=tk.W)
            check4 = tk.Checkbutton(checkoptions, text="TEST", pady=0, borderwidth=0, highlightthickness=0, background="#FFEBEB")
            check4.grid(row=0, column=4, sticky=tk.W)
            checkoptions.columnconfigure(0, weight=1)
            checkoptions.columnconfigure(1, weight=1)
            checkoptions.columnconfigure(2, weight=1)
            checkoptions.columnconfigure(3, weight=1)
            checkoptions.columnconfigure(4, weight=1)
        
        if itemType == 'check':
            if gridIndex['c'] >= 0:
                gridIndex['c'] = 0
                gridIndex['r'] += 1
            
            lab.grid(row=gridIndex['r'], column=gridIndex['c'])
            checkoptions.grid(row=gridIndex['r'], column=gridIndex['c']+1, columnspan=4, sticky=(tk.N, tk.S, tk.E, tk.W))
            gridIndex['r'] += 1
        
        else:
            lab.grid(row=gridIndex['r'], column=gridIndex['c'], sticky=(tk.N))
            gridIndex['c'] += 1
            ent.grid(row=gridIndex['r'], column=gridIndex['c'], sticky=(tk.E, tk.W))
            gridIndex['c'] += 2
            
            if gridIndex['c'] >= 4:
                gridIndex['c'] = 0
                gridIndex['r'] += 1
    
    def _validateCSV(self, entry):
        value = entry.get()
        value = string.capwords(value)
        entry.delete(0, tk.END)
        entry.insert(0, value)
        
        return True
            
    def _buildToolbar(self, toolbarcontent):
        
        rowOne = ttk.Frame(toolbarcontent)
        mainPane = ttk.Frame(rowOne, padding=(1,1,1,1))
        modePane = ttk.Frame(rowOne, padding=(5,1,1,1))
        modeSep = ttk.Separator(rowOne, orient=tk.VERTICAL)
        #bottomSep = ttk.Separator(toolbarcontent, orient=tk.HORIZONTAL)
        
        img = tk.PhotoImage(file="resources/icons/bitcons/icons/gif/tan/16x16/save.gif")
        testbutton = ttk.Button(mainPane, image=img, style='Toolbutton', command=self._saveDataTest)
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
    
    def _saveDataTest(self):
        #sanitise first.
        for i in self.JSONdata['basic']['text']:
            i['value'] = i['value'].get()
        for i in self.JSONdata['basic']['list']:
            i['value'] = i['value'].get()
        for i in self.JSONdata['basic']['phone']:
            i['value'] = i['value'].get()
        print(json.dumps(self.JSONdata, sort_keys=False, indent=1, separators=(',', ': ')))
        
    def _windowPreClose(self):
        self._updateConfigs() #update the config files incase they were changed
        
    def _validatePhoneNumber(self, entry):
        number = entry.get()
        number = str(re.sub("\D", "", number))
        formattedNumber = ""
        if len(number) <= 10:
            for i in range(len(number)):
                if (i==0):
                    formattedNumber = "("
                formattedNumber += number[i]
                if (i == 2):
                    formattedNumber += ') '
                elif (i == 5):
                    formattedNumber += '-'
        
        else:
            for i in range(len(number)):
                formattedNumber += number[i]
                if (len(number) - i == 11):
                    formattedNumber += '-'
                elif (len(number) - i == 8):
                    formattedNumber += '-'
                elif (len(number) - i == 4):
                    formattedNumber += '-'
        
        entry.delete(0, tk.END)
        entry.insert(0, formattedNumber)
        
        return True
        