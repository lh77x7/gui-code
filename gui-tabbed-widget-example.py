import tkinter as tk
from tkinter import ttk

windows = tk.Tk()                   #create instance
windows.title("Python GUI")         #add title
tabControl = ttk.Notebook(windows)  #create tab tabControl
tab1 = ttk.Frame(tabControl)        #create tab
tabControl.add(tab1, text="Tab 1")  #add tab
tabControl.pack(expand = 1, fill ="both") #pack to make visible
tab2 = ttk.Frame(tabControl)        #create second tab
tabControl.add(tab2, text="Tab 2")  #add second tab

windows.mainloop()                  #gui start
