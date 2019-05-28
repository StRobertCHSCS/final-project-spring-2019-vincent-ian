import arcade
import random


# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_ASTEROID = 0.1

LEVEL_1_ASTEROID_COUNT = 5
LEVEL_2_ASTEROID_COUNT = 10
LEVEL_3_ASTEROID_COUNT = 15
LEVEL_4_ASTEROID_COUNT = 20
LEVEL_5_ASTEROID_COUNT = 25


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
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Asteroid Game")

        self.game_level = 1

        # Sprite lists
        self.level_1_asteroid_list = None
        self.level_2_asteroid_list = None
        self.level_3_asteroid_list = None
        self.level_4_asteroid_list = None
        self.level_5_asteroid_list = None

        # Set up background information
        self.background = None

        # Make the mouse not visible in the window
        self.set_mouse_visible(False)

    def setup(self):
        self.background = arcade.load_texture("images/space.jpg")

        # Create level 1 sprite list
        self.level_1_asteroid_list = arcade.SpriteList()

        for i in range(LEVEL_1_ASTEROID_COUNT):
            asteroid = ASTEROID("images/asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.level_1_asteroid_list.append(asteroid)

        # Create level 2 sprite list
        self.level_2_asteroid_list = arcade.SpriteList()

        for i in range(LEVEL_2_ASTEROID_COUNT):
            asteroid = ASTEROID("images/asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.level_2_asteroid_list.append(asteroid)

        # Create level 3 sprite list
        self.level_3_asteroid_list = arcade.SpriteList()

        for i in range(LEVEL_3_ASTEROID_COUNT):
            asteroid = ASTEROID("images/asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.level_3_asteroid_list.append(asteroid)

        # Create level 4 sprite list
        self.level_4_asteroid_list = arcade.SpriteList()

        for i in range(LEVEL_4_ASTEROID_COUNT):
            asteroid = ASTEROID("images/asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.level_4_asteroid_list.append(asteroid)

        # Create level 5 sprite list
        self.level_5_asteroid_list = arcade.SpriteList()

        for i in range(LEVEL_5_ASTEROID_COUNT):
            asteroid = ASTEROID("images/asteroid.png", SPRITE_SCALING_ASTEROID)

            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            self.level_5_asteroid_list.append(asteroid)

    def on_draw(self):
        arcade.start_render()

        # Draw background
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw asteroids
        if self.game_level == 1:
            self.level_1_asteroid_list.draw()
        elif self.game_level == 2:
            self.level_2_asteroid_list.draw()
        elif self.game_level == 3:
            self.level_3_asteroid_list.draw()
        elif self.game_level == 4:
            self.level_4_asteroid_list.draw()
        elif self.game_level == 5:
            self.level_5_asteroid_list.draw()

    def update(self, delta_time):
        if self.game_level == 1:
            self.level_1_asteroid_list.update()
        elif self.game_level == 2:
            self.level_2_asteroid_list.update()
        elif self.game_level == 3:
            self.level_3_asteroid_list.update()
        elif self.game_level == 4:
            self.level_4_asteroid_list.update()
        elif self.game_level == 5:
            self.level_5_asteroid_list.update()


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
