# -*- encoding: utf-8 -*-

# Моя Зверюшка
# Виртуальный питомец, о котором пользователь может заботиться
import random


class Critter(object):
    """Виртуальный питомец"""

    total = 0

    def __init__(self, name):
        print "Появилась на свет новая зверюшка!"
        self.name = name
        self.hunger = random.randint(0, 4)
        self.boredom = random.randint(0, 4)
        Critter.total += 1

    def __str__(self):
        info = "Объект класса Critter:\n"
        info += "Имя " + self.name + "\n"
        info += "Голод " + str(self.hunger) + "\n"
        info += "Настроение " + str(self.boredom) + "\n"
        info += "Всего зверушек" + str(Critter.total) + "\n"
        return info

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "прекрасно"
        elif 5 <= unhappiness <= 10:
            m = "неплохо"
        elif 11 <= unhappiness <= 15:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print "Меня зовут {0} и сейчас я чувствую себя {1}\n".format(self.name, self.mood)
        self.__pass_time()

    

    def eat(self, food):
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time

    

    def play(self, fun):
        
        
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time

def new_animals(number_animal, crit):
    crit_name = raw_input("Как вы назовете свою зверушку? ")
    crit.append(Critter(crit_name))
    number_animal += 1
    return number_animal, crit

def eat_col():
        col_crecer = 0
        while not (0 < col_crecer < 5):
            col_crecer = int (raw_input("Сколько печенюшек вы нам дадите (от 1 до 4)?:"))
            if col_crecer < 1:
                print "Ты жадина!!!"
            elif col_crecer >4:
                print "Мы столько не съедим!!!"
        print "Мрр... Спасибо!"
        return col_crecer

def play_time():
        time = 0
        while not (0 < time < 5):
            time = int (raw_input("Сколько минут ты будешь с нами грать (от 1 до 4)?: "))
            if time < 1:
                print "Ты не хочешь со мной играть?"
            elif time > 4:
                print "Мы устали и не можем так долго играть"
        print "Уиии!"
        return time

def main():
    crit = []
    new_animal = "y"
    number_animal = 0
    number_animal, crit = new_animals(number_animal, crit)
    while  new_animal == "y":
        add_animal = raw_input("Хотите создать еще одну зверушку (y/n)?")
        if add_animal == "y":
            number_animal, crit = new_animals(number_animal, crit)
        elif add_animal == "n":
            break
        else:
             add_animal = raw_input("Выберите y или n.")

    
    choice = None
    while choice != "0":
        print \
        """
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        4
        """
        choice = raw_input("Ваш выбор: ")
        print
        # выход
        if choice == "0":
            print "До свидания."
        # беседа со зверюшкой
        elif choice == "1":
            for zver in range(0, len(crit)):
                crit[zver].talk()
        # Кормление зверюшки
        elif choice == "2":
            food = eat_col()
            for zver in range(0, len(crit)):
                crit[zver].eat(food)
        # игра со зверюшкой
        elif choice == "3":
            fun = play_time()
            for zver in range(0, len(crit)):
                crit[zver].play(fun)
        # Секретная информация
        elif choice == "4":
            for zver in range(0, len(crit)):
                print crit[zver]
        # непонятный пользовательский ввод
        else:
            print "Извините, в меню нет пункта", choice

main()

raw_input("\n\nНажмите Enter, чтобы выйти.")
