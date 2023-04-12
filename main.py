from tkinter import *
 
# create root window
root = Tk()
 
# root window title and dimension
root.title("This is an app")
# Set geometry (widthxheight)
root.geometry('1000x500')
 
# add menu
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

root.mainloop()