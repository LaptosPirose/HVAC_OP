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
