from tkinter import *
import tkinter
from tkinter import font

root = Tk()
root.title('Cronometro')
root.geometry('250x120')

running = False
hours, minutes, seconds = 0, 0, 0

# Func

def start_stopwatch():
    global running
    if not running:
        update()
        running = True

def pause_stopwatch():
    global running
    if running:
        cronometro.after_cancel(update_time)
        running = False
    

def reset_stopwatch():
    global running, hours, minutes, seconds
    if running:
        cronometro.after_cancel(update_time)
        running = False
    hours, minutes, seconds = 0, 0, 0
    cronometro.config(text='00:00:00')

def update():
    global hours, minutes, seconds
    seconds += 1
    if seconds == 60:
        minutes += 1
        seconds = 0
    if minutes == 60:
        hours == 1
        minutes = 0
    hours_string = f'{hours}' if hours > 9 else f'0{hours}'
    minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}' 
    seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'

    cronometro.config(text=hours_string + ':' + minutes_string + ':' + seconds_string)
    global update_time
    update_time = cronometro.after(1000, update)

# Widgets
cronometro = Label(text='00:00:00', font=('Times New Romans', 30))

start = Button(text='Start', font=('Times New Romans', 10), command=start_stopwatch)
pause = Button(text='Pause', font=('Times New Romans', 10), command=pause_stopwatch)
reset = Button(text='Reset', font=('Times New Romans', 10), command=reset_stopwatch)

cronometro.grid(row=0, column=2)
start.grid(row=1, column=1)
pause.grid(row=1, column=2)
reset.grid(row=1, column=3)



root.mainloop()
