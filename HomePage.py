import tkinter as tk
from tkinter import ttk

import os
from tkinter.filedialog import askopenfilename

from legacy import execfile



LARGE_FONT=("Times New Roman", 32)
MEDIUM_FONT=("Times New Roman", 14)

class FRoST(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        #tk.Tk.iconbitmap(self,default='clienticon.ico')
        tk.Tk.wm_title(self, "FRoST CAMP")

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (HomePage, RegistrationPage, NotificationPage, CheckInPage,
                  BandAssignmentPage, DormAssignmentPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(HomePage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class HomePage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self,parent)


        #Label for the Home page heading
        Label = ttk.Label(self, text='Future RockStars Registration Software', font=LARGE_FONT)
        Label.pack(pady=10,padx=10)

        #label and button for the registration page
        Label2 = ttk.Label(self, text='To register a new camper select the Registration button', font=MEDIUM_FONT)
        Label2.pack(pady=10,padx=10)
        button = ttk.Button(self, text='Registration',
                            command = lambda: controller.show_frame(RegistrationPage))
        button.pack()

        #label and button for the notification page
        Label3 = ttk.Label(self, text='To check whether a package needs to be sent to the camper select the Notification button', font=MEDIUM_FONT)
        Label3.pack(pady=10, padx=10)
        button2 = ttk.Button(self, text='Notification',
                            command=lambda: controller.show_frame(NotificationPage))
        button2.pack()

        #label and button for the check-in page
        Label4 = ttk.Label(self, text='To Check-In a camper into the system select the Check-In button', font=MEDIUM_FONT)
        Label4.pack(pady=10, padx=10)
        button3 = ttk.Button(self, text='Check In',
                            command=lambda: controller.show_frame(CheckInPage))
        button3.pack()

        #Label and button for the band assignment
        Label5 = ttk.Label(self, text='To allocate a specific band to a camper select the band assignment button', font=MEDIUM_FONT)
        Label5.pack(pady=10, padx=10)
        button4 = ttk.Button(self, text='Band Assignment',
                            command=lambda: controller.show_frame(BandAssignmentPage))
        button4.pack()

        #Label and button for the dorm assignment
        Label6 = ttk.Label(self, text='To allocate a dorm to the camper select the dorm assignment button', font=MEDIUM_FONT)
        Label6.pack(pady=10, padx=10)
        button5 = ttk.Button(self, text='Dorm Assignment',
                            command=lambda: controller.show_frame(DormAssignmentPage))
        button5.pack()


        #Exit the application
        button7 = ttk. Button(self, text='Exit',
                              command=lambda: exit())
        button7.pack(pady=10, padx=10)

class RegistrationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Registration Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        #self.create_widgets()


        Label1 = ttk.Label(self, text = "To register the student click on the Register button", font=MEDIUM_FONT)
        Label1.pack(pady=60, padx=60)

        registerbutton = ttk.Button(self, text="Register",
                                    command = lambda: execfile("Registration.py",{}))
        registerbutton.pack(pady=10, padx=10)


        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Go to Notification Page",
                            command=lambda: execfile('Notification.py',{}))
        button2.pack(pady=10, padx=10)

class NotificationPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Notification Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Label1 = ttk.Label(self, text="To send notification to the student click on the Notification button", font=MEDIUM_FONT)
        Label1.pack(pady=60, padx=60)

        notifybutton = ttk.Button(self, text="Notify",
                                    command=lambda: execfile("Notification.py",{}))
        notifybutton.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Go to Check In Page",
                            command=lambda: execfile("CheckInPage.py", {}))
        button2.pack(pady=10, padx=10)


class CheckInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Check-In Page", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Label1 = ttk.Label(self, text="To commence with Check-In of a camper click on the Check-In button", font=MEDIUM_FONT)
        Label1.pack(pady=60, padx=60)

        CheckInbutton = ttk.Button(self, text="Check-In",
                                  command=lambda: execfile("CheckInPage.py", {}))
        CheckInbutton.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Go to Band Assignment",
                            command=lambda: execfile("BandAssignment.py", {}))
        button2.pack(pady=10, padx=10)


class BandAssignmentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Band Assignment", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Label1 = ttk.Label(self, text="To allocate band for a camper click on the Band Assginment button", font=MEDIUM_FONT)
        Label1.pack(pady=60, padx=60)

        BandAssignmentbutton = ttk.Button(self, text="Band Assignment",
                                  command=lambda: execfile("BandAssignment.py", {}))
        BandAssignmentbutton.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10, padx=10)

        button2 = ttk.Button(self, text="Go to Dorm Assignment",
                             command=lambda: execfile("DormAssignment.py",{}))
        button2.pack(pady=10, padx=10)



class DormAssignmentPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text="Dorm Assignment", font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        Label1 = ttk.Label(self, text="To allocate dorms to campers click on the Dorm Assignment button", font=MEDIUM_FONT)
        Label1.pack(pady=60, padx=60)

        DormAssignmentbutton = ttk.Button(self, text="Dorm Assignment",
                                  command=lambda: execfile("DormAssignment.py",{}))
        DormAssignmentbutton.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(HomePage))
        button1.pack(pady=10, padx=10)


app = FRoST()
app.mainloop()