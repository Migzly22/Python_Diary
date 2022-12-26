

import json
import os
import numpy as np
import tkinter as tk
import customtkinter as ct
from tkinter import filedialog
import tkinter.scrolledtext as st



BASE_DIR= os.path.dirname(os.path.abspath(__file__))


#Set the initial themes of the app window 
ct.set_appearance_mode("Dark")
#ct.set_default_color_theme(BASE_DIR + "\\themes.json")


class TextRedirector(object):
#Handles console output to GUI
    def __init__(self, widget, tag="stdout"):
        self.widget = widget
        self.tag = tag
    def write(self, str):
        self.widget.configure(state="normal")
        self.widget.insert("end", str, (self.tag,)) 
        self.widget.see("end")
        self.widget.configure(state="disabled")
    def flush(self):
        self.widget.update()


class App(ct.CTk):
    WIDTH =800
    HEIGHT = 600

    def __init__(self): 
        super().__init__()

        self.title("DDiary") 
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.resizable (width=False, height=False)


        self.mainframe = ct.CTkFrame(master= self, width= App.WIDTH-40 , corner_radius= 0, height= App.HEIGHT-40) 
        self.mainframe.grid(row=0, column=0, sticky="nswe", padx = 20, pady =20)

        self.mainframe.grid_rowconfigure(1, minsize=10) # empty row with minsize as spacing 

        self.titlepart = ct.CTkEntry(master=self.mainframe, width= App.WIDTH/2, height= 30, font = ("Roboto Medium", 15), placeholder_text="Title")
        self.titlepart.grid(row=0, column= 0, pady = 20)

        self.Label1 = ct.CTkLabel(master = self.mainframe, text="Let me read your story :", font=("Roboto Medium", -14)) # text_font=("Roboto Medium", -14)
        self.Label1.grid(row=1, column=0, sticky='w', padx = 20)
        
        self.textbox = ct.CTkTextbox(master=self.mainframe, width=App.WIDTH-80, height= 200, font = ("Roboto Medium", 15))
        self.textbox.grid(row=2, column= 0, padx = 20, pady =(0,20))

        self.clearanything = ct.CTkButton(master=self.mainframe, text="Clear", command=self.Clearing)
        self.clearanything.grid(row=3, column=0, padx=20, pady =(0,20) ,sticky='w' ) # w means left while e is right

        self.savedata = ct.CTkButton(master=self.mainframe, text="Save", command=self.Saving)
        self.savedata.grid(row=3, column=0, padx=20, pady =(0,20) ,sticky='e' ) # w means left while e is right

        self.Reading()#read the last data entered and printing the value 

    def Clearing(self):
        #self.textbox.insert("0.0", 'default text')# to insert value
        self.textbox.delete("0.0","end")

    def Saving(self):
        self.title = self.titlepart.get()#to get the value of entry
        self.datatobesave = self.textbox.get("0.0", "end-1c")# to get the value of textbox

        dictionary = {}
        dictionary[self.title] = self.datatobesave

        dataenter = json.dumps(dictionary, indent=4)
        with open(BASE_DIR +"\\storage.json", "w") as outfile: # open the file and have a write property
            outfile.write(dataenter)  # to write in the object



    def Reading(self):
        with open(BASE_DIR +"\\storage.json") as json_file:
            readdata = json.load(json_file)
            listofdata = list(readdata.keys())

            if (len(listofdata) != 0):
                self.rtitle = listofdata[len(listofdata)-1]
                self.rdata = readdata[listofdata[len(listofdata)-1]]
        
                self.titlepart.insert(0, self.rtitle)#set value in the text
                self.textbox.insert("0.0", self.rdata)# to insert value
            




if __name__ == "__main__": 
    app = App()
    app.mainloop()

