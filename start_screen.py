import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Start Screen")

        self.play_size = 20
        self.instructions_size = 20

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE)

        # Title
        arcade.draw_text("Asteroid Shooter", 250, 500, arcade.color.BLACK, 30)

        # Play button
        arcade.draw_rectangle_outline(400, 210, 100, 50, arcade.color.BLACK)
        arcade.draw_text("Play", 370, 200, arcade.color.BLACK, self.play_size)

        # Instructions button
        arcade.draw_rectangle_outline(400, 150, 200, 50, arcade.color.BLACK)
        arcade.draw_text("Instructions", 320, 140, arcade.color.BLACK, self.instructions_size)

    def on_mouse_motion(self, x, y, dx, dy):
        if x >= 350 and x <= 450 and y >= 185 and y <= 235:
            print("play")

def main():
    window = MyGame()
    # window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
