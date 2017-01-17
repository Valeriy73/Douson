# Паника в пиццерии
# Игрок должен ловить падающую пиццу, пока она не достигла земли
from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)


class Pan(games.Sprite):
    """ Сковорода, в которую игрок может ловить падающую пиццу. """
    image = games.load_image("images/pan.bmp")
    score_gen = 0

    def __init__(self):
        """ Инициализирует объект Pan и создает объект Text для отображения
        счета. """
        super(Pan, self).__init__(image=Pan.image,
                                  x=games.mouse.x,
                                  bottom=games.screen.height)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=5, right=games.screen.width-10)

        games.screen.add(self.score)

    def update(self):
        """ Передвигает объект по горизонтали в точку с абсциссой, как у указателя
        мыши. """
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        """ Проверяет, поймал ли игрок падающую пиццу. """
        for pizza in self.overlapping_sprites:
            self.score.value += 10
            if self.bottom > games.screen.height*0.7:
                self.bottom = games.screen.height - self.score.value//100*10
            else:
                self.bottom = games.screen.height*0.7
            if not self.score.value%500:
                chef1 = Chef()
                games.screen.add(chef1)

            Pan.score_gen = self.score.value
            self.score.right = games.screen.width - 10
            pizza.handle_caught()


class Pizza(games.Sprite):
    """ Круги пиццы, падающие на землю. """
    image = games.load_image("images/pizza.bmp")
    speed = 1

    def __init__(self, x, y=90, add_speed=0):
        """ Инициализирует объекта Pizza. """
        super(Pizza, self).__init__(image=Pizza.image,
                                    x=x, y=y,
                                    dy=Pizza.speed + add_speed)


    def update(self):
        """ Провкряет, не коснулась ли нижняя кромка спрайта нижней границы эк-
        рана. """
        if self.bottom > games.screen.height:

            self.end_game()
            self.destroy()

    def handle_caught(self):
        """ Разрушает объект, пойманый игроком. """
        self.destroy()

    def end_game(self):
        """ Завершает игру. """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    lifetime=5*games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Chef(games.Sprite):
    """ Кулинар, который, двигаясь влево-вправо, разбрасывает пиццу. """
    image = games.load_image("images/chef.bmp")

    def __init__(self, y=55, speed=2, odds_change=200):
        """ Инициализирует объект Chef. """
        super(Chef, self).__init__(image=Chef.image,
                                   x=games.screen.width/2,
                                   y=y,
                                   dx=speed)
        self.odds_change = odds_change
        self.time_til_drop = 0


    def update(self):
        """ Определяет, надо ли сменить направление. """
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx
        self.check_drop()

    def check_drop(self):
        """ Уменьшает интервал ожидания на единицу или сбрасывает очередную пиццу
         и восстанавливает исходный интервал. """
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            add_speed = (Pan.score_gen//100)/10
            new_pizza = Pizza(x=self.x, add_speed=add_speed)
            games.screen.add(new_pizza)
        # вне зависимости от скорости падения пиццы "зазор" между падающими кругами
        #  принимается равным 30% каждого из них по высоте
            self.time_til_drop = int(new_pizza.height*1.3/Pizza.speed) + 1


def main():
    """ Собственно игровой процесс. """
    wall_image = games.load_image("images/wall.jpg", transparent=False)
    games.screen.background = wall_image
    the_chef = Chef()
    games.screen.add(the_chef)
    the_pan = Pan()
    the_pan.bottom
    games.screen.add(the_pan)
    games.mouse.is_visible = False
    games.screen.event_grab = True
    games.screen.mainloop()

# поехали
main()
