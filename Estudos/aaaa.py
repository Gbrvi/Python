from tkinter import *
from tkinter.font import BOLD
root = Tk()
widget = Label(root, text='Boa noite grupo', justify='center')
widget.config(
    bd=5, 
    relief=SUNKEN,
    font=('times', 30, BOLD),   
    height=3,
    padx=5,
    pady=5,
    bg='black',
    fg='Yellow'
)
widget.grid(row=0, column=1, columnspan=3, sticky='news')
root.mainloop()
