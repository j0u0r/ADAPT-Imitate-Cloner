from tkinter import *
from tkinter import filedialog
import pandas as pd

def browse_button():
    filename = filedialog.askopenfile(title="Select CSV file...")
    return filename


window = Tk()
Uploadbtn = Button(text="Browse", command=browse_button).grid(row=0, column=3)
mainloop()