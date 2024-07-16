import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("List Box")


initial_value = tk.IntVar(value=20)

spin_box = tk.Spinbox(
    root,
    from_=0,
    to=100,
    width=5,
    textvariable=initial_value,
    wrap=False,
    command=lambda: print("Spinbox value:", initial_value.get())
).pack()

spin_box = ttk.Spinbox(
    root,
    from_=0,
    to=100,
    width=5,
    textvariable=initial_value,
    wrap=True,
    command=lambda: print("Spinbox value:", initial_value.get())
).pack()

spin_box = ttk.Spinbox(
    root,
    values=(0, 10, 20, 30, 40, 50, 60),
    width=5,
    textvariable=initial_value,
    wrap=True,
    command=lambda: print("Spinbox value:", initial_value.get())
).pack()


root.mainloop()
