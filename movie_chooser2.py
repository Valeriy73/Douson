# -*- encoding: utf-8 -*-

# Киноман-2
# Демонстрирует переключатель
from Tkinter import *

class Application(Frame, object):
    """ GUI-приложение, позволяющее выбрать один любимый жанр кино. """
    def __init__(self, master):
        """ Инициализирует рамку. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets():
    """ Создает элементы, с помощью которых пользователь будет выбирать. """
    # метка-описание
    Label(self,
          text = "Укажите выш любимый жанр кино"
          ).grid(row = 0, column = 0, sticky = W