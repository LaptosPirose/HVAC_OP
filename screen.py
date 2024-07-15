import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from windows import set_dpi_awarewness

set_dpi_awarewness.set_dpi_awareness()

root = tk.Tk()
root.geometry("600x480+400+200")
root.resizable(False, False)
root.title("Labels")

my_label = ttk.Label(root, text='Hello, World!', padding=20)
my_label.config(font=('Times New Roman', 30))
# In order to insert images you eill need to install PIllow library
my_label.pack()


root.mainloop()
