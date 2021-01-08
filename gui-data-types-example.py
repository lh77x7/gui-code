import tkinter as tk

win = tk.Tk()

doubleData = tk.DoubleVar()
print(doubleData.get())
doubleData.set(2.4)
print(type(doubleData))

addDoubles = 1.22222222222222 + doubleData.get()
print(addDoubles)
print(type(addDoubles))
