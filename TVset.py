# -*- encoding: utf-8 -*-

class TVset(object):
    """Программ пульт телевизора: каналы и громкость"""
    def __init__(self, name, chenal=12, volume=12):
        self.__name = name
        self.__chenal = chenal
        self.__volume = volume

    @property
    def name(self):
        return self.__name
    
    @property
    def chenal(self):
        return self.__chenal

    @property
    def volume(self):
        return self.__volume

    @chenal.setter
    def chenal(self, new_chenal):
        if new_chenal < 0:
            print 'Каналы на чинаются с "0"'
        elif new_chenal > 24:
            print 'Мы поддерживаем только 24 канала'
        else:
            self.__chenal = new_chenal

    @volume.setter
    def volume(self, new_volume):
        if new_volume < 0:
            print 'Громкость не может быть меньше нуля'
        elif new_volume > 24:
            print 'Максимальная громкость 24 единицы'
        else:
            self.__volume = new_volume

    
def hello(my_tv):
    
    print "Ваш телевизор %s имеет следующие настройки:\n" % my_tv.name
    print "Выбран канал: %s\n" % my_tv.chenal
    print "Установлена громкость: %s\n" % my_tv.volume  


def main():
    name_tv = raw_input("Введите название вашего телевизора: ")
    my_tv = TVset(name_tv)
    
    hello(my_tv)

    choise = None
    while choise != "0":
        print \
        """
        Какие настройки желаете изменить:
            1- Номер канала
            2 - Уровень громкости
            3 - Оставить без изменений
            0 - Выход
        """
        choise = raw_input("Ваш выбор: ")
        if  choise == "0":
            print "До новых встреч"
        elif choise == "1":
            my_tv.chenal = int(raw_input("Введите номер канала от 0 до 24: "))
            hello(my_tv)
        elif choise == "2":
            my_tv.volume = int(raw_input("Введите уровень громкости от 0 до 24: "))
            hello(my_tv)
        elif choise == "3":
            print "Как скажите"
            hello(my_tv)
        else:
            print "Нет такого пункта в меню", choise




main()
raw_input("\n\nНажмите Enter, чтобы выйти.")




