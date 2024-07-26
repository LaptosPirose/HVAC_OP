import tkinter as tk
import tkinter.ttk

print('Entering the style module!')
root = tk.Tk()
root.geometry("800x200+200+200")

s = tkinter.ttk.Style()
s.configure("My.TFrame", background='red')

mail1 = tkinter.ttk.Frame(root, style='My.TFrame')
mail1.place(width=400, height=100, x=10, y=10)
mail1.config()

label = tkinter.ttk.Label(mail1, text="Hello", background='red')
label.place(x=5, y=5)
label.config()

root.mainloop()
