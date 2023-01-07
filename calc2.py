import tkinter as tk
from tkinter import ttk


class Calculator(tk.Frame):

    def show(self, value):
        self.entry_value += value
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

    def __init__(self, master):
        master.title("Calculator")
        master.geometry('363x380')
        master.config(bg="black")
        master.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ''

        entry = ttk.Entry(master, width=17,
                          background="#ccddff", font=('Arial', 28), textvariable=self.equation)
        entry.grid(row=0, column=0, columnspan=3)

        o_prantesis = ttk.Button(
            master, text='(', command=lambda: self.show('('))
        o_prantesis.grid(row=1, column=0, pady=3)
        c_prantesis = ttk.Button(
            master, text=')', command=lambda: self.show(')'))
        c_prantesis.grid(row=1, column=1, pady=3)
        remainder = ttk.Button(
            master, text='%', command=lambda: self.show('%'))
        remainder.grid(row=1, column=2, pady=3)

        button_7 = ttk.Button(
            master, text='7', command=lambda: self.show('7'))
        button_7.grid(row=2, column=0, pady=3)
        button_8 = ttk.Button(
            master, text='8', command=lambda: self.show('8'))
        button_8.grid(row=2, column=1, pady=3)
        button_9 = ttk.Button(
            master, text='9', command=lambda: self.show('9'))
        button_9.grid(row=2, column=2, pady=3)
        button_4 = ttk.Button(
            master, text='4', command=lambda: self.show('4'))
        button_4.grid(row=3, column=0, pady=3)
        button_5 = ttk.Button(
            master, text='5', command=lambda: self.show('5'))
        button_5.grid(row=3, column=1, pady=3)
        button_6 = ttk.Button(
            master, text='6', command=lambda: self.show('6'))
        button_6.grid(row=3, column=2, pady=3)
        button_1 = ttk.Button(
            master, text='1', command=lambda: self.show('1'))
        button_1.grid(row=3, column=0, pady=3)
        button_2 = ttk.Button(
            master, text='2', command=lambda: self.show('2'))
        button_2.grid(row=3, column=1, pady=3)
        button_3 = ttk.Button(
            master, text='3', command=lambda: self.show('3'))
        button_3.grid(row=3, column=2, pady=3)

        button_0 = ttk.Button(
            master, text='0', command=lambda: self.show('0'))
        button_0.grid(row=4, column=0, pady=3)
        button_point = ttk.Button(
            master, text='.', command=lambda: self.show('.'))
        button_point.grid(row=4, column=1, pady=3)
        button_add = ttk.Button(
            master, text='+', command=lambda: self.show('+'))
        button_add.grid(row=4, column=2, pady=3)

        button_sub = ttk.Button(
            master, text='-', command=lambda: self.show('-'))
        button_sub.grid(row=5, column=0, pady=3)
        button_div = ttk.Button(
            master, text='÷', command=lambda: self.show('/'))
        button_div.grid(row=5, column=1, pady=3)
        button_mul = ttk.Button(
            master, text='×', command=lambda: self.show('*'))
        button_mul.grid(row=5, column=2, pady=3)
        button_clear = ttk.Button(
            master, text='c')
        button_clear.grid(row=6, column=0, pady=3)
        button_eq = ttk.Button(
            master, text='=', command=self.solve)
        button_eq.grid(row=6, column=1, pady=3, columnspan=2, sticky="ew")


root = tk.Tk()
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TButton", borderwidth=4, bordercolor="silver", font=('Arial', 12),
                relief="solid", background="black", foreground="white")

print(style.layout('TButton'))
print(style.element_options("Button.border"))
calc = Calculator(root)
root.mainloop()
