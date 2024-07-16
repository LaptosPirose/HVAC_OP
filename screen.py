import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Checkbox")


root.mainloop()
