from tkinter import * 
import webbrowser


def pesquisar():
    webbrowser.open(pesquisa.get())


menu = Tk()
menu.title('Search')

label1 = Label(menu, text='URL:')
pesquisa = Entry(menu)
button = Button(menu, text='Search', command=pesquisar)


label1.grid(row=0, column=0)
pesquisa.grid(row=0, column=1)
button.grid(row=1, column=1, columnspan=2)


menu.mainloop()