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

root.resizable(False, False)

root.title("Distance Converter")

main = ttk.Frame(
    root,
    padding=(30, 15)
)


root.mainloop()
