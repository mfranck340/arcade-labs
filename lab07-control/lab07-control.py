""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def draw_fondo():
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


class Coche():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def draw(self):
        "Dibuja un coche"
        arcade.draw_rectangle_outline(-21 + self.x, -6 + self.y, 15, 10, arcade.color.BLACK, 5)
        arcade.draw_rectangle_outline(25 + self.x, -6 + self.y, 20, 10, arcade.color.BLACK, 5)
        arcade.draw_rectangle_filled(self.x, self.y, 40, 25, self.color)
        arcade.draw_rectangle_outline(self.x, self.y, 40, 25, arcade.color.BLACK, 2)
        arcade.draw_rectangle_filled(-21 + self.x, -6 + self.y, 15, 10, self.color)
        arcade.draw_rectangle_filled(25 + self.x, -6 + self.y, 20, 10, self.color)
        # Ruedas
        arcade.draw_circle_filled(-15 + self.x, -13 + self.y, 10, arcade.color.APPLE_GREEN)
        arcade.draw_circle_filled(20 + self.x, -13 + self.y, 10, arcade.color.APPLE_GREEN)
        arcade.draw_circle_filled(-15 + self.x, -13 + self.y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(20 + self.x, -13 + self.y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(-15 + self.x, -13 + self.y, 4, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(20 + self.x, -13 + self.y, 4, arcade.color.HONEYDEW)
        # Ventanas
        arcade.draw_rectangle_filled(10 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(10 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK, 2)
        arcade.draw_rectangle_filled(-9 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(-9 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK, 2)


class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        self.set_mouse_visible(False)

        self.coche = Coche(400, 300, arcade.color.BANANA_YELLOW)

    def on_draw(self):
        arcade.start_render()
        draw_fondo()
        self.coche.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.coche.x = x
        self.coche.y = y


def main():
    window = MyGame()
    arcade.run()


main()