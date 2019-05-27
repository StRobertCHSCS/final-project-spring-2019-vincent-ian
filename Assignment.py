import arcade
import random
import math

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Bullets(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)
        self.speed = 0
        self.center_x = 0
        self.center_y = 0

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
        super().update()


class ShipSprite(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        self.center_x = 0
        self.center_y = 0
        self.speed = 0

    def update(self):

        # See if the avatar hit the edge of the screen. If so, change direction
        if self.center_x < 25:
            self.center_x = 25

        if self.center_x > SCREEN_WIDTH - 25:
            self.center_x = SCREEN_WIDTH - 25

        if self.center_y < 25:
            self.center_y = 25

        if self.center_y > SCREEN_HEIGHT - 25:
            self.center_y = SCREEN_HEIGHT - 25

        # Move the avatar
        self.change_x = -math.sin(math.radians(self.angle)) * self.speed
        self.change_y = math.cos(math.radians(self.angle)) * self.speed
        self.center_x += self.change_x
        self.center_y += self.change_y
        super().update()


class MyGame(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        self.player_list = None
        self.player_sprite = None
        self.bullet_list = None
        self.bullet_sprite = None

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = ShipSprite(r'images/plane.png', 0.075)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        self.bullet_list = arcade.SpriteList()

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.bullet_list.draw()

    def on_key_press(self, key, modifiers):
        # User Control with arrow keys

        if key == arcade.key.SPACE:
            self.bullet_sprite = Bullets(r'images/lazer.png', 0.25)
            self.bullet_sprite.center_x = self.player_sprite.center_x
            self.bullet_sprite.center_y = self.player_sprite.center_y
            self.bullet_sprite.change_y = math.cos(math.radians(self.player_sprite.angle)) * 13
            self.bullet_sprite.change_x = -math.sin(math.radians(self.player_sprite.angle)) * 13
            self.bullet_list.append(self.bullet_sprite)

        if key == arcade.key.LEFT:
            self.player_sprite.change_angle = 3
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_angle = -3
        elif key == arcade.key.UP:
            self.player_sprite.speed = 5
        elif key == arcade.key.DOWN:
            self.player_sprite.speed = -5

    def on_key_release(self, key, modifiers):
        # Releasing of arrow keys
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0

    def update(self, x):
        self.player_sprite.update()
        self.bullet_list.update()


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Game")
    window.setup()
    arcade.run()

main()

