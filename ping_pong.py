# Игра пинг-понг
# необходимо отбивать шарик
from livewires import games, color
import random


games.init(screen_width=640, screen_height=480, fps=50)


class Wall(games.Sprite):
    """Стены поля"""

    def __init__(self, image_wall, pos_x, pos_y):
        super(Wall, self).__init__(image=image_wall, x=pos_x, y=pos_y)

    def update(self):
        pass


class Ball(games.Sprite):
    """Мячик"""
    image_ball = games.load_image("images/ball.bmp")
    start_x = random.randrange(10, games.screen.width-10)
    count = 0
    def __init__(self):
        super(Ball, self).__init__(image=Ball.image_ball, x=Ball.start_x, y=40, dy=1, dx=1)
        self.score = games.Text(value=0, size=25, color=color.black,
                                top=40, right=games.screen.width - 50)
        games.screen.add(self.score)

    def update(self):
        Ball.count += 1
        self.score.value = self.dx
        if self.y > games.screen.height:
            self.game_over()
        if Ball.count > 200:
            self.dx *= 1.1
            self.dy *= 1.1
            Ball.count =0
        self.check_catch()

    def check_catch(self):
        """ Проверяет, соприкоснулся ли шарик. """
        for ball in self.overlapping_sprites:
            if self.dx > 0 and self.dy > 0:
                self.dx = -self.dx
            elif self.dx < 0 and self.dy > 0:
                self.dy = -self.dy
            elif self.dx < 0 and self.dy < 0:
                self.dx = -self.dx
            elif self.dx > 0 and self.dy < 0:
                self.dy = -self.dy

    def game_over(self):
        """ Завершает игру. """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Raketka(games.Sprite):
    """Ракетка"""
    image_raketka = games.load_image("images/raketka.bmp", transparent=False)

    def __init__(self):
        super(Raketka, self).__init__(image=Raketka.image_raketka, x=320, y=460)

    def update(self):
        self.x = games.mouse.x
        if self.left < 20:
            self.left = 20
        if self.right > 620:
            self.right = 620



class DropDog(games.Sprite):
    image_piksel = games.load_image("images/1piksel.bmp")

    def __init__(self, odd_change=200):
        self.odd_change = odd_change
        self.time_til_drop = 0
        super(DropDog, self).__init__(image=DropDog.image_piksel)

    def update(self):
        if self.time_til_drop > 0:
            self.time_til_drop -= 1
        else:
            new_dog = Dog()
            games.screen.add(new_dog)
            self.time_til_drop = self.odd_change

def main():
    # инициализация игры
    wall_image = games.load_image("images/field.jpg", transparent=False)
    games.screen.background = wall_image

    image_wall_lr = games.load_image("images/wall_l_r.bmp")
    image_wall_top = games.load_image("images/wall_top.bmp")
    the_wall_l = Wall(image_wall_lr, 10, 240)
    games.screen.add(the_wall_l)
    the_wall_r = Wall(image_wall_lr, 630, 240)
    games.screen.add(the_wall_r)
    the_wall_top = Wall(image_wall_top, 320, 10)
    games.screen.add(the_wall_top)

    the_ball = Ball()
    games.screen.add(the_ball)

    the_raketka = Raketka()
    games.screen.add(the_raketka)


    games.screen.mainloop()

# запуск игры
main()