import random
import string
from tkinter import *

menu = Tk()
menu.title('Gerador de senha')

def gerador_senhas(tam=9, upper=True, lower=True, num=True, simbol=True):
    words = []
    if upper:
        words.extend(string.ascii_uppercase)
    if lower:
        words.extend(string.ascii_lowercase)
    if num:
        words.extend(str(string.digits))
    if simbol:
        words.extend(string.punctuation)
    senha = ''.join(random.choices(words, k=tam))
    label2['text'] = senha

#button
botao = Button(menu, text='Gerar', command= lambda: gerador_senhas())
label2 = Label(menu)
label1 = Label(menu, text='Gerador de senhas')

#layout
label1.grid(row=0, column=1)
label2.grid(row=1, column=1)
botao.grid(row=2, column=1, columnspan=1)
menu.mainloop()