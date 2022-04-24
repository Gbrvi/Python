from tkinter import *


def kelvin():
    resultado_kelvin.set(str(round((float(entry_fah.get()) + 459.67) / 1.8, 2)) + 'K')

def celsius():
    resultado_cels.set(str(round((float(entry_fah.get()) - 32) * 5/9, 2)) + 'C')

#GIU
menu = Tk()
menu.title('conversor')

#Variaveis
resultado_cels = StringVar()
resultado_kelvin = StringVar()

#label 
label1 = Label(menu, text='Inserir Fahrenheit:', bg='white', anchor=CENTER)
label2 = Label(menu, textvariable=resultado_cels)
label3 = Label(menu, textvariable=resultado_kelvin)

#Entry
entry_fah = Entry(menu, width=30)

#button
botao_kelvin = Button(menu, text='Kelvin', command=kelvin)
botao_celsius = Button(menu, text='Celsius', command=celsius)

#layout
label1.grid(row=0, columnspan=2)
entry_fah.grid(row=1, columnspan=1)
label2.grid(row=2, columnspan=1)
label3.grid(row=3, columnspan=1)
botao_kelvin.grid(row=4, column=0, sticky=W)
botao_celsius.grid(row=4, columnspan=2, sticky=E)

#Focus
entry_fah.focus()
mainloop()







