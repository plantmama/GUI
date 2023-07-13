# FIRST LETS IMPORT NECESSARY PACKAGES 
from tkinter import *
# THE * SYMBOL MEANS EVERYTHING IN THE SPECIFIC PACKAGE
import webbrowser
# CHROME BROWSER
def open_browser():
    url = "https://www.google.com"
    webbrowser.open(url)

# CREATE A VARIABLE FOR THE Tkinter FUNCTION ( Tk() )
gui = Tk()
# NOW GIVE IT A TITLE
gui.title(" Heavenly ")
# LASTLY GIVE IT A HEIGHT AND WIDTH
gui.geometry("300x300")

# Create a label with the string
text_label = Label(gui, text="Welcome, Jasmine.")
# Use the grid layout manager to position the label in the center
text_label.grid(row=0, column=6, padx=50, pady=50)


text_label2 = Label(gui, text="Where would you like to go?")
# Use the grid layout manager to position the label in the center
text_label2.grid(row=2, column=6, padx=10, pady=10)


# Button turns it into a button
button = Button(gui, text="Enter Database")
button.grid(row=3, column=6, padx=20, pady=20)

# Second button next to it
button2 = Button(gui, text="Terminal")
button2.grid(row=3, column=7, padx=20, pady=20)

# NEW BUTTON WITH COMMAND FUNCTION
button3 = Button(gui, text="Access Future", command=open_browser)  
button3.grid(row=5, column=6, padx=20, pady=10)
gui.mainloop()
