import tkinter as tk
from tkinter import ttk
import tkinter.font as font


def greet(*args):
    print(f'hello {user_name.get()}')


root = tk.Tk()
style = ttk.Style(root)
# print(style.theme_names())
# print(style.theme_use())
# style.theme_use('xpnative')
style.theme_use('clam')
font.nametofont("TkDefaultFont").configure(family="Arial", size=20)
myfont = font.Font(family="B Aseman", size=14, weight="bold")
# style.configure("Custom.TLabel", font=("Arial", 20))

# print(style.layout("TLabel"))
# print(style.element_options("Label.border"))
# print(style.element_options("Label.padding"))
# print(style.element_options("Label.label"))
# print(style.lookup("TLabel", 'font'))
# print(style.lookup("TLabel", 'foreground'))
# print(style.lookup("TLabel", 'background'))
# print(style.lookup("TLabel", 'compound'))
style.configure('TLabel', bordercolor="red", relief="solid",
                borderwidth=20, background="green", foreground="orange")
style.configure("customEntryStyle.TEntry", padding=20)
style.configure("TButton", background="gray", foreground="blue",
                font=15, bordercolor="green", relief="solid", borderwidth=20)
style.map("TButton", foreground=[
          ("pressed", "red"), ("active", "brown")], font=[("pressed", ("TkDefaultFont", 20)), ("active", ("TkDefaultFont", 20))])
style.map("TButton", background=[("pressed", "cyan"), ("active", "yellow")])


main = ttk.Frame(root, padding=(40, 20))
main.grid()

user_name = tk.StringVar()

name_label = ttk.Label(main, text="Name: ", font=myfont)
name_label.grid(row=0, column=0, padx=(0, 10))

# print(name_label.winfo_class())


name_entry = ttk.Entry(main, width=15, textvariable=user_name,
                       style="customEntryStyle.TEntry", font=("Arial", 20))
name_entry.grid(row=0, column=1, padx=10)
name_entry.focus()


greet_button = ttk.Button(main, text="Greet", command=greet)
greet_button.grid(row=1, column=0, columnspan=2, sticky="ew", pady=(10, 0))

root.mainloop()
