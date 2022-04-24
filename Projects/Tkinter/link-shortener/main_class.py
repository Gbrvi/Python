from email import message
from os import stat
from tkinter import *
from tkinter import messagebox
from tkinter.font import BOLD
import pyshorteners

class Encurtador(Frame):
    def __init__(self, window=None):
        super().__init__(window)
        self.window = window

        # Chama a função que cria os widgets
        self.create_widgets()


    def create_widgets(self):
        self.window.geometry("200x100")
        self.window.title("Encurtador")
        self.window.config(background = 'orange' )

        self.label_link = Label(self.window, text='Link:', font=('Time News Romans', 9, BOLD), bg="orange")
        self.label_link.place(x=0, y=0)

        self.entry_link = Entry(self.window, width=25, relief="raised", bd=2)
        self.entry_link.place(x=35, y=0)

        self.button_link = Button(self.window, text='GO', relief="raised", bd=2, command=self.shorter_link)
        self.button_link.place(x=173, y=74)

        self.label_return = Label(self.window, text='Out:', font=('Time News Romans', 9, BOLD), bg="orange")
        self.label_return.place(x=0, y=30)
    
    def shorter_link(self):
        # Função que encurta os links
        try:
            self.shortner = pyshorteners.Shortener()
            self.new_link = self.shortner.tinyurl.short(self.entry_link.get())
            # Mostra o entry apenas após clicar no botão
            self.show_output()

            self.entry_return.insert(0, self.new_link) 
            self.entry_return.config(state='readonly')  # Permite que seja copiado o texto do entry 
        except:
            messagebox.showerror('ERROR', 'Enter a valid URL.')
    
    def show_output(self):
        self.entry_return = Entry(self.window, width=26, relief="raised", bd=2)
        self.entry_return.place(x=32, y=30)
    
def main():
    root = Tk()
    app = Encurtador(root)
    app.mainloop()

main()