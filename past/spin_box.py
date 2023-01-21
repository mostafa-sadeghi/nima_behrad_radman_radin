import tkinter as tk
from tkinter import ttk

root = tk.Tk()

init_val = tk.IntVar(value=10)
spin_box = ttk.Spinbox(root, from_=0, to=25, textvariable=init_val, wrap=True)
spin_box.pack()


root.mainloop()
