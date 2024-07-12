# Creting a simple window

root = tk.Tk()
root.title("My GUI App")

ttk.Label(root, text='Hello World').pack()

root.mainloop()

# Teste routine

import tkinter as tk
from tkinter import ttk

tk.\_test()

# First simple window

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text='Tutorial', padding = (100, 50)).pack()

# Padding - first value is for distance right and left, second value is for distance up and down

import tkinter as tk
from tkinter import ttk

def greet():
print('Hello, World!')

root = tk.Tk()

# Buttons stacked one above the other

greet_button = ttk.Button(root, text='Greeting',
padding=(10, 10), command=greet).pack()
destroy_buton = ttk.Button(root, text='Destroy', padding=(
10, 10), command=root.destroy).pack()

# Buttons stacked one besides the other

greet_button = ttk.Button(root, text='Greeting', padding=(
10, 10), command=greet)
greet_button.pack(side='left')
destroy_buton = ttk.Button(root, text='Destroy', padding=(
10, 10), command=root.destroy)
destroy_buton.pack(side='left')

# Buttons stacked one besides the other but with fill property set to Y (Y coordinate)

# It will fill all spaces when you enlarge the screen

greet_button = ttk.Button(root, text='Greeting', padding=(
10, 10), command=greet)
greet_button.pack(side='left', fill='y')
destroy_buton = ttk.Button(root, text='Destroy', padding=(
10, 10), command=root.destroy)
destroy_buton.pack(side='left')

# Buttons stacked one besides the other but with fill property set to X (x coordinate)

# It will fill all spaces when you enlarge the screen

greet_button = ttk.Button(root, text='Greeting', padding=(
10, 10), command=greet)
greet_button.pack(side='left', fill='x', expand=True)
destroy_buton = ttk.Button(root, text='Destroy', padding=(
10, 10), command=root.destroy)
destroy_buton.pack(side='left')

# Buttons stacked one besides the other but with fill property set to both (x,y coordinate)

# It will fill all spaces when you enlarge the screen

greet_button = ttk.Button(root, text='Greeting', padding=(
10, 10), command=greet)
greet_button.pack(side='left', fill='both', expand=True)
destroy_buton = ttk.Button(root, text='Destroy', padding=(
10, 10), command=root.destroy)
destroy_buton.pack(side='left')

root.mainloop()

root.mainloop()

# Using tk.StringVar

import tkinter as tk
from tkinter import ttk

def print_label():
print(user_name.get() or "No One!")

root = tk.Tk()

user_name = tk.StringVar()

name_label = ttk.Label(root, text='Name: ')
name_label.pack(side='left', padx=(50, 10))

entry_value = ttk.Entry(root, width = 15, textvariable = user_name)
entry_value.pack(side='left', padx=(50, 10))
entry_value.focus()

button_send = ttk.Button(root, width = 15, text = 'Send Button', command = print_label).pack(side = 'left')
button_quit = ttk.Button(root, width = 15, text = 'Quit', command = root.destroy).pack(side = 'left')

root.mainloop()

# Exercising pack

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

print(root.winfo_geometry)
root.geometry("800x400+200+200")
root.title("Geometry")


rectangle_1 = tk.Label(root, text='Rectangle_1', bg='green', fg='white')
rectangle_1.pack(ipadx=10, ipady=10, fill = 'x')

rectangle_2 = tk.Label(root, text='Rectangle_2', bg='red', fg='white')
rectangle_2.pack(ipadx=10, ipady=10, side='left')

root.mainloop()