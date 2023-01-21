import tkinter as tk
from tkinter import ttk
import tkinter.font as font


class MetresToFeet(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.mtres_val = tk.StringVar()
        self.feet_val = tk.StringVar()

        metres_label = ttk.Label(self, text='Mtres: ')
        metres_inpt = ttk.Entry(
            self, width=10, textvariable=self.mtres_val, font=("Calibra", 16))

        feet_label = ttk.Label(self, text="feet:")
        feet_display = ttk.Label(self, text="", textvariable=self.feet_val)

        calc_btn = ttk.Button(self, text="calc", command=self.handle_calc)
        switch_page_button = ttk.Button(
            self, text="switch to feet to metres", command=lambda: controller.show_frame(FeetToMetres))

        metres_label.grid(column=0, row=0, sticky='w')
        metres_inpt.grid(column=1, row=0, sticky='ew')
        feet_label.grid(column=0, row=1, sticky='w')
        feet_display.grid(column=1, row=1, sticky='ew')
        calc_btn.grid(column=0, row=2, columnspan=2, sticky='ew')
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

        metres_inpt.bind('<Return>', self.handle_calc)

    def handle_calc(self, *args):
        m = float(self.mtres_val.get())
        f = m * 3.28
        self.feet_val.set(f'{f}')


class FeetToMetres(ttk.Frame):
    def __init__(self, container, controller, **kwargs):
        super().__init__(container, **kwargs)
        self.mtres_val = tk.StringVar()
        self.feet_val = tk.StringVar()

        feet_label = ttk.Label(self, text='feet: ')
        feet_inpt = ttk.Entry(
            self, width=10, textvariable=self.feet_val, font=("Calibra", 16))

        metres_label = ttk.Label(self, text="metres:")
        metres_display = ttk.Label(self, text="", textvariable=self.mtres_val)

        calc_btn = ttk.Button(self, text="calc", command=self.handle_calc)
        switch_page_button = ttk.Button(
            self, text='switch to meters to feet', command=lambda: controller.show_frame(MetresToFeet))

        feet_label.grid(column=0, row=0, sticky='w')
        feet_inpt.grid(column=1, row=0, sticky='ew')
        metres_label.grid(column=0, row=1, sticky='w')
        metres_display.grid(column=1, row=1, sticky='ew')
        calc_btn.grid(column=0, row=2, columnspan=2, sticky='ew')
        switch_page_button.grid(column=0, row=3, columnspan=2, sticky='ew')

        for child in self.winfo_children():
            child.grid_configure(padx=15, pady=15)

        feet_inpt.bind('<Return>', self.handle_calc)

    def handle_calc(self, *args):
        m = float(self.feet_val.get())
        f = m / 3.28
        self.mtres_val.set(f'{f}')


class DistanceConvertor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Distance Convertor')
        self.frames = dict()
        container = ttk.Frame(self)
        container.grid(padx=60, pady=30)

        feet_to_metres = FeetToMetres(container, self, padding=(60, 30))
        feet_to_metres.grid(row=0, column=0)
        meters_to_feet = MetresToFeet(container, self, padding=(60, 30))
        meters_to_feet.grid(row=0, column=0)

        self.frames[FeetToMetres] = feet_to_metres
        self.frames[MetresToFeet] = meters_to_feet

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


root = DistanceConvertor()
font.nametofont('TkDefaultFont').configure(family="Calibra", size=16)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


root.mainloop()
