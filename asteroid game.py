import arcade
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

SPRITE_SCALING_ASTEROID = 0.1

LEVEL_1_ASTEROID_COUNT = 5
LEVEL_2_ASTEROID_COUNT = 10
LEVEL_3_ASTEROID_COUNT = 15
LEVEL_4_ASTEROID_COUNT = 20
LEVEL_5_ASTEROID_COUNT = 25


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

        if self.center_x > 800 or self.center_x < 0 or self.center_y > 600 or self.center_y < 0:
            self.kill()


class ShipSprite(arcade.Sprite):

    def __init__(self, filename, scale):
        super().__init__(filename, scale)

        self.center_x = 0
        self.center_y = 0
        self.speed = 0
        self.lives = 3
        self.score = 0

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

        self.player_list = None
        self.player_sprite = None
        self.bullet_list = None
        self.bullet_sprite = None
        self.play_size = 20
        self.instructions_size = 20

        self.start = False
        self.background = arcade.load_texture("images/space.jpg")

        self.game_level = 1

        # Sprite lists
        self.level_1_asteroid_list = None
        self.level_2_asteroid_list = None
        self.level_3_asteroid_list = None
        self.level_4_asteroid_list = None
        self.level_5_asteroid_list = None

        # Set up background information
        self.background = None
        self.background = arcade.load_texture("images/space.jpg")

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.player_sprite = ShipSprite(r'images/plane.png', 0.075)
        self.player_sprite.center_x = 400
        self.player_sprite.center_y = 300
        self.player_list.append(self.player_sprite)

        self.bullet_list = arcade.SpriteList()

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

        # Start Screen
        arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                     arcade.color.WHITE)

        # Title
        arcade.draw_text("Asteroid Shooter", 250, 500, arcade.color.BLACK, 30)

        # Play button
        arcade.draw_rectangle_outline(400, 210, 250, 50, arcade.color.BLACK)
        arcade.draw_text("Press SPACE to start", 300, 200, arcade.color.BLACK, self.play_size)

        # Instructions button
        arcade.draw_rectangle_outline(400, 150, 200, 50, arcade.color.BLACK)
        arcade.draw_text("Instructions", 320, 140, arcade.color.BLACK, self.instructions_size)

        # Game Run
        if self.start:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)
            self.player_list.draw()
            self.bullet_list.draw()

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

        score = f"Score: {self.player_sprite.score}"
        arcade.draw_text(score, 10, 20, arcade.color.WHITE, 14)

        life = f"Lives: {self.player_sprite.lives}"
        arcade.draw_text(life, 10, 40, arcade.color.WHITE, 14)

        # Game Over Screen
        if self.player_sprite.lives == 0 or len(self.level_1_asteroid_list) == 0:
            arcade.draw_rectangle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE)
            arcade.draw_text("Game Over", 300, 500, arcade.color.BLACK, 30)

    def on_key_press(self, key, modifiers):
        # User Control with arrow keys

        if key == arcade.key.SPACE and not self.start:
            self.start = True
        elif key == arcade.key.SPACE and self.start:
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

        for good in self.bullet_list:
            good_hit = arcade.check_for_collision_with_list(good, self.level_1_asteroid_list)
            for asteroids in good_hit:
                asteroids.kill()
                self.player_sprite.score += 50

        bad_hit = arcade.check_for_collision_with_list(self.player_sprite, self.level_1_asteroid_list)
        for bad in bad_hit:
            bad.kill()
            self.player_sprite.lives -= 1

        for bad in self.level_1_asteroid_list:
            collisions_bad = arcade.check_for_collision_with_list(bad, self.level_1_asteroid_list)
            for collides_bad in collisions_bad:
                bad.top = collides_bad.bottom
                bad.bottom = collides_bad.top


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
