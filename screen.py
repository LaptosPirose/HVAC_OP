import tkinter as tk
from tkinter import ttk

def greet():
    print('Hello, World!')
    
root = tk.Tk()
ttk.Label(root, text='Tutorial', padding = (100, 50)).pack()
# Padding - first value is for distance right and left, second value is for distance up and down

greet_button = ttk.Button(root, text = 'Greeting', padding = (10,10 ), command = greet).pack()

root.mainloop()