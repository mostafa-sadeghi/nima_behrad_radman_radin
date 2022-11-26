# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()

# checkbutton = ttk.Checkbutton(root, text="pizza", state="disabled")
# checkbutton.pack()
# checkbutton['state'] = "normal"
# root.mainloop()

# exercise : add image to checkbutton like adding pic to labels in past sessions

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

selected_option = tk.StringVar()


def print_selection():
    print(selected_option.get())


checkbutton = ttk.Checkbutton(
    root, text="pizza", state="disabled", variable=selected_option, command=print_selection, onvalue="on", offvalue="off")
checkbutton.pack()
checkbutton['state'] = "normal"
root.mainloop()


# Exercise : write it 2 times
