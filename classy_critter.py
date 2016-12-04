# -*- encoding: utf-8 -*-

# Классово верная зверюшка
# Деомнстрирует атрибуты класса и статические методы


class Critter(object):
    """Виртуальный питомец"""
    total = 0

    @staticmethod
    def status():
        print "\nВсего зверюшек сейчас", Critter.total

    def __init__(self, name):
        print("Появилась на свет новая зверюшка!")
        self.name = name
        Critter.total += 1

# Основная часть

print("Нахожу значение атрибута класса Critter.total:")
print(Critter.total)
Critter.status()
print("\nСоздаю зверюшек.")
crit1 = Critter("Зверюшка 1")
crit2 = Critter("Зверюшка 2")
crit3 = Critter("Зверюшка 3")
Critter.status()
print("\nОбращаюсь к атрибуту класса через объект:")
print(crit1.total)
input("\n\nНажмите Enter, чтобы выйти.")
