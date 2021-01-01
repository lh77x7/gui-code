import tkinter as tk
import tkinter as ttk

windows = tk.Tk()
#adding modified label
m_label = ttk.Label(windows, text="Modified label")
m_label.grid(column=0, row=0)

#click event function
def click_label():
    action.configure(text="Clicked!")
    m_label.configure(fg='white', bg='red')

action = ttk.Button(windows, text='Click me', command=click_label)
action.grid(column=1, row=0)

#gui call
windows.mainloop()
