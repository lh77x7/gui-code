import tkinter as tk
import tkinter as ttk

windows = tk.Tk()
#adding modified label
m_label = ttk.Label(windows, text="Modified label")
m_label.grid(column=0, row=0)

#container for labels
buttons_frame = ttk.LabelFrame(windows, text=' Label in frame')
buttons_frame.grid(column=0, row=7)

#place labels into container in one row
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

#place labels into container in one column, first row = 2
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=2)
ttk.Label(buttons_frame, text="Label2").grid(column=0, row=3)
ttk.Label(buttons_frame, text="Label3").grid(column=0, row=4)

#set padding for labels in column
for child in buttons_frame.winfo_children():
    child.grid_configure(padx=8, pady=4)

#gui call
windows.mainloop()
