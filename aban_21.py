# section 1:
# import tkinter as tk
# from tkinter import ttk
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.geometry("400x330")
# root.resizable(False, False)
# root.title("My app")
# image = Image.open("logo.png").resize((32, 32))
# photo = ImageTk.PhotoImage(image)

# greeting = tk.StringVar()


# label = ttk.Label(root, textvariable=greeting, padding=20,
#                   image=photo, compound="right")
# label.config(font=("B Zar Bold", 14))
# label.pack()

# greeting.set("Hello mehrad!")

# root.mainloop()


########################################################

# section 2:


import tkinter as tk
from tkinter import ttk

root = tk.Tk()

text = tk.Text(root, height=8)
text.pack()

something = tk.StringVar()

label = ttk.Label(root, textvariable=something)
label.pack()

text.insert("1.0", "hello every body")
text.insert("2.2", "blalaaal")

# text["state"] = "disable"
text["state"] = "normal"

text_content = text.get("1.0", "end")
# print(text_content)

something.set(text_content)


root.mainloop()
