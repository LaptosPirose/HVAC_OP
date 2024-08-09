import tkinter as tk
from tkinter import ttk


class MainScreen(tk.Tk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
        self.title("Siemens PLC Monitor")
        self.frames = dict()
        
        self.screen_height = self.winfo_screenheight()
        self.screen_width = self.winfo_screenwidth()
        self.geometry(str(self.screen_width)+'x'+str(self.screen_height)+'+0+0')
        
        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")
        
        frame = MainWindow(self)
        frame.grid(padx=10, pady=10, sticky="EW")
        
        print(type(container))
              
class MainWindow(ttk.Frame):
        
    def __init__(self, container):
        super().__init__(container)

        self.label = ttk.Label(self, text='Teste de carregamento')
        self.label.grid(padx=10, pady=10, sticky="NSE")
       

root = MainScreen()
root.mainloop()
