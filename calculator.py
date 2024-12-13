import customtkinter
import ast
#Create an instance of Tkinter frame
win= customtkinter.CTk()

#Set the geometry of Tkinter frame
win.geometry("750x250")
win.title("Calculator")


def display_text():
    global entry, label
    string = entry.get()

    if not string:
       label.configure(text="Enter any numbers or expressions")
       return
    
    # Clean and Validate Input
    cleaned_string = ""
    allowed_chars = "0123456789.+-/x()%^"
    for char in string:
        if char in allowed_chars:
           if char == 'x':
                cleaned_string += '*' # Convert 'x' to '*' for multiplication
           elif char == '^':
                cleaned_string += '**' # Convert '^' to '**' for power
           else:
              cleaned_string += char
        else:
             label.configure(text="Invalid Input")
             return

    if not cleaned_string:
        label.configure(text="Enter numbers or expressions")
        return

    # Perform Calculation using ast.literal_eval
    try:
        # Using ast.literal_eval for evaluation
        string1 = safe_eval(cleaned_string)
        label.configure(text=string1)
    except Exception as e:
        label.configure(text=f"Invalid Expression or Error: {e}")

def safe_eval(expression):
   try:
        node = ast.parse(expression, mode='eval')
        
        # Check if the expression contains only allowed nodes
        if not isinstance(node, ast.Expression):
            return "Invalid Expression"
        
        for n in ast.walk(node):
           if isinstance(n,(ast.Call,ast.Attribute,ast.Name)):
              return "Invalid Expression"

        return eval(compile(node, '<string>', 'eval')) #use eval to parse the code
   except:
      return "Invalid Expression"

#Initialize a Label to display the User Input
label=customtkinter.CTkLabel(master=win, text="", font=("Courier",22,"bold"))
label.place(x=250,y=100)

#Create an Entry widget to accept User Input
entry= customtkinter.CTkEntry(master=win, width= 350)
entry.focus_set()
entry.place(x=200,y=25)

#Create a Button to validate Entry Widget
button1= customtkinter.CTkButton(master= win, text= "=",width= 50, command= display_text).place(x=350,y=200)

win.mainloop()
