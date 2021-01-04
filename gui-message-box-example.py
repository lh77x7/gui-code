#import or functions from tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg


win = tk.Tk(className="Python Gui with menu")
win.geometry("300x300")

#adding modified label
m_label = ttk.Label(win, text="Modified label")
m_label.grid(column=1, row=1)

#exit functions
def _quit():
    win.quit()
    win.destroy()
    exit()

def _msgBox():
    #win.withdraw()
    msg.showinfo('Python messagebox', 'Message into messagebox')

#create menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

#create menu and add menu items
file_menu = Menu(menuBar, tearoff=0) #create File menuBar
file_menu.add_command(label="New") #add File menu item
file_menu.add_separator() #add separator
file_menu.add_command(label="Exit", command=_quit) #add next File menu item
menuBar.add_cascade(label="File", menu=file_menu)

#add another menu with items
help_menu = Menu(menuBar, tearoff=0)
menuBar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=_msgBox)

#gui call
win.mainloop()
