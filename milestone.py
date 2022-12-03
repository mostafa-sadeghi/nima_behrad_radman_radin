import tkinter as tk
from tkinter import ttk
import tkinter.font as font


def handle_calc(*args):
    m = float(mtres_val.get())
    f = m * 3.28
    feet_val.set(f'{f}')


root = tk.Tk()
font.nametofont('TkDefaultFont').configure(family="Calibra", size=16)

mtres_val = tk.StringVar()
feet_val = tk.StringVar()

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.title('Distance Converter')

main = ttk.Frame(root, padding=(30, 15))
main.grid()

metres_label = ttk.Label(main, text='Mtres: ')
metres_inpt = ttk.Entry(
    main, width=10, textvariable=mtres_val, font=("Calibra", 16))

feet_label = ttk.Label(main, text="feet:")
feet_display = ttk.Label(main, text="", textvariable=feet_val)

calc_btn = ttk.Button(main, text="calc", command=handle_calc)


metres_label.grid(column=0, row=0, sticky='w')
metres_inpt.grid(column=1, row=0, sticky='ew')
feet_label.grid(column=0, row=1, sticky='w')
feet_display.grid(column=1, row=1, sticky='ew')
calc_btn.grid(column=0, row=2, columnspan=2, sticky='ew')

for child in main.winfo_children():
    child.grid_configure(padx=15, pady=15)


metres_inpt.bind('<Return>', handle_calc)
root.mainloop()
