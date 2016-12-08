"""
Simplest example of the proposed Game API
"""

from arcade import Game
from arcade.color import BLUE_GREEN


class MyGame(Game):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        self.draw_text("Hello", 150, 200, BLUE_GREEN, 20)


if __name__ == '__main__':
    game = MyGame()
    game.run()
