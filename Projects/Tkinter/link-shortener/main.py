from cProfile import label
from cgitb import text
from tkinter.font import BOLD
import pyshorteners
from tkinter import *

root = Tk()
root.title('Encurtador')
root.geometry('200x100') 
root['background'] = "orange" 

def shorter_link():
    shortner = pyshorteners.Shortener()
    new_link = shortner.tinyurl.short(entry_link.get())
    entry_return.insert(0, new_link)
    entry_return.place(x=32, y=30)
    entry_return.configure(state='readonly')

# Widgets 

label_link = Label(root, text='Link:', font=('Time News Romans', 9, BOLD), bg="orange")

entry_link = Entry(root, width=25, relief="raised", bd=2)
button_link = Button(root, text='GO', relief="raised", bd=2, command=shorter_link)

label_return = Label(root, text='Out:', font=('Time News Romans', 9, BOLD), bg="orange")
entry_return = Entry(root, width=26)

label_link.place(x=0, y=0)
entry_link.place(x=35, y=0)
button_link.place(x=173, y=74)

label_return.place(x=0, y=30)

root.mainloop()


