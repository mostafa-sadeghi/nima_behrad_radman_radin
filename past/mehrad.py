
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

# root = tk.Tk()
# root.geometry("600x400")


# def greet():
#     print(f'hello {user_name.get()}')


# user_name = tk.StringVar()
# name_label = ttk.Label(root, text="Name:")
# name_label.pack(side="top", padx=(0, 10))
# # add text box
# name_entry = ttk.Entry(root, width=20, textvariable=user_name)
# name_entry.pack(side="top")

# # add buttons
# greet_button = ttk.Button(root, text="خوشامد", command=greet)
# greet_button.pack(side="top")
# quit_button = ttk.Button(root, text="خروج", command=root.destroy)
# quit_button.pack(side="top")

# root.mainloop()


# root = tk.Tk()
# root.geometry("600x400")

# rect_1 = tk.Label(root, text="number one", bg="green", fg="white")
# rect_1.pack(side="left", fill="both", expand=True)

# rect_2 = tk.Label(root, text="number two", bg="red", fg="white")
# rect_2.pack(fill="both", expand=True)

# rect_3 = tk.Label(root, text="number three", bg="blue", fg="white")
# rect_3.pack(side="left", fill="both", expand=True)


# root.mainloop()


root = tk.Tk()

main = ttk.Frame(root)
main.pack(side="left", fill="both", expand=True)

tk.Label(main, text="First label", bg="red").pack(
    side="top", fill="both", expand=True)
tk.Label(main, text="Second label", bg="green").pack(
    side="top", fill="both", expand=True)

main2 = ttk.Frame(root)
main2.pack(side="left", fill="both", expand=True)

tk.Label(main2, text="First label", bg="yellow").pack(
    side="top", fill="both", expand=True)
tk.Label(main2, text="Second label", bg="brown").pack(
    side="top", fill="both", expand=True)

root.mainloop()
