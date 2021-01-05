#import or functions from tkinter library
import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox as msg

#define tooltip class
class Tooltip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave', self.mouse_leave)

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_window:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18
            pass

    def hide_tooptip(self):
        pass

#end define class
