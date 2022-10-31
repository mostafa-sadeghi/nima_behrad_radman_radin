from logging import root
import tkinter as tk
from tkinter import ttk


# def greet():
#     print("hello world")


# root = tk.Tk()
# # ttk.Label(root, text="hello world!", padding=(50, 30)).pack()
# greet_button = ttk.Button(root, text="greet", command=greet)
# greet_button.pack(side="left", fill="both", expand=True)
# quit_button = ttk.Button(root, text="quit", command=root.destroy)
# quit_button.pack(side="left", fill="both", expand=True)
# root.mainloop()

root = tk.Tk()
root.geometry("600x400")


def greet():
    print(f'hello {user_name.get()}')


user_name = tk.StringVar()
name_label = ttk.Label(root, text="Name:")
name_label.pack(side="left", padx=(0, 10))
# add text box
name_entry = ttk.Entry(root, width=20, textvariable=user_name)
name_entry.pack(side="left")

# add buttons
greet_button = ttk.Button(root, text="greet", command=greet)
greet_button.pack(side="left")
quit_button = ttk.Button(root, text="quit", command=root.destroy)
quit_button.pack(side="left")

root.mainloop()
