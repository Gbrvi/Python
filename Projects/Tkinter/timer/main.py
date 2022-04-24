from tkinter import *
import time
import tkinter

clockWindow = Tk()
clockWindow.geometry('200x200')
clockWindow.title('Timer')
clockWindow.config(background='orange')


hours_string = StringVar()
minutes_string = StringVar()
seconds_string = StringVar()

hours_string.set('00')
minutes_string.set('00')
seconds_string.set('00')

hours_textbox = Entry(clockWindow, width=3, font=('Calibri', 20, ""), textvariable=hours_string)
minutes_textbox = Entry(clockWindow, width=3, font=('Calibri', 20, ""), textvariable=minutes_string)
seconds_textbox = Entry(clockWindow, width=3, font=('Calibri', 20, ""), textvariable=seconds_string)

hours_textbox.bind("<Button-1>", lambda e: hours_textbox.delete(0, tkinter.END))
minutes_textbox.bind("<Button-1>", lambda e: minutes_textbox.delete(0, tkinter.END))
seconds_textbox.bind("<Button-1>", lambda e: seconds_textbox.delete(0, tkinter.END))

hours_textbox.place(x=30, y=75)
minutes_textbox.place(x=80, y=75)
seconds_textbox.place(x=130, y=75)

def run_time():
    
    clocktime = (int(hours_string.get()) * 3600) + (int(minutes_string.get()) * 60) + int(seconds_string.get())

    hours_textbox.config(state=DISABLED, disabledbackground='#fffafa')
    minutes_textbox.config(state=DISABLED, disabledbackground='#fffafa')
    seconds_textbox.config(state=DISABLED, disabledforeground='black', disabledbackground='white')

    while clocktime > -1:    

        total_minutes, total_seconds = divmod(clocktime, 60)

        total_hours = 0
        if total_hours > 60:
            total_minutes, total_seconds = divmod(total_minutes, 60)
        
        # hours_string.set(f'{total_hours:2d}')
        # minutes_string.set(f'{total_minutes:2d}')
        # seconds_string.set(f'{total_seconds:2d}')


        hours_string.set(f'{total_hours:2d}' if total_hours > 9 else f'0{total_hours:1d}')
        minutes_string.set(f'{total_minutes:2d}' if total_minutes > 9 else f'0{total_minutes:1d}')
        seconds_string.set(f'{total_seconds:2d}' if total_seconds > 9 else f'0{total_seconds:1d}')

        clockWindow.update()
        time.sleep(1)


        clocktime -= 1


start_button = Button(clockWindow, text='start', command=run_time)

start_button.place(x=30, y=30)



clockWindow.mainloop()

