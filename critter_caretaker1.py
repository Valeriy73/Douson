# -*- encoding: utf-8 -*-

# Моя Зверюшка
# Виртуальный питомец, о котором пользователь может заботиться


class Critter(object):
    """Виртуальный питомец"""
    def __init__(self, name, hunger=0, boredom=0):
        print "Появилась на свет новая зверюшка!"
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

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

    def __eat_col(self):
        col_crecer = 0
        while not (0 < col_crecer < 5):
            col_crecer = int (raw_input("Сколько печенюшек вы хотите дать (от 1 до 4)?:"))
            if col_crecer < 1:
                print "Ты жадина!!!"
            elif col_crecer >4:
                print "Я столько не съем!!!"
        return col_crecer

    def eat(self):
        food = self.__eat_col()
        print "Мрр... Спасибо!"
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time

    def play_time(self):
        time = 0
        while not (0 < time < 5):
            time = int (raw_input("Сколько минут ты со мной поиграешь (от 1 до 4)?: "))
            if time < 1:
                print "Ты не хочешь со мной играть?"
            elif time > 4:
                print "{name} устал, я не могу так долго играть".format (name = self.name)
        return time

    def play(self):
        fun = self.play_time()
        print "Уиии!"
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time


def main():
    crit_name = raw_input("Как вы назовете свою зверушку? ")
    crit = Critter(crit_name)

    choice = None
    while choice != "0":
        print \
        """
        Моя зверюшка
        0 - Выйти
        1 - Узнать о самочувствии зверюшки
        2 - Покормить зверюшку
        3 - Поиграть со зверюшкой
        """
        choice = raw_input("Ваш выбор: ")
        print
        # выход
        if choice == "0":
            print "До свидания."
        # беседа со зверюшкой
        elif choice == "1":
            crit.talk()
        # Кормление зверюшки
        elif choice == "2":
            crit.eat()
        # игра со зверюшкой
        elif choice == "3":
            crit.play()
        # непонятный пользовательский ввод
        else:
            print "Извините, в меню нет пункта", choice

main()

raw_input("\n\nНажмите Enter, чтобы выйти.")
