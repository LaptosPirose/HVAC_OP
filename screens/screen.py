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
