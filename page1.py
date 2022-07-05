from tkinter import *
from tkinter import ttk
from datetime import date

#window
tkWindow = Tk()  
tkWindow.geometry('400x150')  
tkWindow.title('Expense Management App Login')

saved_username = 'kien'
saved_password = '123'

def validateLogin_f():
    user_input_username = username.get()
    user_input_pw = password.get()
    if user_input_username == saved_username and user_input_pw == saved_password :
        notification_lbl.config(text= "successfully logged in as " + user_input_username)
        nextPage()
    else:
        notification_lbl.config(text= "Please check your username and password again")
    print("username entered :", username.get())
    print("password entered :", password.get())
    return

login_frame = Frame(tkWindow)
login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor= 'center')

#username label and text entry box
usernameLabel = Label(login_frame, text="User Name").grid(row=0, column=0)
username = StringVar()
usernameEntry_widget = Entry(login_frame, textvariable=username).grid(row=0, column=1)  

#password label and password entry box
passwordLabel = Label(login_frame,text="Password").grid(row=1, column=0)  
password = StringVar()
passwordEntry_widget = Entry(login_frame, textvariable=password, show='*').grid(row=1, column=1)  

notification_lbl = Label(login_frame, text= "...")
notification_lbl.grid(row=6,column=1)


#login button
loginButton = Button(login_frame, text="Login", command = validateLogin_f).grid(row=4, column=1)  


def nextPage():
    tkWindow.destroy()
    import page2



tkWindow.mainloop()