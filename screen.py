import tkinter as tk
from tkinter import ttk
import tkinter.font as font

import sys
import os

path = os.path.abspath(os.curdir) + '/windows'
print(path)

import set_dpi_awarewness # type: ignore


print(os.path.abspath(os.curdir))


set_dpi_awarewness.set_dpi_awareness()


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
