""" Lab 8 - Sprites """

import arcade
from random import randrange

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 8 - Sprites")
        self.set_update_rate(1 / 60)
        self.player = arcade.Sprite("Sprites/platformChar_idle.png", 0.75)

        self.max_good = 10
        self.good = arcade.SpriteList()
        self.speed_good_x = []
        self.speed_good_y = []

        self.max_bad = 10
        self.bad = arcade.SpriteList()
        self.speed_bad_x = []
        self.speed_bad_y = []

        self.set_mouse_visible(False)

    def setup(self):
        for i in range(self.max_good):
            self.good.append(arcade.Sprite("Sprites/platformPack_item007.png", 0.5, center_x=randrange(SCREEN_WIDTH),
                                           center_y=randrange(SCREEN_HEIGHT)))
            self.speed_good_x.append(randrange(-5, 5, 1))
            self.speed_good_y.append(randrange(-5, 5, 1))

        for i in range(self.max_bad):
            self.bad.append(arcade.Sprite("Sprites/platformPack_tile044.png", 0.5, center_x=randrange(SCREEN_WIDTH),
                                          center_y=randrange(SCREEN_HEIGHT)))
            self.speed_bad_x.append(randrange(-5, 5, 1))
            self.speed_bad_y.append(randrange(-10, 10, 1))

    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.good.draw()
        self.bad.draw()

    def on_update(self, delta_time: float):
        self.move_objects(self.good, self.speed_good_x, self.speed_good_y)
        self.move_objects(self.bad, self.speed_bad_x, self.speed_bad_y)
        self.collision(self.good)
        self.collision(self.bad)

    def move_objects(self, list_objects: arcade.SpriteList, speed_x: list, speed_y: list):
        i = 0
        for elem in list_objects:
            elem.center_x += speed_x[i]
            elem.center_y += speed_y[i]

            if elem.center_x > SCREEN_WIDTH:
                elem.center_x = 0
            elif elem.center_x < 0:
                elem.center_x = SCREEN_WIDTH

            if elem.center_y > SCREEN_HEIGHT:
                elem.center_y = 0
            elif elem.center_y < 0:
                elem.center_y = SCREEN_HEIGHT

            i += 1

    def collision(self, list_objects: arcade.SpriteList):
        hit_list = arcade.check_for_collision_with_list(self.player, list_objects)
        for impact in hit_list:
            impact.center_x = randrange(SCREEN_WIDTH)
            impact.center_y = randrange(SCREEN_HEIGHT)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """Player movement"""
        self.player.center_x = x
        self.player.center_y = y


def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()