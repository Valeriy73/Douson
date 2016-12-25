# -*- encoding: utf-8 -*-

# Простейший GUI
# Демонстрирует создание окна

from Tkinter import *

# создание базового окна
root = Tk()

# изменние окна
root.title("Простейший GUI")
root.geometry("200x100")

# старт событийного цикла
root.mainloop()
