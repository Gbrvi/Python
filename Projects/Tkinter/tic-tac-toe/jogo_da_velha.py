from tkinter import *
from tkinter import messagebox

game = Tk()
game.title('Jogo da velha')

p1 = True # X começa -> True
turn = 0 # Turnos

def desativa_botoes():
    for boton in lista_botoes:  # Desativa botoes dps de empate ou vitoria
        boton.config(state=DISABLED)

def who_win(): 
        # Condições para X ganhar
    winner = False
    if bnt1['text'] == 'X' and bnt2['text'] == 'X' and bnt3['text'] == 'X':
        for boton in lista_botoes[:3]:
            boton.config(bg='green')   

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()
    
    if bnt4['text'] == 'X' and bnt5['text'] == 'X' and bnt6['text'] == 'X':
        for boton in lista_botoes[3:6]:
            boton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt7['text'] == 'X' and bnt8['text'] == 'X' and bnt9['text'] == 'X':
        for boton in lista_botoes[6:9]:
            boton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt1['text'] == 'X' and bnt4['text'] == 'X' and bnt7['text'] == 'X':
        for boton in lista_botoes[0::3]:
            boton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt2['text'] == 'X' and bnt5['text'] == 'X' and bnt8['text'] == 'X':
        for boton in lista_botoes[1::3]:
            boton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt3['text'] == 'X' and bnt6['text'] == 'X' and bnt9['text'] == 'X':
        for boton in lista_botoes[2::3]:
            boton.config(bg='green')       
       
        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt1['text'] == 'X' and bnt5['text'] == 'X' and bnt9['text'] == 'X':
        for boton in lista_botoes[0::4]:
            boton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    if bnt3['text'] == 'X' and bnt5['text'] == 'X' and bnt7['text'] == 'X':
        for buton in [lista_botoes[2], lista_botoes[4], lista_botoes[6]]:
            buton.config(bg='green')       

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o X')
        desativa_botoes()

    # Condições para O vencer...

    if bnt1['text'] == 'O' and bnt2['text'] == 'O' and bnt3['text'] == 'O':
        for boton in lista_botoes[:3]:
            boton.config(bg='green')  

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt4['text'] == 'O' and bnt5['text'] == 'O' and bnt6['text'] == 'O':
        for boton in lista_botoes[3:6]:
            boton.config(bg='green')  

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt7['text'] == 'O' and bnt8['text'] == 'O' and bnt9['text'] == 'O':
        for boton in lista_botoes[6:9]:
            boton.config(bg='green')  

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt1['text'] == 'O' and bnt4['text'] == 'O' and bnt7['text'] == 'O':
        for boton in lista_botoes[0::3]:
            boton.config(bg='green')  

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt2['text'] == 'O' and bnt5['text'] == 'O' and bnt8['text'] == 'O':
        for boton in lista_botoes[1::3]:
            boton.config(bg='green')   

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt3['text'] == 'O' and bnt6['text'] == 'O' and bnt9['text'] == 'O':
        for boton in lista_botoes[2::3]:
            boton.config(bg='green')    

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt1['text'] == 'O' and bnt5['text'] == 'O' and bnt9['text'] == 'O':
        for boton in lista_botoes[0::4]:
            boton.config(bg='green') 

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()

    if bnt3['text'] == 'O' and bnt5['text'] == 'O' and bnt7['text'] == 'O':
        for buton in [lista_botoes[2], lista_botoes[4], lista_botoes[6]]:
            buton.config(bg='green')  

        winner = True
        messagebox.showinfo('Venceu!', 'O vencedor é o O')
        desativa_botoes()
        
    if winner == False and turn == 9:
        messagebox.showinfo('Mensagem', 'Ocorreu um empate!')
        desativa_botoes()

def click_bnt(b):
    global p1, turn

    if b['text'] == ' ' and p1 == True: # Adicionando X no botao
        b['text'] = 'X'
        turn += 1
        p1 = False
        who_win()
    
    elif b['text'] == ' ' and p1 == False:  # Adicionando O no botao
        b['text'] = 'O'
        turn += 1
        p1 = True
        who_win()

#buttons - Criação dos botões

bnt1 = Button(game, font= 'Verdana 11 bold',  text=' ', height=3, width=6, command= lambda: click_bnt(bnt1))
bnt2 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt2))
bnt3 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt3))

bnt4 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt4))
bnt5 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt5))
bnt6 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt6))

bnt7 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt7))
bnt8 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt8))
bnt9 = Button(game, font= 'Verdana 11 bold', text=' ', height=3, width=6, command= lambda: click_bnt(bnt9))

lista_botoes = [bnt1, bnt2, bnt3, bnt4, bnt5, bnt6, bnt7, bnt8, bnt9]

#grid -> Implementando os botões

bnt1.grid(row=0, column=0)
bnt2.grid(row=0, column=1)
bnt3.grid(row=0, column=2)

bnt4.grid(row=1, column=0)
bnt5.grid(row=1, column=1)
bnt6.grid(row=1, column=2)

bnt7.grid(row=2, column=0)
bnt8.grid(row=2, column=1)
bnt9.grid(row=2, column=2)

game.mainloop()