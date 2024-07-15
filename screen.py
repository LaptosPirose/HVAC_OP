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
