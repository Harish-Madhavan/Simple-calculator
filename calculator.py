import customtkinter

#Create an instance of Tkinter frame
win= customtkinter.CTk()

#Set the geometry of Tkinter frame
win.geometry("750x250")
win.title("Calculator")

def display_text():
   global entry
   string= entry.get()
   if(string.isalpha() and string!="x"):
      label.configure(text="enter numbers")
   else:
      a=""
      for i in string:
         if i=="x":
            a+="*"
         else:
            a+=i
      string1=eval(a)
      label.configure(text=string1)

#Initialize a Label to display the User Input
label=customtkinter.CTkLabel(master=win, text="", font=("Courier",22,"bold"))
label.pack(anchor="center")
label.place(x=250,y=100)

#Create an Entry widget to accept User Input
entry= customtkinter.CTkEntry(master=win, width= 350)
entry.focus_set()
entry.pack(anchor="n")
entry.place(x=200,y=25)

#Create a Button to validate Entry Widget
button1= customtkinter.CTkButton(master= win, text= "Okay",width= 50, command= display_text).place(x=350,y=200)

win.mainloop()
