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

text.insert("1.0", "Enter the thext here...")

root.mainloop()
