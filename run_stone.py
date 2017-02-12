# камни с неба
# необходимо уварачиваться от камней
from livewires import games, color
import random


class Screen_game(games.Screen):
    """Экран игры"""
    bg_image = games.load_image("images/bg_stone.jpg", transparent=False)

    def __init__(self):
        super(Screen_game, self).__init__(width=640, height=480, fps=50)
        self.background = Screen_game.bg_image


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
        """
        if self.x > games.screen.width:
            self.image = Cat.image_cat_l
            self.dx = -self.dx
        elif self.x < 0:
            self.image = Cat.image_cat_r
            self.dx = -self.dx"""


class Dog(games.Sprite):
    """Падающая собака"""
    image_dog = games.load_image("images/dog.bmp")

    def __init__(self):
        self.start_x = random.randrange(0, games.screen.width)
        super(Dog, self).__init__(image=Dog.image_dog, x=self.start_x, y=40, dy=1)

    def update(self):
        pass

    

def main():
    # инициализация игры
    the_screen = Screen_game()
    the_cat = Cat()
    the_screen.add(the_cat)
    the_dog = Dog()
    the_screen.add(the_dog)
    the_screen.mainloop()

# запуск игры
main()