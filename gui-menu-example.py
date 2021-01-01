#import or functions from tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import Menu

win = tk.Tk(className="Python Gui with menu")
win.geometry("300x300")
#adding modified label
m_label = ttk.Label(win, text="Modified label")
m_label.grid(column=1, row=1)
#create menu bar
menuBar = Menu(win)
win.config(menu=menuBar)

#create menu and add menu items
file_menu = Menu(menuBar, tearoff=0) #create File menuBar
file_menu.add_command(label="New") #add File menu item
file_menu.add_separator() #add separator
file_menu.add_command(label="Exit") #add next File menu item
menuBar.add_cascade(label="File", menu=file_menu)

#gui call
win.mainloop()
