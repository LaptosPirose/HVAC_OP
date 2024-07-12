import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry("800x600+550+200")

main = ttk.Frame(root)
main.pack(side='left', fill='both', expand=True)


label1 = tk.Label(main, text='Panel Top', bg='red').pack(
    side='top', expand=True, fill='both')
label2 = tk.Label(root, text='Panel Top', bg='red').pack(
    side='top', expand=True, fill='both')
label3 = tk.Label(main, text='Panel Left', bg='green').pack(
    side='left', expand=True, fill='both')


root.mainloop()
