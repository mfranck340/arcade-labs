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
        self.player = arcade.Sprite("Sprites/platformChar_idle.png", 0.75)
        self.max_good = 5
        self.good = arcade.SpriteList()
        self.max_bad = 5
        self.bad = arcade.SpriteList()

        self.sound_good = arcade.sound.load_sound("sounds/CARHORN.mp3")

        self.set_mouse_visible(False)

    def setup(self):
        for i in range(self.max_good):
            self.good.append(arcade.Sprite("Sprites/platformPack_item007.png", 0.5, center_x = randrange(SCREEN_WIDTH),
                             center_y = randrange(SCREEN_HEIGHT)))

        for i in range(self.max_bad):
            self.bad.append(arcade.Sprite("Sprites/platformPack_tile044.png", 0.5, center_x = randrange(SCREEN_WIDTH),
                             center_y = randrange(SCREEN_HEIGHT)))


    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.good.draw()
        self.bad.draw()


    #def on_update(self, delta_time):



    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """Player movement"""
        self.player.center_x = x
        self.player.center_y = y



def main():
    window = MyGame()
    window.setup()
    arcade.run()


main()