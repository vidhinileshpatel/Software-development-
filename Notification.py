import os
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Frame, Button, Entry

from tkinter import *
import sys

#import stream
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

        self.instruction = Label(self, text="Accepted")
        self.instruction.grid(row=1, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=1, column=1)


        self.instruction = Label(self, text="Rejected")
        self.instruction.grid(row=2, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=2, column=1)


        self.instruction = Label(self, text="Total Payment")
        self.instruction.grid(row=3, column=0)

        self.entry = Entry(self)
        self.entry.grid(row=3, column=1)



root = Tk()
root.geometry("500x200")
root.title("Notification Page")
app = App(root)

root.mainloop()
