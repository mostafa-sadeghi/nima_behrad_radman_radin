import tkinter as tk
from tkinter import ttk


# add frame with oop
class UserInputFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.user_input = tk.StringVar()
        label = ttk.Label(self, text="Enter your name")
        entry = ttk.Entry(self, textvariable=self.user_input)
        label.pack(side='left')
        entry.pack(side='left')
        button = ttk.Button(self, text="OK", command=self.greet)
        button.pack()

    def greet(self):
        print(f'hello {self.user_input.get()}')


class HelloWorld(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Hello world')
        # ttk.Label(self, text="Hello world").pack()
        user_input_frame = UserInputFrame(self)
        user_input_frame.pack()


root = HelloWorld()
root.mainloop()


##############################################
# add Frames

# root = tk.Tk()
# frame = ttk.Frame(root)
# frame.pack()
# label = ttk.Label(frame, text="Enter your name")
# label.pack()
# root.mainloop()


# root = tk.Tk()

# frame = UserInputFrame(root)
# frame.pack()
# root.mainloop()
