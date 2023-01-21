import tkinter as tk
from tkinter import ttk

root = tk.Tk()
selection = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selection)
weekday['values'] = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
weekday.pack()
root.mainloop()


# exercise : write it 3 times and print selected day
