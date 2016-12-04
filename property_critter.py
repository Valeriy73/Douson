# -*- encoding: utf-8 -*-

# Зверюшка со свойствами
# Деомнстрирует свойства


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name):
        print "Появилась на свет новая зверюшка!"
        self.__name = name  # закрытый атрибут

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if new_name == "":
            print("Имя зверюшки не может быть пустой строкой.")
        else:
            self.__name = new_name
            print("Имя успешно изменено.")

    def talk(self):
        print "\nПривет, меня зовут ", self.name


# Основная часть
crit = Critter("Бобик")
crit.talk()
print("\nМою зверюшку зовут")
print(crit.name)
print("\nПробую изменить имя зверюшки на Мурзик...")
crit.name = "Мурзик"
print("\nМою зверюшку зовут")
print(crit.name)
print("\nПробую изменить имя зверюшки на пустую строку...")
crit.name = ""
print("\nМою зверюшку зовут")
print(crit.name)
input("\n\nНажмите Enter, чтобы выйти.")
