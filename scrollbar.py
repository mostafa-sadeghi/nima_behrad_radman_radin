# scrollBars
from tkinter import ttk, NONE
import tkinter as tk

root = tk.Tk()
text = tk.Text(root, height=8, width=30, wrap=NONE)
text.grid(row=0, column=0, sticky="ew")

text_scroll = ttk.Scrollbar(
    root, orient="horizontal", command=text.xview)
text_scroll.grid(row=1, column=0, sticky="ew")

# text["yscrollcommand"] = text_scroll.set
text["xscrollcommand"] = text_scroll.set
root.mainloop()


# exercise : write above code three time and change it to vertical scrollBar

