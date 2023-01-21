import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


class Calculator(tk.Frame):

    def show(self, value):
        self.entry_value += value
        self.equation.set(self.entry_value)

    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def __init__(self, master):
        master.title("Calculator")
        master.geometry('245x500')
        master.resizable(False, False)

        self.equation = tk.StringVar()
        self.entry_value = ''

        entry = ttk.Entry(master,  bootstyle="dark", font=8,
                          textvariable=self.equation)
        entry.grid(row=0, column=0, columnspan=3,
                   sticky="ew", ipady=8, padx=(4, 2), pady=2)

        o_prantesis = ttk.Button(
            master, text='(', command=lambda: self.show('('), bootstyle="secondary, outline", padding=(0, 15))
        o_prantesis.grid(row=1, column=0, pady=3, padx=(5, 2), sticky="ew")
        c_prantesis = ttk.Button(
            master, text=')', command=lambda: self.show(')'), bootstyle="secondary, outline", padding=(0, 15))
        c_prantesis.grid(row=1, column=1, pady=3, padx=2, sticky="ew")
        remainder = ttk.Button(
            master, text='%', command=lambda: self.show('%'), bootstyle="secondary, outline", padding=(0, 15))
        remainder.grid(row=1, column=2, pady=3, padx=2, sticky="ew")

        button_7 = ttk.Button(
            master, text='7', command=lambda: self.show('7'), bootstyle="info, outline", padding=(0, 15))
        button_7.grid(row=2, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_8 = ttk.Button(
            master, text='8', command=lambda: self.show('8'), bootstyle="info, outline", padding=(0, 15))
        button_8.grid(row=2, column=1, pady=3, padx=2, sticky="ew")
        button_9 = ttk.Button(
            master, text='9', command=lambda: self.show('9'), bootstyle="info, outline", padding=(0, 15))
        button_9.grid(row=2, column=2, pady=3, padx=2, sticky="ew")
        button_4 = ttk.Button(
            master, text='4', command=lambda: self.show('4'), bootstyle="info, outline", padding=(0, 15))
        button_4.grid(row=3, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_5 = ttk.Button(
            master, text='5', command=lambda: self.show('5'), bootstyle="info, outline", padding=(0, 15))
        button_5.grid(row=3, column=1, pady=3, padx=2, sticky="ew")
        button_6 = ttk.Button(
            master, text='6', command=lambda: self.show('6'), bootstyle="info, outline", padding=(0, 15))
        button_6.grid(row=3, column=2, pady=3, padx=2, sticky="ew")
        button_1 = ttk.Button(
            master, text='1', command=lambda: self.show('1'), bootstyle="info, outline", padding=(0, 15))
        button_1.grid(row=4, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_2 = ttk.Button(
            master, text='2', command=lambda: self.show('2'), bootstyle="info, outline", padding=(0, 15))
        button_2.grid(row=4, column=1, pady=3, padx=2, sticky="ew")
        button_3 = ttk.Button(
            master, text='3', command=lambda: self.show('3'), bootstyle="info, outline", padding=(0, 15))
        button_3.grid(row=4, column=2, pady=3, padx=2, sticky="ew")

        button_0 = ttk.Button(
            master, text='0', command=lambda: self.show('0'), bootstyle="info, outline", padding=(0, 15))
        button_0.grid(row=5, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_point = ttk.Button(
            master, text='.', command=lambda: self.show('.'), bootstyle="info, outline", padding=(0, 15))
        button_point.grid(row=5, column=1, padx=2, pady=3, sticky="ew")
        button_add = ttk.Button(
            master, text='+', command=lambda: self.show('+'), bootstyle="info, outline", padding=(0, 15))
        button_add.grid(row=5, column=2, pady=3, padx=2, sticky="ew")

        button_sub = ttk.Button(
            master, text='-', command=lambda: self.show('-'), bootstyle="secondary, outline", padding=(0, 15))
        button_sub.grid(row=6, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_div = ttk.Button(
            master, text='÷', command=lambda: self.show('/'), bootstyle="secondary, outline", padding=(0, 15))
        button_div.grid(row=6, column=1, pady=3, padx=2, sticky="ew")
        button_mul = ttk.Button(
            master, text='×', command=lambda: self.show('*'), bootstyle="secondary, outline", padding=(0, 15))
        button_mul.grid(row=6, column=2, pady=3, padx=2, sticky="ew")
        button_clear = ttk.Button(
            master, text='c', command=self.clear, bootstyle="success, outline", padding=(0, 15))
        button_clear.grid(row=7, column=0, pady=3, padx=(5, 2), sticky="ew")
        button_eq = ttk.Button(
            master, text='=', command=self.solve, bootstyle="primary", padding=(0, 15))
        button_eq.grid(row=7, column=1, pady=3, padx=2,
                       columnspan=2, sticky="ew")


root = tk.Tk()
root.iconbitmap('./images/favicon.ico')
style = ttk.Style('united')
style.configure("TButton", font=8)

calc = Calculator(root)
root.mainloop()
