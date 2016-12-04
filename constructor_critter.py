# -*- encoding: utf-8 -*-

# Зверюшка с конструктором
# Деомнстрирует метод-конструктор


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self):
        print("Появилась на свет новая зверюшка!")

    def talk(self):
        print("Привет. Я зверюшка - экземпляр класса Critter.")
# Основная часть
crit1 = Critter()
crit2 = Critter()
crit1.talk()
crit2.talk()
input("\n\nНажмите Enter, чтобы выйти.")
