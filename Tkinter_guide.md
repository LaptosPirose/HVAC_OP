# Creting a simple window

root = tk.Tk()
root.title("My GUI App")

ttk.Label(root, text='Hello World').pack()

root.mainloop()

# Teste routine

import tkinter as tk
from tkinter import ttk

tk._test()

# First simple window
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text='Tutorial', padding = (100, 50)).pack()
# Padding - first value is for distance right and left, second value is for distance up and down

root.mainloop()
