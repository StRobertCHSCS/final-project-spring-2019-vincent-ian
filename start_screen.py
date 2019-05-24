import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Text:
    def __init__(self, text, x_pos, y_pos, size):
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.size = size

    def draw_text(self):
        arcade.draw_text(self.text, self.x_pos, self.y_pos, arcade.color.BLACK, self.size)


class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Start Screen")

    def setup(self):
        pass

    def on_draw(self):
        arcade.start_render()

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, arcade.color.WHITE)


def main():
    window = MyGame()
    # window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
