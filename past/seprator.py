import tkinter as tk
from tkinter import ttk

root = tk.Tk()

ttk.Label(root, text="label 1").pack()
ttk.Separator(root, orient="horizontal").pack(fill='x')
ttk.Label(root, text="label 2").pack()


root.mainloop()

# exercise : write above code 2 times and test it for vertical orient
