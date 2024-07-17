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


def calculate_feet(*args):
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
