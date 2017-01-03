# -*- encoding: utf-8 -*-

# Отгадай число
# Нужно отгадать число от 1 до 100
from Tkinter import *
import random


class Application(Frame, object):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.the_number = random.randint(1, 100)
        self.create_widget()

    def create_widget(self):
        # приветсвте
        Label(self,
              text="Добро пожаловать в игру 'Отгадай число'!"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        # правила игры
        Label(self,
              text="Правила:"
              ).grid(row=1, column=0, sticky=W)
        Label(self,
              text="Я загадал натуральное число из диапазона от 1 до 100."
              ).grid(row=2, column=0, columnspan=2, sticky=W)
        Label(self,
              text="Постарайтесь отгадать его за минимальное число попыток."
              ).grid(row=3, column=0, columnspan=2, sticky=W)
        # ввод значения
        Label(self,
              text="Ваше предположение: "
              ).grid(row=4, column=0, sticky=W)

        self.guess = Entry(self)
        self.guess.grid(row=4, column=1, sticky=W)

        # кнопка отсылки данных
        Button(self,
               text="Мой вариант!",
               command=self.guess_number
               ).grid(row=5, column=1, sticky=W)

        # вывод результата
        Label(self,
              text="Результат: "
              ).grid(row=6, column=0, sticky=W)
        self.rezult = Text(self, width=20, height=1, wrap=WORD)
        self.rezult.grid(row=6, column=1, sticky=W)
        self.rezult.insert(0.0, "Здесь будет результат")

    def guess_number(self):
        my_number = int(self.guess.get())
        if self.the_number > my_number:
            text_rezult = "наше число больше"
        elif self.the_number < my_number:
            text_rezult = "наше число меньше"
        else:
            text_rezult = "ты отгадал"
        self.rezult.delete(0.0, END)
        self.rezult.insert(0.0, text_rezult)

# основная часть
root = Tk()
root.title = "Отгадай число"
app = Application(root)
app.mainloop()
