# -*- encoding: utf-8 -*-

# закрытая зверюшка
# Деомнстрирует закрытые переменные и методы


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, mood):
        print("Появилась на свет новая зверюшка!")
        self.name = name # открытый атрибут
        self.__mood = mood # закрытый атрибут

    def talk(self):
        print("Меня зовут {0}\n".format(self.name))
        print("Сейчас я чувстую себя {0}\n".format(self.__mood))

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод.")
        self.__private_method()

# Основная часть
crit = Critter(name="Бобик", mood="прекрасно")
crit.talk()
crit.public_method()
input("\n\nНажмите Enter, чтобы выйти.")
