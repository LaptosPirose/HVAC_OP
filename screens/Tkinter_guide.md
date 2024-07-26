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

# Another example

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.title('ROOT _//_ Label with Image')

image_1 = Image.open('./images/example.jpg').resize((300, 150))
photo_1 = ImageTk.PhotoImage(image_1)

label = ttk.Label(root, image=photo_1)
label.pack()

root.mainloop()

# Another example

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("600x400")
root.title('ROOT _//_ Label with Image')

image_1 = Image.open('./images/example.jpg').resize((300, 150))
photo_1 = ImageTk.PhotoImage(image_1)

label = ttk.Label(root, image=photo_1)
label.pack()

root.mainloop()

# Change StringVar values and put images and texts with copound

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

def change_name():
text_name.set("Hello Angelo")

root = tk.Tk()
root.geometry("800x450+300+100")
root.title("PLC Monitor")

image = Image.open('./images/example.jpg')
photo = ImageTk.PhotoImage(image)

label = ttk.Label(root, padding=10, image=photo,
text="Label Text", compound='bottom').pack()
text_name = tk.StringVar()

text_name.set("Hello World!")

label_name = ttk.Label(root, textvariable=text_name,
font=("Arial", 20), wraplength=200).pack()

button = ttk.Button(root, text='change name', command=change_name).pack()

root.mainloop()

# Rapid lambda function

def valor(x, y): return x + y
print(valor(5, 3))

# Tekinter Text

# Text insert

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()

window_width = 1200
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)

window_pos_x = int((screen_width/2) - (window_width/2))
window_pos_y = int((screen_height/2) - (window_height/2))

root.geometry(str(window_width)+'x'+str(window_height) +
'+'+str(window_pos_x)+'+'+str(window_pos_y))
root.resizable(False, False)

root.title('Text Insert')

text = tk.Text(root, height=8)
text.pack(pady=(20, 0))
text.focus()

# Line 1 char zero (1.0) and firt comment inside

text.insert("1.0", "Enter the thext here...")
text['state'] = 'normal' # disable- status to be able put a text or not

# get the text content from line 1 char 5 till the end

text_content = text.get("1.5", "end")
print(text_content)

root.mainloop()

# Text with scrollbar

# Text insert

import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

root = tk.Tk()

window_width = 1200
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)

window_pos_x = int((screen_width/2) - (window_width/2))
window_pos_y = int((screen_height/2) - (window_height/2))

root.geometry(str(window_width)+'x'+str(window_height) +
'+'+str(window_pos_x)+'+'+str(window_pos_y))
root.resizable(False, False)

root.title('Text Insert')

text = tk.Text(root, height=8)
text.grid(row=0, column=0, pady=(20, 0), padx=(20, 0), sticky='EW')
text.focus()

# Line 1 char zero (1.0) and firt comment inside

text.insert("1.0", "Enter the thext here...")
text['state'] = 'normal' # disable- status to be able put a text or not

# get the text content from line 1 char 5 till the end

text_content = text.get("1.0", "end")
print(text_content)

text_scroll = tk.Scrollbar(root, orient='vertical', command=text.yview)
text_scroll.grid(row=0, column=1, pady=(20, 0), padx=(0, 20), sticky='ns')
text["yscrollcommand"] = text_scroll.set

root.mainloop()

# Horizontal separators

import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x450+200+100")
ttk.Label(root, text="Hello, world!").pack()

ttk.Separator(root, orient='horizontal').pack(fill='x')

ttk.Label(root, text="Hello, world!").pack()
root.mainloop()

#Check Buttons

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Checkbox")

checkbutton = ttk.Checkbutton(root, text="Check me")
checkbutton.pack()
checkbutton['state'] = 'disabled' # Or normal if you want to turn able or not

root.mainloop()

# Checkbutton associated with variable

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Checkbox")

selected_option = tk.StringVar()

def print_current_option():
print(selected_option.get())

checkbutton = ttk.Checkbutton(
root,
text="Check me",
variable=selected_option,
onvalue='On',
offvalue='Off',
command=print_current_option
)

checkbutton.pack()

# Normal or disabled if you want to turn able or not

checkbutton['state'] = 'normal'

root.mainloop()

# Radio Button

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Radio Button")

option_selected = tk.StringVar()

option1 = ttk.Radiobutton(
root,
text="Option 1",
variable=option_selected,
value="Option 1"
)

option2 = ttk.Radiobutton(
root,
text="Option 2",
variable=option_selected,
value="Option 2"
)

option3 = ttk.Radiobutton(
root,
text="Option 3",
variable=option_selected,
value="Option 3"
)

option1.grid(row=0, column=0)
option2.grid(row=0, column=1)
option3.grid(row=0, column=2)

ttk.Label(
root,
textvariable=option_selected,
font=("Arial", 16),
anchor=tk.W
).grid(row=1, columnspan=1)

root.mainloop()

# Combo box

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Combo Box")

selected_weekday = tk.StringVar()
selected_weekday_1 = tk.StringVar()

weekday = ttk.Combobox(
root,
textvariable=selected_weekday,
values=["Segunda", "Terça", "Quarta",
"Quinta", "Sexta", "Sábado", "Domingo"], # Impede que o usuário digite um valor qualquer - se puder digitar, selecione 'normal'
state='readonly'
)
weekday.grid(column=0, row=0, pady=(10, 0), padx=(10, 10))

# Os parâmetros de uma widget podem ser passados dentro do widget ou separados

weekday_1 = ttk.Combobox(
root,
textvariable=selected_weekday_1,
)
weekday_1['values'] = ("Segunda", "Terça", "Quarta",
"Sexta", "Sábado", "Domingo")
weekday_1['state'] = 'readonly'
weekday_1.grid(column=0, row=1, pady=(10, 0), padx=(10, 10))

# Force valores do combobox

def handle_slection(event):
print(f'Today is {selected_weekday.get()}.')
print(f'O primeiro valor clicado foi de {weekday.current()}.')
print(f'But we\'re gonna change it to Sexta')
selected_weekday.set('Sexta')
print(f'Agora hoje é {weekday.get()}.')
print(f'O valor atual clicado é de {weekday.current()}')

weekday.bind("<<ComboboxSelected>>", handle_slection)
root.mainloop()

# List Box

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("List Box")

programming_languages = ("C", "C++", "Java", "JavaScript", "R", "Python")

langs = tk.StringVar(value=programming_languages)

list_box = tk.Listbox(
root,
listvariable=langs,
selectmode=tk.MULTIPLE,
height=6,
width=20
)
list_box.pack()
list_box = tk.Listbox(
root,
listvariable=langs,
height=6,
width=20
)
list_box["selectmode"] = tk.BROWSE
list_box.pack()

# No curso é falado sobre os valors para select mode como 'extended' e 'browse',

# mas não funcionou. Apenas usando tk.MULTIPLE para multiplos elementos e tk.BROWSE para único

def handle_selection_change(event):
selected_indices = list_box.curselection()
for i in selected_indices:
print(list_box.get(i))

list_box.bind("<<ListboxSelect>>", handle_selection_change)

root.mainloop()

# Spin Boxes

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Spin Boxes")

initial_value = tk.IntVar(value=20)

spin*box = tk.Spinbox(
root,
from*=0,
to=100,
width=5,
textvariable=initial_value,
wrap=False,
command=lambda: print("Spinbox value:", initial_value.get())
).pack()

spin*box = ttk.Spinbox(
root,
from*=0,
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

# Cálculo centralizar janela na tela

window_width = 1200
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(screen_width)
print(screen_height)

window_pos_x = int((screen_width/2) - (window_width/2))
window_pos_y = int((screen_height/2) - (window_height/2))

root.geometry(str(window_width)+'x'+str(window_height) +
'+'+str(window_pos_x)+'+'+str(window_pos_y))
root.resizable(False, False)

# Scales

import tkinter as tk
from tkinter import ttk

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("800x450+400+200")
root.title("Scale")

scale = ttk.Scale(
root,
orient='horizontal',
from\_=0,
to=100,
state='normal', #disabled
command=lambda x: print("Scale value with lambda function:", x)
).pack(fill='x', padx=(20,20), pady=(20,20))

def handle_scale_change(event):
print(f'Scale value with regular function: {current_value.get()}')

current*value = tk.DoubleVar()  
scale = ttk.Scale(
root,
orient='horizontal',
from*=0,
to=100,
state='normal', #disabled
variable=current_value,
command=handle_scale_change
).pack(fill='x', padx=(20,20), pady=(20,20))
root.mainloop()

# Application Distance Converter

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()

window_width = 800
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_pos_x = int((screen_width/2) - (window_width/2))
window_pos_y = int((screen_height/2) - (window_height/2))

root.geometry(str(window_width)+'x'+str(window_height) +
'+'+str(window_pos_x)+'+'+str(window_pos_y))

root.resizable(True, True)
root.columnconfigure(0, weight=1)

root.title("Distance Converter")

font.nametofont("TkDefaultFont").configure(size=10)

meters_value = tk.StringVar()
feet_value = tk.StringVar()

def calculate*feet(\_args):
try:
pass
meters = float(meters_value.get())
feet = meters * 3.28084
print(f'{meters} meters is equal to {feet:.3f} feet.')
feet_value.set(f'{feet:.3f}')
feet_display.config(text=f'{feet_value.get()}')
except ValueError:
feet_display.config(text='Invalid input')
return

main = ttk.Frame(
root,
padding=(30, 15)
)
main.grid()

meter_label = ttk.Label(master=main, text='Meters:')
meter_input = ttk.Entry(master=main, width=10,
textvariable=meters_value)
meter_input.config(font=('Segoe UI', 10))

feet_label = ttk.Label(master=main, text='Feet:')
feet_display = ttk.Label(master=main, text='Feet from here')
calc_button = ttk.Button(master=main, text='Calculate', command=calculate_feet)

meter_label.grid(row=0, column=0, sticky='W')
meter_input.grid(row=0, column=1, sticky='EW')
meter_input.focus()

feet_label.grid(row=1, column=0, sticky='W')
feet_display.grid(row=1, column=1, sticky='EW')

calc_button.grid(row=2, column=0, columnspan=2, sticky='EW')

root.bind('<Return>', calculate_feet)
root.bind('<KP_Enter>', calculate_feet)

for child in main.winfo_children():
child.grid_configure(padx=10, pady=10)

root.mainloop()

# Object Oriented Programming

## root class

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.__window_width = 800
        self.__window_height = 400
        self.title("Tkinter Object Oriented Programming")

        self.__screen_width = self.winfo_screenwidth()
        self.__screen_height = self.winfo_screenheight()

        self.__window_pos_x = int((self.__screen_width/2) - (self.__window_width/2))
        self.__window_pos_y = int((self.__screen_height/2) - (self.__window_height/2))

        self.geometry(str(self.__window_width)+'x'+str(self.__window_height) +
                    '+'+str(self.__window_pos_x)+'+'+str(self.__window_pos_y))

        self.resizable(True, True)
        self.columnconfigure(0, weight=1)

        ttk.Label(master=self, text="Object Oriented Programming Test!").pack()

root = HelloWorld()
root.mainloop()

## frame class

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

class UserInputFrame(ttk.Frame):
def **init**(self, container):
super().**init**(container)

        self.user_input = tk.StringVar()

        self.label = ttk.Label(
            master=self,
            text="Enter your name:"
        )
        self.label.pack(side='left')

        self.entry = ttk.Entry(
            master=self,
            textvariable=self.user_input
        )
        self.entry.focus()
        self.entry.pack(side='left')

        self.button = ttk.Button(
            master=self,
            text='Greet',
            command=self.greet
        )
        self.button.pack(side='left')

        for self.i in self.winfo_children():
            self.i.pack_configure(padx=10, pady=10)

    def greet(self):
        print(f"Hello, {self.user_input.get() or 'No One'}.")

root = tk.Tk()
root.geometry("800x450+250+200")
root.title('OO Frame')
frame = UserInputFrame(container=root).pack()
root.mainloop()

## both frames and classes

import tkinter as tk
from tkinter import ttk
import tkinter.font as font

from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

class HelloWorld(tk.Tk):

    def __init__(self):
        super().__init__()

        self.title("Hello World _ Frame and Root OO")
        self.geometry("800x450+250+200")

        self.__frame = UserInputFrame(self)
        self.__frame.pack()

class UserInputFrame(ttk.Frame):

def **init**(self, container):
super().**init**(container)

        self.user_input = tk.StringVar()

        self.label = ttk.Label(
            master=self,
            text="Enter your name:"
        )
        self.label.pack(side='left')

        self.entry = ttk.Entry(
            master=self,
            textvariable=self.user_input
        )
        self.entry.focus()
        self.entry.pack(side='left')

        self.button = ttk.Button(
            master=self,
            text='Greet',
            command=self.greet
        )
        self.button.pack(side='left')

        for self.i in self.winfo_children():
            self.i.pack_configure(padx=10, pady=10)

    def greet(self):
        print(f"Hello, {self.user_input.get() or 'No One'}.")

root = HelloWorld()

root.mainloop()

# Distance converter Object Oriented\_\_

# Define the project absolut path

import set_path as set_path
from windows import set_dpi_awareness
from siemens_lib import s7_get_inputs
import tkinter.font as font
from tkinter import ttk
import tkinter as tk

# Include avoid dpi problemns solving - Only in Windows 10

set_dpi_awareness.set_dpi_awareness()

class DistanceConverter(tk.Tk):

    def __init__(self, width, height, x_pos, y_pos, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Distance Converter')

        self.width = str(width)
        self.height = str(height)
        self.x_pos = str(x_pos)
        self.y_pos = str(y_pos)

        self.geometry(self.width+'x'+self.height+'+'+self.x_pos+'+'+self.y_pos)

        self.frame = AppFrame(self)
        self.frame.grid()

        self.bind('<Return>', self.frame.calculate_feet)
        self.bind('<KP_Enter>', self.frame.calculate_feet)

class AppFrame(ttk.Frame):

    def __init__(self, container, **kwargs):
        super().__init__(container, **kwargs)
        self['padding'] = (30, 30)

        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        self.meter_label = ttk.Label(master=self, text='Meters:')
        self.meter_input = ttk.Entry(master=self, width=10,
                                     textvariable=self.meters_value)
        self.meter_input.config(font=('Segoe UI', 10))

        self.feet_label = ttk.Label(master=self, text='Feet:')
        self.feet_display = ttk.Label(master=self, text='Feet from here')
        self.calc_button = ttk.Button(
            master=self, text='Calculate', command=self.calculate_feet)

        self.meter_label.grid(row=0, column=0, sticky='W')
        self.meter_input.grid(row=0, column=1, sticky='EW')
        self.meter_input.focus()

        self.feet_label.grid(row=1, column=0, sticky='W')
        self.feet_display.grid(row=1, column=1, sticky='EW')

        self.calc_button.grid(row=2, column=0, columnspan=2, sticky='EW')

        for self.child in self.winfo_children():
            self.child.grid_configure(padx=5, pady=5)

    def calculate_feet(self, *args):

        try:
            self.meters = float(self.meters_value.get())
            self.feet = self.meters * 3.28084
            print(f'{self.meters} meters is equal to {self.feet:.3f} feet.')
            self.feet_value.set(f'{self.feet:.3f}')
            self.feet_display.config(text=f'{self.feet_value.get()}')
        except ValueError:
            self.feet_display.config(text='Invalid input')
        return

root = DistanceConverter(width=600, height=350, x_pos=550, y_pos=200)
font.nametofont("TkDefaultFont").configure(size=10)
root.columnconfigure(index=0, weight=1)
root.mainloop()

# Switching frames

# Define the project absolut path

import set_path as set_path
from windows import set_dpi_awareness
from siemens_lib import s7_get_inputs
import tkinter.font as font
from tkinter import ttk
import tkinter as tk

# Include avoid dpi problemns solving - Only in Windows 10

set_dpi_awareness.set_dpi_awareness()

class DistanceConverter(tk.Tk):
"""
Main window for the distance converter app.

    Args:
        tk (_type_): tkinter min window
    """

    def __init__(
        self,
        width,
        height,
        x_pos,
        y_pos,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.title('Distance Converter')

        self.width = str(width)
        self.height = str(height)
        self.x_pos = str(x_pos)
        self.y_pos = str(y_pos)

        self.geometry(self.width+'x'+self.height+'+'+self.x_pos+'+'+self.y_pos)

        self.frames = dict()

        self.container = ttk.Frame(
            self
        )
        self.container.grid(
            padx=10,
            pady=5,
            sticky='NSEW'
        )

        self.frame_feets_to_meters = FeetsToMeter(
            self.container,
            self
        )

        self.frame_feets_to_meters.grid(
            row=0,
            column=0,
            sticky='NSEW'
        )

        self.frame_meters_to_feets = MetersToFeet(
            self.container,
            self
        )

        self.frame_meters_to_feets.grid(
            row=0,
            column=0,
            sticky='NSEW'
        )

        self.frames[FeetsToMeter] = self.frame_feets_to_meters
        self.frames[MetersToFeet] = self.frame_meters_to_feets

        self.switch_frame(MetersToFeet)

        self.bind('<Return>', self.frame_feets_to_meters.calculate)
        self.bind('<KP_Enter>', self.frame_feets_to_meters.calculate)
        self.bind('<Return>', self.frame_meters_to_feets.calculate)
        self.bind('<KP_Enter>', self.frame_meters_to_feets.calculate)

    def switch_frame(
        self,
        frame_class
    ):
        self.frame_class = frame_class
        self.frame = self.frames[self.frame_class]
        self.frame.tkraise()

class MetersToFeet(ttk.Frame):

    def __init__(
        self,
        container,
        controller,
        **kwargs
    ):
        super().__init__(container, **kwargs)
        self['padding'] = (30, 30)

        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        self.meter_label = ttk.Label(
            master=self,
            text='Meters:'
        )

        self.meter_input = ttk.Entry(
            master=self,
            width=10,
            textvariable=self.meters_value
        )
        self.meter_input.config(font=('Segoe UI', 10))

        self.feet_label = ttk.Label(
            master=self,
            text='Feet:'
        )

        self.feet_display = ttk.Label(
            master=self,
            text='Feet from here'
        )

        self.calc_button = ttk.Button(
            master=self,
            text='Calculate',
            command=self.calculate
        )

        self.switch_button = ttk.Button(
            master=self,
            text='Switch to feets',
            command=lambda: controller.switch_frame(FeetsToMeter)
        )

        self.meter_label.grid(
            row=0,
            column=0,
            sticky='W'
        )
        self.meter_input.grid(
            row=0,
            column=1,
            sticky='EW'
        )
        self.meter_input.focus()

        self.feet_label.grid(
            row=1,
            column=0,
            sticky='W'
        )

        self.feet_display.grid(
            row=1,
            column=1,
            sticky='EW'
        )

        self.calc_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='EW'
        )
        self.switch_button.grid(row=3, column=0, columnspan=2, sticky='EW')

        for self.child in self.winfo_children():
            self.child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            self.meters = float(self.meters_value.get())
            self.feet = self.meters * 3.28084
            print(f'{self.meters} meters is equal to {self.feet:.3f} feet.')
            self.feet_value.set(f'{self.feet:.3f}')
            self.feet_display.config(text=f'{self.feet_value.get()}')
        except ValueError:
            self.feet_display.config(text='Invalid input')
        return

class FeetsToMeter(ttk.Frame):

    def __init__(
            self,
            container,
            controller,
            **kwargs
    ):
        super().__init__(container, **kwargs)
        self['padding'] = (30, 30)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        self.feet_label = ttk.Label(
            master=self,
            text='Feets:'
        )

        self.feet_input = ttk.Entry(
            master=self,
            width=10,
            textvariable=self.feet_value
        )

        self.feet_input.config(font=('Segoe UI', 10))

        self.meters_label = ttk.Label(
            master=self,
            text='Meters:'
        )

        self.meters_display = ttk.Label(
            master=self,
            text='Meters from here'
        )

        self.calc_button = ttk.Button(
            master=self,
            text='Calculate',
            command=self.calculate
        )

        self.switch_button = ttk.Button(
            master=self,
            text='Switch to meters',
            command=lambda: controller.switch_frame(MetersToFeet)
        )

        self.feet_label.grid(
            row=0,
            column=0,
            sticky='W'
        )

        self.feet_input.grid(
            row=0,
            column=1,
            sticky='EW'
        )

        self.feet_input.focus()

        self.meters_label.grid(
            row=1,
            column=0,
            sticky='W'
        )

        self.meters_display.grid(
            row=1,
            column=1,
            sticky='EW'
        )

        self.calc_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='EW'
        )

        self.switch_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky='EW'
        )

        for self.child in self.winfo_children():
            self.child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):

        try:
            self.feet = float(self.feet_value.get())
            self.meters = self.feet / 3.28084
            print(f'{self.feet} feet is equal to {self.meters:.3f} meters.')
            self.meters_value.set(f'{self.meters:.3f}')
            self.meters_display.config(text=f'{self.meters_value.get()}')
        except ValueError:
            self.meters_display.config(text='Invalid input')
        return

root = DistanceConverter(
width=600,
height=350,
x_pos=550,
y_pos=200
)
font.nametofont(
"TkDefaultFont"
).configure(
size=10
)

root.columnconfigure(
index=0,
weight=1
)

root.mainloop()

# Last BackUp

# Define the project absolut path

import set_path as set_path
from windows import set_dpi_awareness
from siemens_lib import s7_get_inputs
import tkinter.font as font
from tkinter import ttk
import tkinter as tk

# Include avoid dpi problemns solving - Only in Windows 10

set_dpi_awareness.set_dpi_awareness()

class DistanceConverter(tk.Tk):
"""
Main window for the distance converter app.

    Args:
        tk (_type_): tkinter min window
    """

    def __init__(
        self,
        width,
        height,
        x_pos,
        y_pos,
        *args,
        **kwargs
    ):
        super().__init__(*args, **kwargs)

        self.title('Distance Converter')

        self.width = str(width)
        self.height = str(height)
        self.x_pos = str(x_pos)
        self.y_pos = str(y_pos)

        self.geometry(self.width+'x'+self.height+'+'+self.x_pos+'+'+self.y_pos)

        self.frames = dict()

        self.container = ttk.Frame(
            self
        )
        self.container.grid(
            padx=10,
            pady=5,
            sticky='NSEW'
        )

        self.frame_feets_to_meters = FeetsToMeters(
            self.container,
            self
        )

        self.frame_feets_to_meters.grid(
            row=0,
            column=0,
            sticky='NSEW'
        )

        self.frame_meters_to_feets = MetersToFeets(
            self.container,
            self
        )

        self.frame_meters_to_feets.grid(
            row=0,
            column=0,
            sticky='NSEW'
        )

        self.frames[FeetsToMeters] = self.frame_feets_to_meters
        self.frames[MetersToFeets] = self.frame_meters_to_feets

        actual_frame = self.switch_frame(MetersToFeets)

        print(
            actual_frame
        )

        self.bind('<Return>', self.frame_feets_to_meters.calculate)
        self.bind('<KP_Enter>', self.frame_feets_to_meters.calculate)
        self.bind('<Return>', self.frame_meters_to_feets.calculate)
        self.bind('<KP_Enter>', self.frame_meters_to_feets.calculate)

    def switch_frame(
        self,
        frame_class
    ):
        self.frame_class = frame_class
        self.frame = self.frames[self.frame_class]
        self.frame.tkraise()
        return frame_class

class MetersToFeets(ttk.Frame):

    def __init__(
        self,
        container,
        controller,
        **kwargs
    ):
        super().__init__(container, **kwargs)
        self['padding'] = (30, 30)

        self.meters_value = tk.StringVar()
        self.feet_value = tk.StringVar()

        self.meter_label = ttk.Label(
            master=self,
            text='Meters:'
        )

        self.meter_input = ttk.Entry(
            master=self,
            width=10,
            textvariable=self.meters_value
        )
        self.meter_input.config(font=('Segoe UI', 10))

        self.feet_label = ttk.Label(
            master=self,
            text='Feet:'
        )

        self.feet_display = ttk.Label(
            master=self,
            text='Feet from here'
        )

        self.calc_button = ttk.Button(
            master=self,
            text='Calculate',
            command=self.calculate
        )

        self.switch_button = ttk.Button(
            master=self,
            text='Switch to feets',
            command=lambda: controller.switch_frame(FeetsToMeters)
        )

        self.meter_label.grid(
            row=0,
            column=0,
            sticky='W'
        )
        self.meter_input.grid(
            row=0,
            column=1,
            sticky='EW'
        )
        self.meter_input.focus()

        self.feet_label.grid(
            row=1,
            column=0,
            sticky='W'
        )

        self.feet_display.grid(
            row=1,
            column=1,
            sticky='EW'
        )

        self.calc_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='EW'
        )
        self.switch_button.grid(row=3, column=0, columnspan=2, sticky='EW')

        for self.child in self.winfo_children():
            self.child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            self.meters = float(self.meters_value.get())
            self.feet = self.meters * 3.28084
            print(f'{self.meters} meters is equal to {self.feet:.3f} feet.')
            self.feet_value.set(f'{self.feet:.3f}')
            self.feet_display.config(text=f'{self.feet_value.get()}')
        except ValueError:
            self.feet_display.config(text='Invalid input')
        return

class FeetsToMeters(ttk.Frame):

    def __init__(
            self,
            container,
            controller,
            **kwargs
    ):
        super().__init__(container, **kwargs)
        self['padding'] = (30, 30)

        self.feet_value = tk.StringVar()
        self.meters_value = tk.StringVar()

        self.feet_label = ttk.Label(
            master=self,
            text='Feets:'
        )

        self.feet_input = ttk.Entry(
            master=self,
            width=10,
            textvariable=self.feet_value
        )

        self.feet_input.config(font=('Segoe UI', 10))

        self.meters_label = ttk.Label(
            master=self,
            text='Meters:'
        )

        self.meters_display = ttk.Label(
            master=self,
            text='Meters from here'
        )

        self.calc_button = ttk.Button(
            master=self,
            text='Calculate',
            command=self.calculate
        )

        self.switch_button = ttk.Button(
            master=self,
            text='Switch to meters',
            command=lambda: controller.switch_frame(MetersToFeets)
        )

        self.feet_label.grid(
            row=0,
            column=0,
            sticky='W'
        )

        self.feet_input.grid(
            row=0,
            column=1,
            sticky='EW'
        )

        self.feet_input.focus()

        self.meters_label.grid(
            row=1,
            column=0,
            sticky='W'
        )

        self.meters_display.grid(
            row=1,
            column=1,
            sticky='EW'
        )

        self.calc_button.grid(
            row=2,
            column=0,
            columnspan=2,
            sticky='EW'
        )

        self.switch_button.grid(
            row=3,
            column=0,
            columnspan=2,
            sticky='EW'
        )

        for self.child in self.winfo_children():
            self.child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):

        try:
            self.feet = float(self.feet_value.get())
            self.meters = self.feet / 3.28084
            print(f'{self.feet} feet is equal to {self.meters:.3f} meters.')
            self.meters_value.set(f'{self.meters:.3f}')
            self.meters_display.config(text=f'{self.meters_value.get()}')
        except ValueError:
            self.meters_display.config(text='Invalid input')
        return

root = DistanceConverter(
width=600,
height=350,
x_pos=550,
y_pos=200
)
font.nametofont(
"TkDefaultFont"
).configure(
size=10
)

root.columnconfigure(
index=0,
weight=1
)

root.mainloop()
