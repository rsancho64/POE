#! /usr/bin/python3

# intro POE w py : https://enriquelazcorreta.gitbooks.io/tkinter/content/
# un ejemplo:

from tkinter import *

def key(event):
    print("tecla pulsada:", repr(event.char))

def callback(event):
    frame.focus_set()
    print("click en", event.x, event.y)

if __name__ == "__main__":

    root = Tk()

    frame = Frame(root, width=200, height=200)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.pack()

    root.mainloop()

