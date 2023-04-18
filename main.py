import tkinter as tk
from tkinter import *
from tkinter import ttk
import dbControllers

# root window and notebook
root = tk.Tk()
root.title("tab widget")
root.geometry('750x500')
tabControl = ttk.Notebook(root)

# tabs
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

tabControl.add(tab1, text='Main')
tabControl.add(tab2, text='Secondary')

tabControl.pack(expand=1, fill="both")

# tab 1 (new file?)
lbl1 = Label(tab1, text="...")
lbl1.grid(column = 0, row = 0, padx = 30, pady = 30) 

# tab 2 (new file?)
lbl2 = Label(tab2, text="...")
lbl2.grid(column = 0, row = 0, padx = 30, pady = 30) 

# functions
def getTitle():
    res = dbControllers.getTopicColor(titleInput.get())
    lbl2.configure(text = res[0])

titleInput = Entry(tab2, width=10)
titleInput.grid(column = 0, row = 1)

btn = Button(tab2, text = "Send", command=getTitle)
btn.grid(column = 2, row = 1)

root.mainloop()