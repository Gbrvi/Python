import ctypes
from os import listdir
from random import choice
CAMINHO = "C:\\Users\\Acer\\OneDrive\\Documentos\\Wallpapers" 

def wallpaper():
    today_wallpaper = listdir(CAMINHO)
    return choice(today_wallpaper)

def definindo():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, CAMINHO + "\\" + wallpaper(), 0)

definindo()