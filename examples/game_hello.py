"""
Simplest example of the proposed Game API
"""

from arcade import Game
from arcade.color import BLUE_GREEN


class MyGame(Game):
    def __init__(self, width, height):
        super().__init__(width=width, height=height)

    def on_draw(self):
        self.draw_text("Hello", 300, 200, BLUE_GREEN, 20)


if __name__ == '__main__':
    game = MyGame(700, 600)
    game.run()
