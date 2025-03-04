import tkinter as tk
from tkinter import *

display = tk.Tk()


nameBoxLBL = tk.Label(display, text="Name: ")
nameBoxLBL.grid(row=1,column=3)

nameBoxENT = tk.Entry(display)
nameBoxENT.grid(row=2,column=3)

display.attributes('-fullscreen', True)
mainloop()