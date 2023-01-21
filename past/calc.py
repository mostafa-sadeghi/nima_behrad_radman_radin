import tkinter as tk
from tkinter import ttk, END


def button_click(number):
    # e.insert(END, number)
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))


def buttonClear():
    e.delete(0, END)


def buttonAdd():
    first_number = e.get()
    global f_num
    global math
    math = "add"
    f_num = int(float(first_number))
    e.delete(0, END)


def buttonEqual():
    second_number = e.get()
    snum = int(float(second_number))
    e.delete(0, END)
    if math == "add":
        e.insert(0, f_num + snum)
    elif math == "sub":
        e.insert(0, f_num - snum)
    elif math == "mul":
        e.insert(0, f_num * snum)
    elif math == "div":
        e.insert(0, f_num / snum)


def buttonSubtract():
    first_number = e.get()
    global f_num
    global math
    math = "sub"
    f_num = int(float(first_number))
    e.delete(0, END)


def buttonMul():
    first_number = e.get()
    global f_num
    global math
    math = "mul"
    f_num = int(float(first_number))
    e.delete(0, END)


def buttonDiv():
    first_number = e.get()
    global f_num
    global math
    math = "div"
    f_num = int(first_number)
    e.delete(0, END)


root = tk.Tk()
root.title('calculator')
e = tk.Entry(root, width=15, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=30, pady=15, sticky="ew")

button_7 = ttk.Button(root, text="7", command=lambda: button_click(7))
button_7.grid(row=1, column=0)
button_8 = ttk.Button(root, text="8", command=lambda: button_click(8))
button_8.grid(row=1, column=1)
button_9 = ttk.Button(root, text="9", command=lambda: button_click(9))
button_9.grid(row=1, column=2)

button_4 = ttk.Button(root, text="4", command=lambda: button_click(4))
button_4.grid(row=2, column=0)
button_5 = ttk.Button(root, text="5", command=lambda: button_click(5))
button_5.grid(row=2, column=1)
button_6 = ttk.Button(root, text="6", command=lambda: button_click(6))
button_6.grid(row=2, column=2)

button_1 = ttk.Button(root, text="1", command=lambda: button_click(1))
button_1.grid(row=3, column=0)
button_2 = ttk.Button(root, text="2", command=lambda: button_click(2))
button_2.grid(row=3, column=1)
button_3 = ttk.Button(root, text="3", command=lambda: button_click(3))
button_3.grid(row=3, column=2)
button_0 = ttk.Button(root, text="0", command=lambda: button_click(0))
button_0.grid(row=4, column=0)

button_clear = ttk.Button(root, text="clear", command=buttonClear)
button_clear.grid(row=4, column=1, columnspan=2, sticky="ew")
button_add = ttk.Button(root, text="+", command=buttonAdd)
button_add.grid(row=5, column=0)
button_equal = ttk.Button(root, text="=", command=buttonEqual)
button_equal.grid(row=5, column=1, columnspan=2, sticky="ew")

button_subtract = ttk.Button(root, text="-", command=buttonSubtract)
button_subtract.grid(row=6, column=0)
button_mul = ttk.Button(root, text="*", command=buttonMul)
button_mul.grid(row=6, column=1)
button_div = ttk.Button(root, text="/", command=buttonDiv)
button_div.grid(row=6, column=2)

root.mainloop()
