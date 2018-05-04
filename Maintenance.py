import os
from tkinter.ttk import Frame, Button, Entry

from tkinter import *
import sys

#import stream
from legacy import execfile

sys.path.append("/path/to/script/file/directory/")

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()


    def create_widgets(self):
        self.instruction = Label(self, text="Application ID")
        self.instruction.grid(row=0, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)

        self.b2 = Button(self, text="Edit Member Information",
                         command=lambda: execfile("Registration.py",{}))
        self.b2.grid(row=2, column=0)

        self.b2 = Button(self, text="Delete Previous data",
                         command=lambda: execfile("Delete.py",{}))
        self.b2.grid(row=2, column=1)

root = Tk()
root.geometry("500x200")
root.title("Maintenance Page")
app = App(root)

root.mainloop()
