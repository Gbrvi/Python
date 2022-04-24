import time
from tkinter import *
from tkinter import font


# root = Tk()
# root.title('Relogio')
# root.geometry('320x200')

# def clock():
#     horas = time.strftime("%H")
#     minutes = time.strftime("%M")
#     seconds = time.strftime("%S")

#     label1.config(text=f'{horas} : {minutes} : {seconds}')
#     label1.after(1000, clock)

# label1 = Label(text="", font=('Times New Romans', 25))
# label1.pack()
# clock()
# root.mainloop()

# print(clock())

class Clock(Frame):

    def __init__(self, window=None):
        super().__init__(window)
        self.window = window
        self.widgets()
        self.clock_work()
    
    def clock_work(self):
        self.horas = time.strftime("%H")
        self.minutes = time.strftime("%M")
        self.seconds = time.strftime("%S")
        self.day = time.strftime("%A")

        self.timer.config(text=f'{self.horas} : {self.minutes} : {self.seconds}')
        self.day_label.config(text=self.day)

        self.timer.after(1000, self.clock_work)
        self.window.title('Relogio')
    
    def widgets(self):
        self.window.config(background='#fff')
        self.timer = Label(font=('Times News Roman', 25), background='#fff')
        self.timer.pack(ipadx=10, ipady=10)
        self.day_label = Label(font=('Times News Roman', 20), background='#FFFFF0')
        self.day_label.pack()

root = Tk()
app = Clock(root)
app.mainloop()