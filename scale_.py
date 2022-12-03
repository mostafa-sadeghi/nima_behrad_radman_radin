import tkinter as tk
from tkinter import ttk


def handle_scale(e):
    print(scale.get())


root = tk.Tk()
scale = ttk.Scale(root, orient="horizontal", from_=0,
                  to=20, command=handle_scale)
scale.pack()


root.mainloop()
