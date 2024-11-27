#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# origen: https://recursospython.com/guias-y-manuales/posicionar-elementos-en-tkinter/

import tkinter as tk
from tkinter import ttk

class Application(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)
        main_window.title("Posicionar elementos en Tcl/Tk")
        
        main_window.configure(width=300, height=200)
        # Ignorar esto por el momento.
        self.place(relwidth=1, relheight=1)

        # self.entry = ttk.Entry(self)
        # self.entry.pack()

        self.button = ttk.Button(self, text="girar")
        # self.button.place(x=60, y=40)
        # self.button.place(relx= relwidth=0.5, relheight=0.5)
        # self.button.place(relx=0.5, rely=0.5, relwidth=0.5, relheight=0.5)
        self.button.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.button.pack()
        # self.pack()
                        
                
                
if __name__ == "__main__":

    main_window = tk.Tk()
    app = Application(main_window)
    app.mainloop()

