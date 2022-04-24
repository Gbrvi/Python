''' Criação de um cronometro feito com POO'''
from tkinter import *
from tokenize import String
from turtle import right

class Stopwatch(Frame):
    
    def __init__(self, window = None):
        # Instancias da classe
        super().__init__(window)
        self.window = window
        self.running = False    # Utilizado para controle das funções start, pause & reset 
        self.minutes, self.seconds, self.miliseconds = StringVar(), StringVar(), StringVar(),
        self.set_strings()
        self.create_widgets()

    def set_strings(self):
        self.minutes.set('00')
        self.seconds.set('00')
        self.miliseconds.set('00')

    def create_widgets(self):
        # Configurando a tela
        self.window.config(background='#FFDE00')
        self.window.title('Stopwatch')
        self.window.resizable(False, False)
        self.window.geometry('200x105')

        # Criação das entrys
        self.stopwatch_minutes = Entry(textvariable=self.minutes, width=2, font=('Times New romans', 20), bg='#FFEA00')
        self.stopwatch_minutes.place(relx=0.2, rely= 0.1)

        self.stopwatch_seconds = Entry(textvariable=self.seconds, width=2, font=('Times New romans', 20), bg='#FFEA00')
        self.stopwatch_seconds.place(relx=0.4, rely=0.1)

        self.stopwatch_miliseconds = Entry(textvariable=self.miliseconds, width=2, font=('Times New romans', 20), bg='#FFEA00')
        self.stopwatch_miliseconds.place(relx=0.6, rely=0.1)

        # Botão de iniciar
        self.start_button = Button(text='Start', font=('Candara', 12), background='#6599FF', activebackground='#107db2', command=self.start)
        self.start_button.place(relx=0.05, rely=0.6)

        # #Botão de pause
        self.pause_button = Button(text='Pause', font=('Candara', 12), background='#6599FF', activebackground='#6599FF', command=self.pause)
        self.pause_button.place(relx=0.35, rely=0.6)

        # #Botão de reset
        self.reset_button = Button(text='Reset', font=('Candara', 12), background='#6599FF', activebackground='#6599FF', command=self.reset)
        self.reset_button.place(relx=0.7, rely=0.6)
        
        self.disable_entry()
        self.disable_button(self.pause_button, self.reset_button)

    def disable_entry(self):
        # Desativa as entry
        self.stopwatch_minutes.config(state=DISABLED, disabledbackground='white', disabledforeground='black') 
        self.stopwatch_seconds.config(state=DISABLED, disabledbackground='white', disabledforeground='black')
        self.stopwatch_miliseconds.config(state=DISABLED, disabledbackground='white', disabledforeground='black')   

    def enable_button(self):
        # Ativa os botões
        self.reset_button.config(state=ACTIVE)
        self.pause_button.config(state=ACTIVE)
    
    def disable_button(self, *arg):
        # Desativa os botões
        for self.button in arg:
            self.button.config(state=DISABLED)


    def _update(self):
        # Função que atualiza o cronometro

        self.min = int(self.minutes.get())
        self.sec = int(self.seconds.get())
        self.milisec = int(self.miliseconds.get())

        self.milisec += 1

        if self.milisec == 60:
            self.sec += 1
            self.milisec = 0

        if self.sec == 60:
            self.min += 1
            self.sec = 0

        # Cria a minutagem que apareça no cronometro

        self.minutes.set(f'{self.min}' if self.min > 9 else f'0{self.min}')
        self.seconds.set(f'{self.sec}' if self.sec > 9 else f'0{self.sec}')
        self.miliseconds.set(f'{self.milisec}' if self.milisec > 9 else f'0{self.milisec}')

        # Ativa os botões desativados
        self.enable_button()

        # self.update_time utlizado para pausar ou resetar o cronometro
        self.update_time = self.stopwatch_miliseconds.after(10, self._update)
    
    # Função de iniciar
    def start(self):
        if not self.running:
            self._update()
            self.running = True

    # Função de pause
    def pause(self):
        if self.running:
            # Cancela a contagem
            self.stopwatch_miliseconds.after_cancel(self.update_time)
            self.running = False
            # Desativa os botões escolhidos
            self.disable_button(self.pause_button)
    
    # Função de reset
    def reset(self):
        if self.running:
            # Cancela a contagem
            self.stopwatch_miliseconds.after_cancel(self.update_time)
            self.running = False
        
        # Desativa os botões escolhidos
        self.disable_button(self.pause_button, self.reset_button)

        # Define tudo para a minutagem inicial (00:00:00)
        self.set_strings()

if __name__ == '__main__':
    root = Tk()
    app = Stopwatch(root)
    app.mainloop()