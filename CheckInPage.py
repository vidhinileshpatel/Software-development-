import os
from tkinter import ttk
from tkinter.ttk import Frame, Button, Entry
import tkinter as tk

from tkinter import *
import sys


sys.path.append("/path/to/script/file/directory/")
app = Tk


class FRoST(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "FRoST CAMP")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (CheckInPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(CheckInPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()



class CheckInPage(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):

        self.instruction = Label(self, text="Application ID")
        self.instruction.grid(row=0, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)

        self.instruction = Label(self, text="First Name")
        self.instruction.grid(row=1, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=1, column=1)

        self.instruction = Label(self, text="Last Name")
        self.instruction.grid(row=2, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=2, column=1)

        self.instruction = Label(self, text="Application Form Submitted")
        self.instruction.grid(row=3, column=0)

        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=3, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=3, column=2)

        self.instruction = Label(self, text="Legal Form Submitted")
        self.instruction.grid(row=4, column=0)

        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=4, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=4, column=2)

        self.instruction = Label(self, text="List of Items to be brought sent")
        self.instruction.grid(row=5, column=0)

        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=5, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=5, column=2)

        self.button1 = ttk.Button(self, text="Save")  # command add the data from above into database
        self.button1.grid(row=6, column=0)

        self.button2 = ttk.Button(self, text="Cancel")  # command add the data from above into database
        self.button2.grid(row=6, column=1)


root = Tk()
root.geometry("500x200")
root.title("Check-In Page")
app = CheckInPage(root)
root.mainloop()
