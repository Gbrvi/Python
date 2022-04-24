from pytube import YouTube 
from tkinter import * 
from time import sleep

#funcs
def download_vid():
    try:
        ytb = YouTube(entry_link.get())

        stream = ytb.streams.get_highest_resolution()
        stream.download(output_path='C:\\Users\\Acer\\Downloads')
        label_info['text'] = 'Download concluido'
    except:
        label_info['text'] = 'Insira um link válido!'

    label_info.grid(row=2, column=0, columnspan=2, sticky='n')

#Grid
root =  Tk()
root.title('Download youtube videos')
root.config(background='#f1f2f3')
root.resizable(False, False)

#Labels
lb_intro = Label(root, text='Link:', font=('times', 12, 'bold'), bg='#f1f2f3')
label_info = Label(root, relief='sunken', bg='#7FFFD4')

#Entry
entry_link = Entry(root, bg="#f1f2f3")

#Button
bnt_down = Button(root, text='Download', command= download_vid)

#Grid
lb_intro.grid(row=0, column=0)

entry_link.grid(row=0, column=1)

bnt_down.grid(row=1, column=1, sticky='e', padx=5, pady=5)

root.mainloop()

# TK dict_keys(['bd', 'borderwidth', 'class', 'menu', 'relief', 'screen', 'use', 'background', 'bg', 
# 'colormap', 'container', 'cursor', 'height', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'padx', 'pady', 
# 'takefocus', 'visual', 'width'])

# LABELS dict_keys(['activebackground', 'activeforeground', 'anchor', 'background', 'bd', 'bg', 'bitmap', 
# 'borderwidth', 'compound', 'cursor', 'disabledforeground', 'fg', 'font', 'foreground', 'height', 'highlightbackground', 'highlightcolor',
#  'highlightthickness', 'image', 'justify', 'padx', 'pady', 'relief', 'state', 'takefocus', 'text', 'textvariable', 'underline', 'width', 'wraplength'])

# Entry dict_keys(['background', 'bd', 'bg', 'borderwidth', 'cursor', 'disabledbackground', 'disabledforeground', 'exportselection',
#  'fg', 'font', 'foreground', 'highlightbackground', 'highlightcolor', 'highlightthickness', 'insertbackground', 
# 'insertborderwidth', 'insertofftime', 'insertontime', 'insertwidth', 'invalidcommand', 'invcmd', 'justify', 'readonlybackground',
#  'relief', 'selectbackground', 'selectborderwidth', 'selectforeground', 'show', 'state', 'takefocus', 'textvariable', 'validate', 
# 'validatecommand', 'vcmd', 'width', 'xscrollcommand'])


# ytb = YouTube("https://www.youtube.com/watch?v=QSWPUfNYgUs")

# print(ytb.streams.filter(progressive=True)) # Progressive são vídeos com audio e video juntos
# adaptative são vídeos e audios SEPARADOS
# only_audio -> Apenas audio
# file_extension='mp4' -> Apenas formato MP4

# stream = ytb.streams.get_by_itag(22)
# stream.download(output_path='C:\\Users\\Acer\\Downloads')
