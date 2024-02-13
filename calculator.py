from tkinter import *
import customtkinter 
from tkinter import ttk

#Create an instance of Tkinter frame
win= customtkinter.CTk()

#Set the geometry of Tkinter frame
win.geometry("750x250")
win.title("Calculator")

def display_text():
   global entry
   string= entry.get()
   if(string.isalpha()):
      label.configure(text="enter numbers")
   else:
      string1=eval(string)
      label.configure(text=string1)

#Initialize a Label to display the User Input
label=Label(win, text="", font=("Courier 22 bold"))
label.pack(anchor="center")
label.place(x=250,y=100)

#Create an Entry widget to accept User Input
entry= Entry(win, width= 40)
entry.focus_set()
entry.pack(anchor="n")
entry.place(x=250,y=25)

#Create a Button to validate Entry Widget
ttk.Button(win, text= "Okay",width= 20, command= display_text).place(x=300,y=200)

win.mainloop()
