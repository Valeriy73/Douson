# Скачущая пицца
# Демонстрирует обработку столкновений с границами экрана
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)


class Pizza(games.Sprite):
    """ Скачущая пицца. """
    def update(self):
        """ Обращает одну или обе компоненты скорости, если достигнута граница
        экрана. """

        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy


def main():
    wall_image = games.load_image("images/wall.jpg", transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image("images/pizza.bmp")
    the_pizza = Pizza(image=pizza_image,
                      x=games.screen.width/2,
                      y=games.screen.height/2,
                      dx=1,
                      dy=1)
    games.screen.add(the_pizza)
    games.screen.mainloop()
# поехали
if __name__ == '__main__':
    main()
