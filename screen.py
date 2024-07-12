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
