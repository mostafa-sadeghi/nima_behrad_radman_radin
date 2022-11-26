import tkinter as tk
from tkinter import ttk

root = tk.Tk()
selection_var = tk.StringVar()


def func():
    print(selection_var.get())


option1 = ttk.Radiobutton(
    root, text="pizza", variable=selection_var, value="pizza", command=func).pack(anchor='w')
option2 = ttk.Radiobutton(
    root, text="cheese", variable=selection_var, value="cheese", command=func).pack(anchor='w')
option3 = ttk.Radiobutton(root, text="pepperoni",
                          variable=selection_var, value="pepperoni", command=func).pack(anchor='w')

root.mainloop()


# exercise : write above code three time
