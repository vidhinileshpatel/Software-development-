import os
#from sqlite3 import Date
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Frame, Button, Entry

from tkinter import *
import sys
import tkinter as tk


#import stream


sys.path.append("/path/to/script/file/directory/")

import MySQLdb

db = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="rameshsingh123",  # your password
                     db="frost")
#cur = db.cursor()

class App(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    
    def buttonclick(self):
        print(self.var2.get(), self.var3.get(), self.var4.get(), self.var5.get(), self.var6.get())
        if (db):
        # Carry out normal procedure
            print ("Connection successful")
            try:
                cur.execute("INSERT INTO Student (FirstName, LastName, Age, Gender,Email, PhoneNumber, AddressLine1, AddressLine2, City, State, ZipCode, Country) values('+self.var2.get+','+self.var3.get+','+self.var4.get+','+self.var5.get+','+self.var6.get+','+self.var7.get+','+self.var8.get+', '+self.var9.get+','+self.var10.get+','+self.var11.get+','+self.var12.get+', '+self.var13.get+' )")
                print('one row inserted')
                db.commit()
                cur.execute("SELECT * FROM Student")
                for row in cur.fetchall():
                    print(row)
            except:
                db.rollback()
        else:
        # Terminate
            cur.close()
            db.close()
            print ("Connection unsuccessful")
        cur = db.cursor()

    def create_widgets(self):

        #create_dict = {}
        self.instruction = Label(self, text="Application ID")
        self.instruction.grid(row=0, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=0, column=1)
        #print(create_dict)

        self.var2 = StringVar()
        self.instruction = Label(self, text="First Name")
        self.instruction.grid(row=1, column=0)
        self.entry = Entry(self, textvariable=self.var2)
        self.entry.grid(row=1, column=1)

        self.var3 = StringVar()
        self.instruction = Label(self, text="Last Name")
        self.instruction.grid(row=2, column=0)
        self.entry = Entry(self, textvariable=self.var3)
        self.entry.grid(row=2, column=1)

        self.instruction = Label(self, text="Select Age Group")
        self.instruction.grid(row=3, column=0)
        #self.Radiobutton1 = Radiobutton(self, text="13-14", command=YES, value = 1)
        #self.Radiobutton1.grid(row=3, column=2)
        #self.Radiobutton2 = Radiobutton(self, text="15-16", command=NO, value = 2)
        #self.Radiobutton2.grid(row=3, column=3)
        #self.Radiobutton3 = Radiobutton(self, text="17-18", command=YES, value =3)
        #self.Radiobutton3.grid(row=3, column=4)
        self.Checkbutton1 = Checkbutton(self, text="13-14", command=YES)
        self.Checkbutton1.grid(row=3, column=1)
        self.Checkbutton2 = Checkbutton(self, text="15-16", command=NO)
        self.Checkbutton2.grid(row=3, column=2)
        self.Checkbutton3 = Checkbutton(self, text="17-18", command=YES)
        self.Checkbutton3.grid(row=3, column=3)

        self.var4 = StringVar()
        self.instruction = Label(self, text="Age")
        self.instruction.grid(row=4, column=0)
        self.entry = Entry(self, textvariable=self.var4)
        self.entry.grid(row=4, column=1)


        self.var5 = StringVar()
        self.instruction = Label(self, text="Gender")
        self.instruction.grid(row=5, column=0)
        self.Radiobutton5 = Radiobutton(self, text="Male", command=YES, value = 5)
        self.Radiobutton5.grid(row=5, column=1)
        self.Radiobutton6 = Radiobutton(self, text="Female", command=NO, value = 6)
        self.Radiobutton6.grid(row=5, column=2)
        self.Radiobutton7 = Radiobutton(self, text="Other", command=NO, value = 7)
        self.Radiobutton7.grid(row=5, column=3)

        self.var6 = StringVar()
        self.instruction = Label(self, text="Email")
        self.instruction.grid(row=6, column=0)
        self.entry = Entry(self, textvariable=self.var6)
        self.entry.grid(row=6, column=1)


        self.var7 = StringVar()
        self.instruction = Label(self, text="Phone Number")
        self.instruction.grid(row=7, column=0)
        self.entry = Entry(self, textvariable=self.var7)
        self.entry.grid(row=7, column=1)


        self.var8 = StringVar()
        self.instruction = Label(self, text="Address Line 1")
        self.instruction.grid(row=8, column=0)
        self.entry = Entry(self, textvariable=self.var8)
        self.entry.grid(row=8, column=1)


        self.var9 = StringVar()
        self.instruction = Label(self, text="Address Line 2")
        self.instruction.grid(row=9, column=0)
        self.entry = Entry(self, textvariable=self.var9)
        self.entry.grid(row=9, column=1)



        self.var10 = StringVar()
        self.instruction = Label(self, text="City")
        self.instruction.grid(row=10, column=0)
        self.entry = Entry(self, textvariable=self.var10)
        self.entry.grid(row=10, column=1)


        self.var11 = StringVar()
        self.instruction = Label(self, text="State")
        self.instruction.grid(row=11, column=0)
        self.entry = Entry(self, textvariable=self.var11)
        self.entry.grid(row=11, column=1)

        self.var12 = StringVar()
        self.instruction = Label(self, text="Zip Code")
        self.instruction.grid(row=12, column=0)
        self.entry = Entry(self, textvariable=self.var12)
        self.entry.grid(row=12, column=1)

        self.var13 = StringVar()
        self.instruction = Label(self, text="Country")
        self.instruction.grid(row=13, column=0)
        self.entry = Entry(self, textvariable=self.var13)
        self.entry.grid(row=13, column=1)


        self.instruction = Label(self, text="Emergency Contact")
        self.instruction.grid(row=14, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=14, column=1)


        self.instruction = Label(self, text="Medical Info")
        self.instruction.grid(row=15, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=15, column=1)


        self.instruction = Label(self, text="Personal Essay Sent")
        self.instruction.grid(row=16, column=0)
        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=16, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=16, column=2)


        var1 = StringVar()
        self.instruction1 = Label(self, text="Instrument Choice")
        self.instruction1.grid(row=17, column=0)
        self.entry = Entry(self, textvariable=var1)
        self.entry.grid(row=17, column=1)


        self.instruction = Label(self, text="Proficiency Choice")
        self.instruction.grid(row=18, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=18, column=1)


        self.instruction = Label(self, text="Recording Sent")
        self.instruction.grid(row=19, column=0)
        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=19, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=19, column=2)


        self.instruction = Label(self, text="Payment Completed")
        self.instruction.grid(row=20, column=0)
        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=20, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=20, column=2)



        self.instruction = Label(self, text="Disability Check")
        self.instruction.grid(row=21, column=0)
        self.Checkbutton1 = Checkbutton(self, text="I have disabilities", command=YES)
        self.Checkbutton1.grid(row=21, column=1)
        self.Checkbutton2 = Checkbutton(self, text="I do not have disabilities", command=NO)
        self.Checkbutton2.grid(row=21, column=2)
        self.Checkbutton1 = Checkbutton(self, text="I do not wish to answer", command=YES)
        self.Checkbutton1.grid(row=21, column=3)


        self.instruction = Label(self, text="Signature")
        self.instruction.grid(row=22, column=0)
        self.Checkbutton1 = Checkbutton(self, text="Yes", command=YES)
        self.Checkbutton1.grid(row=22, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=22, column=2)


        self.instruction = Label(self, text="Date of Application Submission")
        self.instruction.grid(row=23, column=0)
        self.entry = Entry(self)
        self.entry.grid(row=23, column=1)


        self.instruction = Label(self, text="Agreements Signed")
        self.instruction.grid(row=24, column=0)
        var = IntVar()
        self.Checkbutton1 = Checkbutton(self, text="Yes", variable=var, command=YES)
        self.Checkbutton1.grid(row=24, column=1)
        self.Checkbutton2 = Checkbutton(self, text="No", command=NO)
        self.Checkbutton2.grid(row=24, column=2)
        #var.get()


        self.b2 = Button(self, text="Register the Camper",
                         command=lambda: self.buttonclick())
        self.b2.grid(row=25, column=0)

        #self.b3 = Button(self, text="Send Notification",
         #             command=lambda : os.system("python C:\Users\Anand Singh Chauhan\Desktop\SD\Notification.py"))
        #self.b3.grid(row=25, column=1)


root = Tk()
root.geometry("600x600")
root.title("Registration Page")
app = App(root)

root.mainloop()
