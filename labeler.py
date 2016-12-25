# -*- encoding: utf-8 -*-

# Это я, метка
# Демонстрирует применение меток
from  Tkinter import *
# создание базового окна
root = Tk()
root.title("Это я, метка")
root.geometry("200x50")

# внутри окна создается рамка для размещения других элементов
app = Frame(root)
app.grid()
lbl = Label(app, text = "Вот она я!")
lbl.grid()

# старт событийного цикла
root.mainloop()

