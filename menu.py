# -*- encoding: utf-8 -*-

# Счет, пожалуйста!
# Рассчитывает стомость заказа на основе меню
from Tkinter import *

class Application(Frame, object):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.menu_price = {"Осетрина": 105,
                          "Телятина": 26,
                          "Люляки-баб": 55,
                          "Котлеты": 16,
                          "Нарезка": 30}
        self.create_widget()

    def create_widget(self):
        Label(self,
              text="Меню:"
              ).grid(row=0, column=0, columnspan=2, sticky=W)


# основная часть
root = Tk()
root.title("Счет, пожалуйста!")
app = Application(root)
root.mainloop()