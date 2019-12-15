"""
Name: asteroid game.py
Purpose:
To create a 2D space game with the objective to destroy asteroids and beat all the levels.

Authors: Yang.V, Lin.I

Created: 06/13/2019
"""

import arcade
import math
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

LEVEL_1_ASTEROID_COUNT = 5
LEVEL_2_ASTEROID_COUNT = 10
LEVEL_3_ASTEROID_COUNT = 15
LEVEL_4_ASTEROID_COUNT = 20
LEVEL_5_ASTEROID_COUNT = 25


class Bullets(arcade.Sprite):
    """
    Sprite to model the bullets
    """

    def __init__(self, filename, scale):
        """
        Initializes bullet values

        :param filename: Name of the file
        :param scale: Scale of game
        :return: None
        """

        super().__init__(filename, scale)
        self.speed = 0
        self.center_x = 0
        self.center_y = 0
        self.laser = arcade.load_sound(r"images/laser.mp3")
        self.explode = arcade.load_sound(r"images/explode.mp3")

    def update(self):
        """
        Updates the bullets across the screen
        :return: None
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Angle matches the direction of the ship movement
        self.angle = math.degrees(math.atan2(self.change_y, self.change_x))
        super().update()

        # Kill the bullet if it leaves the screen
        if self.center_x > 800 or self.center_x < 0 or self.center_y > 600 or self.center_y < 0:
            self.kill()

    def collision(self, asteroid_list, player_obj):
        """
        Check for collision between the bullet and the asteroid
        :param asteroid_list: list of asteroid sprites
        :param player_obj: instance of a ship sprite
        :return: None
        """
        # Check for collision between bullets and asteroid
        asteroid_shot_list = arcade.check_for_collision_with_list(self, asteroid_list)
        for asteroid in asteroid_shot_list:
            asteroid.kill()
            player_obj.score += 1
            self.explosion()

    def shooting_sound(self):
        """
        Play sound when bullet is shot
        :return: None
        """
        arcade.play_sound(self.laser)

    def explosion(self):
        """
        Play sound when bullet hits an asteroid
        :return: None
        """
        arcade.play_sound(self.explode)


class ShipSprite(arcade.Sprite):
    """
    Sprite to model the character/ ship
    """

    def __init__(self, filename, scale):
        """
        Initializes ship values

        :param filename: Name of the file
        :param scale: Scale of game
        :return: None
        """

        super().__init__(filename, scale)

        self.center_x = 400
        self.center_y = 300
        self.speed = 0
        self.lives = 3
        self.score = 0
        self.explode = arcade.load_sound(r"images/explode.mp3")

    def update(self):
        """
        Updates the user control movements
        :return: None
        """

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

    def center_ship(self):
        """
        Reset the location of the ship
        :return: None
        """
        self.center_x = 400
        self.center_y = 300
        self.angle = 0

    def collision(self, asteroid_list, ship_life_list):
        """
        Check for collision between the ship sprite and asteroid sprites
        :param asteroid_list: list asteroid sprites
        :param ship_life_list: list of ship sprites that show the number of lives left
        :return: None
        """
        # Check for collision between player and asteroid
        hit_list = arcade.check_for_collision_with_list(self, asteroid_list)
        for asteroid in hit_list:
            asteroid.kill()
            self.lives -= 1
            ship_life_list.pop().kill()
            self.explosion()

    def explosion(self):
        """
        Play sound when asteroid hits ship sprite
        :return: None
        """
        arcade.play_sound(self.explode)


class Asteroid(arcade.Sprite):
    """
    Sprite to model the asteroids
    """

    def __init__(self):
        """
        Initializes asteroid values
        :return: None
        """

        super().__init__("images/asteroid.png", 0.1)

    def update(self):
        """
        Updates the asteroid movements
        :return: None
        """

        self.center_x += self.change_x
        self.center_y += self.change_y

        # Move asteroids back to the middle if it leaves the screen
        if self.center_x < 0:
            self.center_x = SCREEN_WIDTH
        if self.center_x > SCREEN_WIDTH:
            self.center_x = 0
        if self.center_y < 0:
            self.center_y = SCREEN_HEIGHT
        if self.center_y > SCREEN_HEIGHT:
            self.center_y = 0


class HomeScreen:
    """
    Models the menu screen
    """

    def __init__(self):
        """
        Initiate menu values
        :return: None
        """

        self.menu = True
        self.home_screen_background = arcade.load_texture("images/galaxy.jpg")

    def draw(self):
        """
        Draw the menu items
        :return: None
        """
        # Start Screen
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.home_screen_background)

        # Title
        arcade.draw_text("Asteroid Shooter", 400, 500, arcade.color.WHITE, 30,
                         width=500, align="center", anchor_x="center", anchor_y="center")

        # Play button
        arcade.draw_rectangle_outline(400, 200, 250, 50, arcade.color.WHITE)
        arcade.draw_text("Press SPACE to start", 400, 200, arcade.color.WHITE, 20,
                         width=300, align="center", anchor_x="center", anchor_y="center")

        # Instructions button
        arcade.draw_rectangle_outline(400, 140, 200, 50, arcade.color.WHITE)
        arcade.draw_text("Press I for Instructions", 400, 140, arcade.color.WHITE, 15,
                         width=300, align="center", anchor_x="center", anchor_y="center")


class InstructionsScreen:
    """
    Models instructions menu
    """

    def __init__(self):

        """
        Initiate instructions menu values
        :return: None
        """

        self.instructions = False
        self.home_screen_background = arcade.load_texture("images/galaxy.jpg")

    def draw(self):

        """
        Draw instruction menu items
        :return: None
        """

        # Instructions screen
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                      self.home_screen_background)

        # All controls
        arcade.draw_text("Instructions", 400, 500, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Up", 200, 450, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Up Arrow", 600, 450, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Down", 200, 400, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Down Arrow", 600, 400, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Turn Left", 200, 350, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Left Arrow", 600, 350, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Turn Right", 200, 300, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Right Arrow", 600, 300, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Shoot", 200, 250, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Space", 600, 250, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")
        arcade.draw_text("Press M to go back", 400, 100, arcade.color.WHITE, 30,
                         width=300, align="center", anchor_x="center", anchor_y="center")


class MyGame(arcade.Window):
    """
    Full game mechanics
    """

    def __init__(self):
        """
        Initiate game values
        :return: None
        """

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Asteroid Game")

        # Player variables
        self.player_list = None
        self.ship_life_list = None
        self.player_sprite = None
        self.player_high_score = 0

        # Bullet variables
        self.bullet_list = None
        self.bullet_sprite = None

        # Screen information
        self.menu = HomeScreen()
        self.instructions = InstructionsScreen()
        self.play_game = None

        # Game level
        self.game_level = None

        # Show game level
        self.show_level_1 = None
        self.show_level_2 = None
        self.show_level_3 = None
        self.show_level_4 = None
        self.show_level_5 = None

        # Sprite lists
        self.level_1_asteroid_list = None
        self.level_2_asteroid_list = None
        self.level_3_asteroid_list = None
        self.level_4_asteroid_list = None
        self.level_5_asteroid_list = None

        # Set up background information
        self.game_background = arcade.load_texture("images/space.jpg")
        self.game_over_screen = arcade.load_texture("images/game over screen.jpg")
        self.win_screen = arcade.load_texture("images/win screen.jpg")

    def setup(self):
        """
        Setup for the game
        :return: None
        """

        # Setup player information
        self.player_list = arcade.SpriteList()
        self.player_sprite = ShipSprite(r'images/plane.png', 0.075)
        self.player_list.append(self.player_sprite)

        # Set up bullet information
        self.bullet_list = arcade.SpriteList()

        # Game information
        self.play_game = False

        # Setup game level
        self.game_level = 1

        # Set up showing level screen
        self.show_level_1 = True
        self.show_level_2 = True
        self.show_level_3 = True
        self.show_level_4 = True
        self.show_level_5 = True

        # Lives list
        position = 0
        self.ship_life_list = arcade.SpriteList()

        for i in range(self.player_sprite.lives):
            life = arcade.Sprite(r"images/plane.png", 0.05)
            life.center_x = position + life.width
            life.center_y = life.height
            position += life.width
            self.ship_life_list.append(life)

        # Create level 1 asteroid list
        self.level_1_asteroid_list = arcade.SpriteList()
        self.setup_asteroids(self.level_1_asteroid_list, LEVEL_1_ASTEROID_COUNT)

        # Create level 2 asteroid list
        self.level_2_asteroid_list = arcade.SpriteList()
        self.setup_asteroids(self.level_2_asteroid_list, LEVEL_2_ASTEROID_COUNT)

        # Create level 3 asteroid list
        self.level_3_asteroid_list = arcade.SpriteList()
        self.setup_asteroids(self.level_3_asteroid_list, LEVEL_3_ASTEROID_COUNT)

        # Create level 4 sprite list
        self.level_4_asteroid_list = arcade.SpriteList()
        self.setup_asteroids(self.level_4_asteroid_list, LEVEL_4_ASTEROID_COUNT)

        # Create level 5 sprite list
        self.level_5_asteroid_list = arcade.SpriteList()
        self.setup_asteroids(self.level_5_asteroid_list, LEVEL_5_ASTEROID_COUNT)

    def on_draw(self):
        """
        Draw asteroid shooting game
        :return: None
        """

        arcade.start_render()

        # Home Screen
        if self.menu.menu:
            self.menu.draw()

        # Instructions Menu
        if self.instructions.instructions:
            self.instructions.draw()

        # Game Run
        if self.play_game:
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.game_background)
            self.player_list.draw()
            self.bullet_list.draw()

            # Draw asteroids
            if self.game_level == 1 and not self.show_level_1:
                self.level_1_asteroid_list.draw()
            elif self.game_level == 2 and not self.show_level_2:
                self.level_2_asteroid_list.draw()
            elif self.game_level == 3 and not self.show_level_3:
                self.level_3_asteroid_list.draw()
            elif self.game_level == 4 and not self.show_level_4:
                self.level_4_asteroid_list.draw()
            elif self.game_level == 5 and not self.show_level_5:
                self.level_5_asteroid_list.draw()

            # Show level
            level = f"Level: {self.game_level}"
            arcade.draw_text(level, 10, 75, arcade.color.WHITE, 14,
                             width=300, align="left", anchor_x="left", anchor_y="center")

            # Show score
            score = f"Score: {self.player_sprite.score}"
            arcade.draw_text(score, 10, 55, arcade.color.WHITE, 14,
                             width=300, align="left", anchor_x="left", anchor_y="center")

            # Draw Lives List
            self.ship_life_list.draw()

            # Show the game level
            if self.show_level_1 and self.game_level == 1:
                arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.BLACK)
                arcade.draw_text("LEVEL 1", 400, 300, arcade.color.WHITE, 50,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
                arcade.draw_text("Press SPACE", 400, 150, arcade.color.WHITE, 20,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
            elif self.show_level_2 and self.game_level == 2:
                arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.BLACK)
                arcade.draw_text("LEVEL 2", 400, 300, arcade.color.WHITE, 50,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
                arcade.draw_text("Press SPACE", 400, 150, arcade.color.WHITE, 20,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
            elif self.show_level_3 and self.game_level == 3:
                arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.BLACK)
                arcade.draw_text("LEVEL 3", 400, 300, arcade.color.WHITE, 50,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
                arcade.draw_text("Press SPACE", 400, 150, arcade.color.WHITE, 20,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
            elif self.show_level_4 and self.game_level == 4:
                arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.BLACK)
                arcade.draw_text("LEVEL 4", 400, 300, arcade.color.WHITE, 50,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
                arcade.draw_text("Press SPACE", 400, 150, arcade.color.WHITE, 20,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
            elif self.show_level_5 and self.game_level == 5:
                arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.BLACK)
                arcade.draw_text("LEVEL 5", 400, 300, arcade.color.WHITE, 50,
                                 width=300, align="center", anchor_x="center", anchor_y="center")
                arcade.draw_text("Press SPACE", 400, 150, arcade.color.WHITE, 20,
                                 width=300, align="center", anchor_x="center", anchor_y="center")

        # Game Over Screen
        if self.player_sprite.lives == 0:
            if self.player_sprite.score > self.player_high_score:
                self.player_high_score = self.player_sprite.score
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.game_over_screen)
            arcade.draw_text("Score: " + str(self.player_sprite.score), 400, 150, arcade.color.WHITE, 30,
                             width=300, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text("High Score: " + str(self.player_high_score), 400, 100, arcade.color.WHITE, 15,
                             width=300, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text("Press Space to Restart", 400, 45, arcade.color.WHITE, 30,
                             width=500, align="center", anchor_x="center", anchor_y="center")

        # Win Screen
        elif len(self.level_5_asteroid_list) == 0:
            if self.player_sprite.lives == 0:
                if self.player_sprite.score > self.player_high_score:
                    self.player_high_score = self.player_sprite.score
            arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT,
                                          self.win_screen)
            arcade.draw_text("Score: " + str(self.player_sprite.score), 400, 140, arcade.color.WHITE, 30,
                             width=300, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text("High Score: " + str(self.player_high_score), 400, 100, arcade.color.WHITE, 15,
                             width=300, align="center", anchor_x="center", anchor_y="center")
            arcade.draw_text("Press Space to Restart", 400, 45, arcade.color.WHITE, 30,
                             width=500, align="center", anchor_x="center", anchor_y="center")

    def on_key_press(self, key, modifiers):
        """
        User control from keyboard
        :param key: Key pressed
        :param modifiers: Modifying press
        :return: None
        """

        # Commands for game
        if self.play_game:

            # Display level
            if self.show_level_1 and self.game_level == 1 and key == arcade.key.SPACE:
                self.show_level_1 = False
            elif self.show_level_2 and self.game_level == 2 and key == arcade.key.SPACE:
                self.show_level_2 = False
            elif self.show_level_3 and self.game_level == 3 and key == arcade.key.SPACE:
                self.show_level_3 = False
            elif self.show_level_4 and self.game_level == 4 and key == arcade.key.SPACE:
                self.show_level_4 = False
            elif self.show_level_5 and self.game_level == 5 and key == arcade.key.SPACE:
                self.show_level_5 = False

            # Player movement
            elif key == arcade.key.LEFT:
                self.player_sprite.change_angle = 5
            elif key == arcade.key.RIGHT:
                self.player_sprite.change_angle = -5
            elif key == arcade.key.UP:
                self.player_sprite.speed = 5
            elif key == arcade.key.DOWN:
                self.player_sprite.speed = -5

            # Shoot lasers
            elif key == arcade.key.SPACE and self.player_sprite.lives != 0 and len(self.level_5_asteroid_list) != 0:
                self.bullet_sprite = Bullets(r'images/lazer.png', 0.25)
                self.bullet_sprite.center_x = self.player_sprite.center_x
                self.bullet_sprite.center_y = self.player_sprite.center_y
                self.bullet_sprite.change_y = math.cos(math.radians(self.player_sprite.angle)) * 13
                self.bullet_sprite.change_x = -math.sin(math.radians(self.player_sprite.angle)) * 13
                self.bullet_sprite.shooting_sound()
                self.bullet_list.append(self.bullet_sprite)

        # User navigation with keys
        if key == arcade.key.SPACE and not self.play_game:
            self.play_game = True
            self.menu.menu = False
            self.instructions.instructions = False
        elif key == arcade.key.I and self.menu.menu:
            self.instructions.instructions = True
            self.menu.menu = False
            self.play_game = False
        elif key == arcade.key.M and self.instructions.instructions:
            self.menu.menu = True
            self.play_game = False
            self.instructions.instructions = False

        # Reset game after player has lost or won
        if (self.player_sprite.lives == 0 or len(self.level_5_asteroid_list) == 0) and key == arcade.key.SPACE:
            self.reset()

    def on_key_release(self, key, modifiers):
        """
        User control from keyboard
        :param key: Key released
        :param modifiers: Modifying release
        :return: None
        """

        # Releasing of arrow keys
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_angle = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.speed = 0

    def update(self, x):
        """
        Update the positions of the sprites
        :return: None
        """

        if not self.show_level_1 and self.player_sprite.lives != 0:
            self.player_sprite.update()
            self.bullet_list.update()

            if self.game_level == 1 and not self.show_level_1:
                self.level_1_asteroid_list.update()

                # Check for any collisions
                self.player_sprite.collision(self.level_1_asteroid_list, self.ship_life_list)
                for bullet in self.bullet_list:
                    bullet.collision(self.level_1_asteroid_list, self.player_sprite)

                # Move onto next level if there are no more asteroids
                if len(self.level_1_asteroid_list) == 0:
                    self.game_level = 2
                    self.player_sprite.center_ship()

            elif self.game_level == 2 and not self.show_level_2:
                self.level_2_asteroid_list.update()

                # Check for any collisions
                self.player_sprite.collision(self.level_2_asteroid_list, self.ship_life_list)
                for bullet in self.bullet_list:
                    bullet.collision(self.level_2_asteroid_list, self.player_sprite)

                # Move onto next level if there are no more asteroids
                if len(self.level_2_asteroid_list) == 0:
                    self.game_level = 3
                    self.player_sprite.center_ship()

            elif self.game_level == 3 and not self.show_level_3:
                self.level_3_asteroid_list.update()

                # Check for any collisions
                self.player_sprite.collision(self.level_3_asteroid_list, self.ship_life_list)
                for bullet in self.bullet_list:
                    bullet.collision(self.level_3_asteroid_list, self.player_sprite)

                # Move onto next level if there are no more asteroids
                if len(self.level_3_asteroid_list) == 0:
                    self.game_level = 4
                    self.player_sprite.center_ship()

            elif self.game_level == 4 and not self.show_level_4:
                self.level_4_asteroid_list.update()

                # Check for any collisions
                self.player_sprite.collision(self.level_4_asteroid_list, self.ship_life_list)
                for bullet in self.bullet_list:
                    bullet.collision(self.level_4_asteroid_list, self.player_sprite)

                # Move onto next level if there are no more asteroids
                if len(self.level_4_asteroid_list) == 0:
                    self.game_level = 5
                    self.player_sprite.center_ship()

            elif self.game_level == 5 and not self.show_level_5:
                self.level_5_asteroid_list.update()

                # Check for any collisions
                self.player_sprite.collision(self.level_5_asteroid_list, self.ship_life_list)
                for bullet in self.bullet_list:
                    bullet.collision(self.level_5_asteroid_list, self.player_sprite)

    def setup_asteroids(self, asteroid_list, asteroid_count):
        """
        Set up the location and speed of the asteroids
        :param asteroid_list: list of asteroids in a level
        :param asteroid_count: number of asteroids to be in a level
        :return: None
        """

        for i in range(asteroid_count):
            # Create instance of an asteroid class
            asteroid = Asteroid()

            # Assign asteroid random x and y coordinates
            asteroid.center_x = random.randrange(SCREEN_WIDTH)
            asteroid.center_y = random.randrange(SCREEN_HEIGHT)

            # Reset asteroid coordinate until not inside player spawning area
            while 300 < asteroid.center_x < 500 and 200 < asteroid.center_y < 400:
                asteroid.center_x = random.randrange(SCREEN_WIDTH)
                asteroid.center_y = random.randrange(SCREEN_HEIGHT)

            # Assign asteroid an x and y speed
            asteroid.change_x = random.randrange(-5, 5)
            asteroid.change_y = random.randrange(-5, 5)

            # Add instance of the asteroid to the asteroid list
            asteroid_list.append(asteroid)

    def reset(self):
        """
        Reset game after player has won or lost
        :return: None
        """

        self.setup()
        self.player_sprite.center_ship()
        self.menu.menu = True
        self.instructions.instructions = False


def main():
    """
    Main function to run game
    :return: None
    """

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
