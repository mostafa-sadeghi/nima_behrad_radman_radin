# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry("300x100")


# def greet():
#     print(f'hello {user_name.get()}')


# user_name = tk.StringVar()

# input_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
# input_frame.grid(fill="both", expand=True)


# name_label = ttk.Label(input_frame, text="Name:")
# name_label.grid(side="left", padx=(0, 10), expand=True, fill="both")
# # add text box
# name_entry = ttk.Entry(input_frame, width=20, textvariable=user_name)
# name_entry.grid(side="left", expand=True, fill="both")

# # add buttons

# buttons = ttk.Frame(root, padding=(20, 10))
# buttons.grid(fill="both", expand=True)
# greet_button = ttk.Button(buttons, text="خوشامد", command=greet)
# greet_button.grid(side="left", expand=True, fill="both")
# quit_button = ttk.Button(buttons, text="خروج", command=root.destroy)
# quit_button.grid(side="left", expand=True, fill="both")

# root.mainloop()


import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sample")
root.resizable(False, False)
root.geometry("300x100")
root.columnconfigure(0, weight=1)


def greet():
    print(f'hello {user_name.get()}')


user_name = tk.StringVar()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 10))
input_frame.grid(row=0, column=0, sticky="EW")
input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=1)


# add text box
name_entry = ttk.Entry(input_frame, width=20, textvariable=user_name)
name_entry.grid(row=0, column=0, sticky="EW")
name_label = ttk.Label(input_frame, text="نام")
name_label.config(font=("B Zar Bold", 14))
name_label.grid(row=0, column=1, padx=(80, 0), sticky="EW")

# add buttons

buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky="EW")
buttons.columnconfigure(0, weight=1)
buttons.columnconfigure(1, weight=1)


greet_button = ttk.Button(buttons, text="خوشامد", command=greet)
greet_button.grid(row=0, column=0, sticky="EW")
quit_button = ttk.Button(buttons, text="خروج", command=root.destroy)
quit_button.grid(row=0, column=1, sticky="EW")

root.mainloop()
