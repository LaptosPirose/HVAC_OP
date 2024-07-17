import tkinter as tk
from tkinter import ttk

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

meters_value = tk.StringVar()


def calculate_feet(*args):
    try:
        pass
        meters = float(meters_value.get())
        feet = meters * 3.28084
        print(f'{meters} meters is equal to {feet:.3f} feet.')
    except ValueError:
        feet_display.config(text='Invalid input')
        return


main = ttk.Frame(
    root,
    padding=(30, 15)
)
main.grid()

meter_label = ttk.Label(master=main, text='Meters:')
meter_input = ttk.Entry(master=main, width=10, textvariable=meters_value)

feet_label = ttk.Label(master=main, text='Feet:')
feet_display = ttk.Label(master=main, text='Feet from here')
calc_button = ttk.Button(master=main, text='Calculate', command=calculate_feet)

meter_label.grid(row=0, column=0, sticky='W', padx=5, pady=5)
meter_input.grid(row=0, column=1, sticky='EW', padx=5, pady=5)
meter_input.focus()

feet_label.grid(row=1, column=0, sticky='W', padx=5, pady=5)
feet_display.grid(row=1, column=1, sticky='EW', padx=5, pady=5)

calc_button.grid(row=2, column=0, columnspan=2, sticky='EW', padx=5, pady=5)

root.mainloop()
