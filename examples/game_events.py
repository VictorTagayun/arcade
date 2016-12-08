"""
Event handling in the proposed Game API
"""

from arcade import Game
from arcade.color import BLUE_GREEN, GREEN, BLACK
from arcade.key import SPACE

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 600
BALL_RADIUS = 20


class MyGame(Game):
    def __init__(self, width, height, title):
        super().__init__(width=width, height=height)
        self.height = height
        self.width = width
        self.title = title
        self.set_background_color(BLUE_GREEN)
        self.ball_x_position = BALL_RADIUS
        self.velocity = 70

    def on_draw(self):
        self.draw_circle_filled(self.ball_x_position, self.height // 2,
                                BALL_RADIUS, GREEN)
        self.draw_text("Press space to reverse",
                       10, self.height // 4, BLACK, 20)

    def reverse(self):
        self.velocity *= -1

    def update_model(self, delta_time):
        # Move the ball
        self.ball_x_position += self.velocity * delta_time

        # Did the ball hit the right side of the screen while moving right?
        if self.ball_x_position > self.width - BALL_RADIUS \
                and self.velocity > 0:
            self.reverse()

        # Did the ball hit the left side of the screen while moving left?
        if self.ball_x_position < BALL_RADIUS \
                and self.velocity < 0:
            self.reverse()

    def on_key_press(self, key, key_modifiers):
        if key == SPACE:
            self.reverse()


if __name__ == '__main__':
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, 'My Game')
    game.run()
