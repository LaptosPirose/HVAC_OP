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

# Frames

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600+550+200")

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)

label1 = tk.Label(main, text='Panel Top', bg='red').pack(
side='top', expand=True, fill='both')
label2 = tk.Label(root, text='Panel Top', bg='red').pack(
side='top', expand=True, fill='both')
label3 = tk.Label(main, text='Panel Left', bg='green').pack(
side='left', expand=True, fill='both')

root.mainloop()

# Two frames

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# root.geometry("800x600+400+200")

root.geometry("+400+200")
root.title("Geometry")

def print_name():
print(f"Hello {user_name.get() or 'No One'}")

user_name = tk.StringVar()

label = ttk.Label(root, text="Hello, World!", justify='center')
label.pack(pady=20)

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.pack(fill=tk.BOTH, expand=True)

label1 = tk.Label(input_frame, text="Name: ")
label1.pack(side='left', padx=(20, 10), pady=(10, 10))

entry_value = ttk.Entry(input_frame, textvariable=user_name, justify='left')
entry_value.pack(side='left', padx=(10, 20), pady=(10, 10))
entry_value.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.pack(fill=tk.BOTH, expand=True)

button_print = ttk.Button(buttons, text='Print', command=print_name)
button_print.pack(side='left', padx=40, pady=20)

button_destroy = ttk.Button(buttons, text='Quit', command=root.destroy)
button_destroy.pack(side='left', padx=20, pady=20)

root.mainloop()

# With two frames

import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# root.geometry("800x600+400+200")

root.geometry("+400+200")
root.title("Greeting")
root.columnconfigure(0, weight=1)

def print_name():
print(f"Hello {user_name.get() or 'No One'}")

user_name = tk.StringVar()

label = ttk.Label(root, text="Hello, World!", justify='center')
label.grid()

input_frame = ttk.Frame(root, padding=(20, 10, 20, 0))
input_frame.grid(row=0, column=0, sticky='EW')

label1 = tk.Label(input_frame, text="Name: ")
label1.grid(row=0, column=0)

entry_value = ttk.Entry(input_frame, width=25,
textvariable=user_name, justify='left')
entry_value.grid(row=0, column=1)
entry_value.focus()

buttons = ttk.Frame(root, padding=(20, 10))
buttons.grid(row=1, column=0, sticky='EW')
buttons.columnconfigure((0,1), weight=1)

button_print = ttk.Button(buttons, text='Print', command=print_name)
button_print.grid(row=1, column=0, padx=(20, 10), sticky='EW')

button_destroy = ttk.Button(buttons, text='Quit', command=root.destroy)
button_destroy.grid(row=1, column=1, padx=(10, 20), sticky='EW')

root.mainloop()

# Study

import tkinter as tk
from tkinter import ttk
import time
import datetime

def print_message():
print(user_name.get() or 'No One!')

root = tk.Tk()

user_name = tk.StringVar()

time_now = datetime.datetime.now()
str_date = time_now.strftime('%Y/%m/%d')
str_time = time_now.strftime('%H:%m:%S')

root.geometry("1080x600+450+100")
root.title("My First APP")

print(time_now)
print(str_date)
print(str_time)

label_1 = ttk.Label(root, text="My First Label!")
label_1.grid(row=0, column=0, sticky='EW', pady=(20, 10))

entry = ttk.Entry(root, width=25, textvariable=user_name, justify='center')
entry.grid(row=0, column=1, pady=(20, 10))
entry.focus()

button_1 = ttk.Button(root, text='Print Message', command=print_message)
button_1.grid(row=1, column=0)

button_2 = ttk.Button(root, text="Quit", command=root.destroy)
button_2.grid(row=1, column=1)

root.mainloop()

# Label with images

## Changing images

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("600x480+400+200")
root.resizable(True, False)
root.title("Labels")

my_label = ttk.Label(root, text='Hello, World!', padding=20)
my_label.config(font=('Times New Roman', 30))
my_label.pack(expand=True)

# In order to insert images you eill need to install PIllow library

# image = Image.open('./images/example.jpg')

# or

# with open('./images/example.jpg', 'r') as img:

# image = Image.open(img)

photo*T* = False

def change*image():
global photo_T*
label['image'] = photo_b

    if not (photo_T_):
        photo_T_ = not photo_T_
        return None
    if photo_T_:
        label['image'] = photo_a
        photo_T_ = not photo_T_
        return None


image_a = Image.open('./images/example.jpg').resize((200, 100)) # Resize image
photo_a = ImageTk.PhotoImage(image_a)

image_b = Image.open('./images/jpg.png').resize((100, 100))
photo_b = ImageTk.PhotoImage(image_b)

label = ttk.Label(root, image=photo_a, padding=5)
label.pack(fill='both', expand=True)
label.pack()

button_change_image = ttk.Button(
root, text="Change Image", command=change_image)
button_change_image.pack()

# To change image

# label['image']=photo_b

root.mainloop()
