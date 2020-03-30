""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 7

def draw_fondo():
    """Dibuja el fondo"""
    arcade.draw_rectangle_filled(400, 300, 530, 85, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(490, 430, 80, 185, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(310, 170, 80, 185, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(630, 150, 80, 385, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(170, 450, 80, 385, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(640, 480, 380, 85, arcade.color.OUTER_SPACE)
    arcade.draw_rectangle_filled(160, 120, 380, 85, arcade.color.OUTER_SPACE)


class Coche():
    def __init__(self, x, y, change_x, change_y, color):
        self.x = x
        self.y = y
        self.change_x = change_x
        self.change_y = change_y
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
        arcade.draw_circle_filled(-15 + self.x, -13 + self.y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(20 + self.x, -13 + self.y, 9, arcade.color.BLACK)
        arcade.draw_circle_filled(-15 + self.x, -13 + self.y, 4, arcade.color.HONEYDEW)
        arcade.draw_circle_filled(20 + self.x, -13 + self.y, 4, arcade.color.HONEYDEW)
        # Ventanas
        arcade.draw_rectangle_filled(10 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(10 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK, 2)
        arcade.draw_rectangle_filled(-9 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK_LEATHER_JACKET)
        arcade.draw_rectangle_outline(-9 + self.x, 5 + self.y, 15, 7, arcade.color.BLACK, 2)

    def update(self):
        # Move the ball
        self.y += self.change_y
        self.x += self.change_x

        if self.x < 25:
            self.x = 25
        if self.x > SCREEN_WIDTH - 25:
            self.x = SCREEN_WIDTH - 25
        if self.y < 15:
            self.y = 15
        if self.y > SCREEN_HEIGHT - 15:
            self.y = SCREEN_HEIGHT - 15


class MyGame(arcade.Window):
    """ Our Custom Window Class"""
    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")

        arcade.set_background_color(arcade.color.APPLE_GREEN)

        self.set_mouse_visible(False)

        self.coche = Coche(400, 300, 0, 0, arcade.color.BANANA_YELLOW)

    def on_draw(self):
        arcade.start_render()
        draw_fondo()
        self.coche.draw()

    def update(self, delta_time):
        self.coche.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.coche.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.coche.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.coche.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.coche.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.coche.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.coche.change_y = 0


def main():
    window = MyGame()
    arcade.run()


main()