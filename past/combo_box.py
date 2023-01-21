import tkinter as tk
from tkinter import ttk


def handle_selection(event):
    print("selected day is", selected_weekday.get())


root = tk.Tk()

selected_weekday = tk.StringVar()
weekday = ttk.Combobox(root, textvariable=selected_weekday)
weekday['values'] = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
weekday['state'] = 'readonly'

weekday.bind('<<ComboboxSelected>>', handle_selection)

weekday.pack()


root.mainloop()
