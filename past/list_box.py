import tkinter as tk
from tkinter import ttk


def handle_selection(e):
    selected_items = langs_select.curselection()
    for item in selected_items:
        print(langs_select.get(item))


root = tk.Tk()

prog_langs = ('c', 'c++', 'java', 'python')
langs = tk.StringVar(value=prog_langs)
langs_select = tk.Listbox(root, listvariable=langs,
                          height=4, selectmode='extended')
langs_select.pack()
langs_select.bind("<<ListboxSelect>>", handle_selection)


root.mainloop()
