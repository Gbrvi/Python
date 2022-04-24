''' Criação de um cronometro feito com POO'''
from tkinter import *
from tokenize import String

class Stopwatch(Frame):
    
    def __init__(self, window = None):
        # Instancias da classe
        super().__init__(window)
        self.window = window
        self.running = False    # Utilizado para controle das funções start, pause & reset 
        self.hours, self.minutes, self.seconds = 0, 0, 0
        self.create_widgets()

    def create_widgets(self):
        # Configurando a 
        self.window.config(background='#FFEA00')
        self.window.title('Stopwatch')
        self.window.resizable(False, False)

        self.stopwatch_label = Label(text='00 : 00 : 00s', font=('Times New romans', 22), bg='#FFEA00')
        self.stopwatch_label.pack()

        # Botão de iniciar
        self.start_button = Button(text='Start', font=('Candara', 12), command=self.start)
        self.start_button.pack(side=LEFT, padx=5, pady=5)

        #Botão de pause
        self.pause_button = Button(text='Pause', font=('Candara', 12), command=self.pause)
        self.pause_button.pack(side=LEFT, padx=5, pady=5)

        #Botão de reset
        self.reset_button = Button(text='Reset', font=('Candara', 12),  command=self.reset)
        self.reset_button.pack(side=LEFT, padx=5, pady=5)

        self.disable_button(self.pause_button, self.reset_button)
    
    def enable_button(self):
        self.reset_button.config(state=ACTIVE)
        self.pause_button.config(state=ACTIVE)
    
    def disable_button(self, *arg):
        for self.button in arg:
            self.button.config(state=DISABLED)


    def _update(self):
        # Função que atualiza o cronometro
        self.seconds += 1

        if self.seconds == 60:
            self.minutes += 1
            self.seconds = 0

        if self.minutes == 60:
            self.hours += 1
            self.minutes = 0

        # Cria a minutagem que apareça no cronometro

        hours_string = f'{self.hours}' if self.hours > 9 else f'0{self.hours}'
        minutes_string = f'{self.minutes}' if self.minutes > 9 else f'0{self.minutes}' 
        seconds_string = f'{self.seconds}' if self.seconds > 9 else f'0{self.seconds}'

        # Configura o label do cronometro
        self.stopwatch_label.config(text=f'{hours_string} : {minutes_string} : {seconds_string}s')

        # Ativa os botões desativados
        self.enable_button()

        # self.update_time utlizado para pausar ou resetar o cronometro
        self.update_time = self.stopwatch_label.after(1000, self._update)
    
    # Função de iniciar
    def start(self):
        if not self.running:
            self._update()
            self.running = True

    def pause(self):
        if self.running:
            # Cancela a contagem
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
            # Desativa os botões escolhidos
            self.disable_button(self.pause_button)
    
    def reset(self):
        if self.running:
            # Cancela a contagem
            self.stopwatch_label.after_cancel(self.update_time)
            self.running = False
        
        # Desativa os botões escolhidos
        self.disable_button(self.pause_button, self.reset_button)

        # Define tudo para a minutagem inicial (00:00:00)
        self.stopwatch_label.config(text='00 : 00 : 00s')
        self.hours, self.minutes, self.seconds = 0, 0, 0

if __name__ == '__main__':
    root = Tk()
    app = Stopwatch(root)
    app.mainloop()