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
        self.item = {}
        self.create_widget()

    def create_widget(self):
        Label(self,
              text="Меню:"
              ).grid(row=0, column=0, columnspan=2, sticky=W)
        # формируем перечень блюд и цен
        number_row = 1
        for item in self.menu_price.keys():
            self.item[item] = BooleanVar()
            Checkbutton(self,
                        text= item + " " + str(self.menu_price[item]) + "грн",
                        variable=self.item[item]
                        ).grid(row=number_row, column=0, sticky=W)
            number_row += 1
        # кнопка для отправки данных для рассчета стоимости заказа
        Button(self,
               text="Рассчитать меню",
               command=self.count_menu
               ).grid(row=number_row, column=0, sticky=W)

        # окно вывода стоимости заказа
        Label(self,
              text="Стоимость заказа:"
              ).grid(row=number_row+1, column=0, sticky=W)

        self.win_count = Text(self, width=20, height=1)
        self.win_count.grid(row=number_row+1, column=1, sticky=W)

    def count_menu(self):
        price =0
        for item in self.menu_price.keys():
            if self.item[item].get():
                price += int(self.menu_price[item])
        self.win_count.delete(0.0, END)
        self.win_count.insert(0.0, str(price) + "грн")


# основная часть
root = Tk()
root.title("Счет, пожалуйста!")
app = Application(root)
root.mainloop()