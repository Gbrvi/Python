from tkinter import *

root = Tk()

class App():
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_de_tela()
        root.mainloop()
    
    def tela(self):
        self.root.title('Aplicativo')
        self.root.configure(background='#008B8B')
        self.root.geometry('700x500')
    
    def frame_de_tela(self):
        self.frame_1 = Frame(self.root)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46) #rlx vai de 0 a 1. Mais perto de 1 = direita, mais perto de 0 = esquerda

App()