# -*- encoding: utf-8 -*-

# Сумашедший сказочник
# Создает рассказ на основе пользовательского ввода
from Tkinter import *


class Application(Frame, object):
    """ GUI-приложение, создающее рассказ на основе пользовательского ввода. """
    def __init__(self, master):
        """ Инициализирует рамку. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Создает элементы управления, с помощьюкоторых пользователь будет вводить
        исходные данные и получать готовый рассказ. """

        # метка с текстом-инструкцией
        Label(self,
              text="Введите данные для создания нового рассказа"
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        # метка и поле ввода для имени человека
        Label(self,
              text="Имя человека: "
              ).grid(row=1, column=0, sticky=W)

        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        # метка и поле ввода для существительного
        Label(self,
              text="Существительное во мн. ч.:  "
              ).grid(row=2, column=0, sticky=W)

        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        # метка и поле ввода для глагола
        Label(self,
              text="Глагол в инфинитиве:  "
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        # метка при группе флажков с прилагательными
        Label(self,
              text="Прилагательоне (-ые):  "
              ).grid(row=4, column=0, sticky=W)

        # флажок со словом "нетерпеливый"
        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text="нетерпеливый",
                    variable=self.is_itchy
                    ).grid(row=4, column=1, sticky=W)

        # флажок со словом "радостный"
        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="радостный",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)

        # флажок со словом "пронизывающий"
        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="пронизывающий",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)

        # метка при переключателе с названиями частей тела
        Label(self,
              text="Body Part:  "
              ).grid(row=5, column=0, sticky=W)

        # переменная, содержащая название одной из частей тела
        self.body_part = StringVar()
        self.body_part.set(None)

        # переключатель с названиями частей тела
        body_parts = ["пупок", "большой палец ноги", "продолговатый мозг"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text=part,
                        variable=self.body_part,
                        value=part
                        ).grid(row=5, column=column, sticky=W)
            column += 1

        # кнопка отсылки данных
        Button(self,
               text="Получить рассказ",
               command=self.tell_story
               ).grid(row=6, column=0, sticky=W)
        self.story_txt = Text(self, width=75, height=10, wrap=WORD)
        self.story_txt.grid(row=7, column=0, columnspan=4)

    def tell_story(self):
        """ Заполняет текстовую область очередной историей на основе пользовательского
         ввода. """
        # get values from the GUI
        person = self.person_ent.get()
        noun = self.noun_ent.get()
        verb = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += u"нетерпеливое, "
        if self.is_joyous.get():
            adjectives += u"радостное, "
        if self.is_electric.get():
            adjectives += u"пронизывающее, "
        body_part = self.body_part.get()
        # создание рассказа
        story = u"Знаменитый путешествиник "
        story += person
        story += u" уже совсем отчаялся довершить дело всей своей жизни - поиск затерян-" \
                 u"ного города, в котором, по легенде, обитали "
        story += noun.title()
        story += u". Но однажды "
        story += noun
        story += u" и "
        story += person + u" столкнулись лицом к лицу. "
        story += u"Мощное,  "
        story += adjectives
        story += u"ни с чем не сравнимое чувство охватило душу путешественика. "
        story += u"После стольких лет поисков цель была наконец достигнута. "
        story += person
        story += u" ощутил, как на его " + body_part + u" скатилась слезинка. "
        story += u"И тут внезапно "
        story += noun
        story += u" перешли в атаку, и "
        story += person + u" был ими мгновено сожран. "
        story += u"Мораль? Если задумали "
        story += verb
        story += u", надо делать с осторожностью."
        # вывод рассказа на экран
        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)

# основная часть
root = Tk()
root.title("Сумасшедший сказочник")
app = Application(root)
root.mainloop()
