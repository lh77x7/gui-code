import tkinter as tk
import tkinter as ttk

windows = tk.Tk()
windows.title("First windows program")
ttk.Label(windows, text="Label text").grid(column=3, row=0)
windows.mainloop()
