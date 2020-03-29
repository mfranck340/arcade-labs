""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class Coche():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        "Dibuja un coche"
        arcade.draw_rectangle_outline(379 + x, 294 + y, 15, 10, arcade.color.BLACK, 5)
        arcade.draw_rectangle_outline(425 + x, 294 + y, 20, 10, arcade.color.BLACK, 5)
        arcade.draw_rectangle_filled(400 + x, 300 + y, 40, 25, arcade.color.BYZANTINE)
        arcade.draw_rectangle_outline(400 + x, 300 + y, 40, 25, arcade.color.BLACK, 2)
        arcade.draw_rectangle_filled(379 + x, 294 + y, 15, 10, arcade.color.BYZANTINE)
        arcade.draw_rectangle_filled(425 + x, 294 + y, 20, 10, arcade.color.BYZANTINE)
        # Ruedas
        arcade.draw_circle_filled(385 + x, 287 + y, 10, arcade.color.GRAPE)
        arcade.draw_circle_filled(420 + x, 287 + y, 10, arcade.color.GRAPE)
        arcade.draw_circle_filled(385 + x, 287 + y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(420 + x, 287 + y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(385 + x, 287 + y, 4, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(420 + x, 287 + y, 4, arcade.color.HONEYDEW)
        # Ventanas
        arcade.draw_rectangle_filled(410 + x, 305 + y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(410 + x, 305 + y, 15, 7, arcade.color.BLACK, 2)
        arcade.draw_rectangle_filled(390 + x, 305 + y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(390 + x, 305 + y, 15, 7, arcade.color.BLACK, 2)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def draw_fondo(self):
        """Dibuja el fondo"""

        arcade.draw_rectangle_filled(400, 300, 800, 600, arcade.color.APPLE_GREEN)

        arcade.draw_rectangle_filled(400, 300, 580, 125, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(490, 430, 129, 200, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(311, 170, 129, 200, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(630, 150, 120, 400, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(170, 450, 120, 400, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(640, 480, 430, 115, arcade.color.TIMBERWOLF)
        arcade.draw_rectangle_filled(160, 120, 430, 115, arcade.color.TIMBERWOLF)

        arcade.draw_rectangle_filled(400, 300, 530, 85, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(490, 430, 80, 185, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(310, 170, 80, 185, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(630, 150, 80, 385, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(170, 450, 80, 385, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(640, 480, 380, 85, arcade.color.OUTER_SPACE)
        arcade.draw_rectangle_filled(160, 120, 380, 85, arcade.color.OUTER_SPACE)

    def __init__(self):
        """ Initializer """

        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

    def on_draw(self):
        arcade.start_render()
        draw_fondo()


def main():
    window = MyGame()
    arcade.run()


main()