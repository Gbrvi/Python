from tkinter import *
from tkinter import messagebox
from time import sleep

class Clock_Work(Frame):
    def __init__(self, window= None):
        super().__init__(window)
        self.window = window
        self.hours_string, self.minutes_string, self.seconds_string = StringVar(), StringVar(), StringVar()

        self.create_widgets()
    
    def set_strings(self):
        # Setando valor padrao pras variaveis criadas
        self.hours_string.set('00')
        self.minutes_string.set('00')
        self.seconds_string.set('00')

        
    def create_widgets(self):
        # Criação e posição dos widgets

        self.set_strings() # Chama a função de setar strings

        self.window.title('Timer')
        self.window.geometry('200x100')
        self.window.config(background='#6599FF')
        self.window.resizable(False, False)      

        self.info_label = Label(self.window, text='Insira o tempo!', font=('Maiandra GD', 12), background='#6599FF',)
        self.info_label.place(x=50, y=1)  

        self.hours_textbox = Entry(self.window, width=3, font=('Times New Romans', 15), background='#6599FF', textvariable=self.hours_string)
        self.hours_textbox.place(x=45, y=30)

        self.minutes_textbox = Entry(self.window, width=3, font=('Times New Romans', 15), background='#6599FF', textvariable=self.minutes_string)
        self.minutes_textbox.place(x=85, y=30)

        self.seconds_textbox = Entry(self.window, width=3, font=('Times New Romans',15), background='#6599FF', textvariable=self.seconds_string)
        self.seconds_textbox.place(x=125, y=30)

        self.button_start = Button(self.window, text='Start', font=('Maiandra GD', 11), background='#FF9900', command=self.run_clock)
        self.button_start.place(x=170, y=80, anchor=CENTER)

        self.button_pause = Button(self.window, text='pause', font=('Maiandra GD', 11), background='#FF9900',command=self.pause_button)
        self.button_pause.place(x=110, y=80, anchor=CENTER)

        self.button_reset = Button(self.window, text='reset', font=('Maiandra GD', 11), background='#FF9900', command=self.reset_button)
        self.button_reset.place(x=50, y=80, anchor=CENTER)

        self.clean_entry()

    def clean_entry(self):
        # Limpa quando o mouse passar clicar em qualquer entry
        self.hours_textbox.bind("<Button-1>", lambda e: self.hours_textbox.delete(0, END)) 
        self.minutes_textbox.bind("<Button-1>", lambda e: self.minutes_textbox.delete(0, END)) 
        self.seconds_textbox.bind("<Button-1>", lambda e: self.seconds_textbox.delete(0, END)) 

    
    def disable_entry(self):
        #Desativa os botões 
        self.hours_textbox.config(state=DISABLED, disabledbackground='white', disabledforeground='black')
        self.minutes_textbox.config(state=DISABLED, disabledbackground='white', disabledforeground='black')
        self.seconds_textbox.config(state=DISABLED, disabledbackground='white', disabledforeground='black')
    
    def pause_button(self):
        #Pausa o botão
        self.running = False

    def reset_button(self):
        #Reseta o botão
        self.running = False
        self.enable_entry()

    def enable_entry(self):
        # Reativa os botões
        self.hours_textbox.config(state=NORMAL)
        self.minutes_textbox.config(state=NORMAL)
        self.seconds_textbox.config(state=NORMAL)

    def run_clock(self):
        self.running = True     # Necessario para saber quando será pausado ou resetado

        try:
            # Faz os calculos transformando os valores digitados nas entry em horas, minutos e segundos
            self.clock_time = (int(self.hours_string.get()) * 3600) + (int(self.minutes_string.get()) * 60) + int(self.seconds_string.get())
            self.disable_entry()
            
        except ValueError: # Aparece messagebox caso nao seja digitado números
            messagebox.showinfo('ERRO!', 'Insira apenas números')            

        while self.clock_time > -1:

            if not self.running:
                break

            self.total_minutes, self.total_seconds = divmod(self.clock_time, 60)    # Divide a soma das horas e coloca o quociente nos minutos e o resto nos segundos

            self.total_hours = 0

            if self.total_minutes > 60:
                self.total_hours, self.total_minutes = divmod(self.total_minutes, 60) # Divide total dos minutos acima de 60, quociente vai para as horas, resto para os minutos
            
            # Apresentação na tela do timer 
            self.hours_string.set(f'{self.total_hours}' if self.total_hours > 9 else f'0{self.total_hours}')
            self.minutes_string.set(f'{self.total_minutes}' if self.total_minutes > 9 else f'0{self.total_minutes}')
            self.seconds_string.set(f'{self.total_seconds}' if self.total_seconds > 9 else f'0{self.total_seconds}')

            # Atualiza a tela
            self.window.update()

            # Dorme por um segundo
            sleep(1)

            self.clock_time -= 1

def start():
    root = Tk()
    Clock_Work(root)
    root.mainloop()

start()