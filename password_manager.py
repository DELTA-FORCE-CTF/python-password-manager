#This code was rushed to be made. I probably registered a few unnecessary variables, so just play around with this until you find what is shortest.
import tkinter as tk #imports tkinter as tk, which is shorter to type.
from tkinter import messagebox #imports a message box which will be used in the openList function.

def buttonClicked(): #Defines the function buttonClicked, used for the first button.
    userInfo = "Name: " + sv1.get() + ", Password: " + sv2.get() + "\n" #Gets the input of entries e1 and e1 and puts them in the format of "Name: <name>, Password: <password>".
    mkf = open("data.txt", "a") #Opens the file named data.txt. We open it with "a" so we can append to the file.
    mkf.write(userInfo) #Writes the variable "userInfo" which is the name and password.
    mkf.close() #Closes the file. We don't want it stored in RAM until the program closes, do we? (Although the file is small, it is not good practive to keep unnecessary files loaded in RAM)

def openList(): #Defines the function openList, used for the second button.
    opf = open("data.txt", "r") #Opens the file read only, since we don't need to make changes to the file.
    getdata = opf.read() #Gets the data of the file and puts it in the getdata variable.
    opf.close() #Again, we don't want to keep this file in RAM.
    messagebox.showinfo("Names and passwords", getdata) #Makes the gui that shows our names and passwords.

mkf = open("data.txt", "a") #Creates the file "data.txt" if it hasn't been created already. DO NOT DELETE THIS FILE!
mkf.close() #Closing the file.

main = tk.Tk(className=" Password Manager (partial GUI)") #Creates the main window. className names the window, but this is not required.
#main.geometry("800x200") #Gets the size of the window, in pixels. Made with the length x width format. I commented this line out so it could size itself better, but you can uncomment the line and play around with it a little.
tk.Label(main, text="Password manager for LSW. Enter name in the first field, and the password in the second.").pack() #Makes the text that you see when opening the gui.
sv1=tk.StringVar() #Registers string variables so we can get the text from out entries.
sv2=tk.StringVar() # ^
e1 = tk.Entry(main, width=30, textvariable=sv1).pack() #These are the user input fields.
e2 = tk.Entry(main, width=50, textvariable=sv2).pack() # ^
b1 = tk.Button(main, text="Click here when both fields are filled to save password.", command=buttonClicked).pack() #Creates the button that uses the buttonClicked function.
b2 = tk.Button(main, text="Click to see names and passwords.", command = openList).pack() #Creates the button that uses the openList function.
main.mainloop() #You need this, or else the window and close in a short amount of time, about a few hundreths of a second.



