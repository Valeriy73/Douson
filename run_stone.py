# камни с неба
# необходимо уварачиваться от камней
from livewires import games, color
import random


games.init(screen_width=640, screen_height=480, fps=50)


class Cat(games.Sprite):
    """Бегающий кот"""
    image_cat_r = games.load_image("images/cat_right.bmp")
    image_cat_l = games.load_image("images/cat_left.bmp")

    def __init__(self):
        super(Cat, self).__init__(image=Cat.image_cat_r, x=320, y=400, dx=1)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width

        self.tach_dog()
        """
        if self.x > games.screen.width:
            self.image = Cat.image_cat_l
            self.dx = -self.dx
        elif self.x < 0:
            self.image = Cat.image_cat_r
            self.dx = -self.dx"""

    def tach_dog(self):
        """ Проверяет, упала ли собака на кота. """
        for dog in self.overlapping_sprites:
            dog.handle_caught()
            self.end_game()

    def end_game(self):
        """ Завершает игру. """
        end_message = games.Message(value="Game Over",
                                    size=90,
                                    color=color.red,
                                    x=games.screen.width / 2,
                                    y=games.screen.height / 2,
                                    lifetime=5 * games.screen.fps,
                                    after_death=games.screen.quit)
        games.screen.add(end_message)


class Dog(games.Sprite):
    """Падающая собака"""
    image_dog = games.load_image("images/dog.bmp")

    def __init__(self):
        self.start_x = random.randrange(0, games.screen.width)
        super(Dog, self).__init__(image=Dog.image_dog, x=self.start_x, y=40, dy=1)

    def update(self):
        pass

    def handle_caught(self):
        self.destroy()


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
    wall_image = games.load_image("images/bg_stone.jpg", transparent=False)
    games.screen.background = wall_image
    the_cat = Cat()
    games.screen.add(the_cat)
    the_dog = Dog()
    games.screen.add(the_dog)
    the_drop_dog = DropDog()
    games.screen.add(the_drop_dog)

    games.screen.mainloop()

# запуск игры
main()