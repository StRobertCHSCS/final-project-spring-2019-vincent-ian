import arcade
import random


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

ASTEROID_COUNT = 10
SPRITE_SCALING_ASTEROID = 0.1


class ASTEROID(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0


class MyGame(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab_08 - Sprites")

        # Sprite lists
        self.asteroid_list = None

        # Set up directions
        self.asteroid_change_x = None
        self.asteroid_change_y = None

        # Make the mouse not visible in the window
        self.set_mouse_visible(False)

        # Set up background information
        self.background = None

    def setup(self):
        self.background = arcade.load_texture("space.jpg")

        # Sprite lists
        self.asteroid_list = arcade.SpriteList()

        # Create asteroids
        for i in range(ASTEROID_COUNT):
            asteroid = ASTEROID("asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.asteroid_list.append(asteroid)

    def on_draw(self):
        arcade.start_render()

        # Draw background
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw asteroids
        self.asteroid_list.draw()

    def update(self, delta_time):
        self.asteroid_list.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
