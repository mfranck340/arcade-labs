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
        arcade.set_background_color(arcade.color.DENIM)
        self.player = arcade.Sprite("Sprites/platformChar_idle.png", 0.75)
        self.score = 0
        self.num_life = 3
        self.life = arcade.Sprite("Sprites/platformPack_item017.png", 0.75, center_x=20, center_y=580)
        self.fin = False

        self.max_good = 10
        self.good = arcade.SpriteList()
        self.speed_good_x = []
        self.speed_good_y = []

        self.max_bad = 5
        self.bad = arcade.SpriteList()
        self.speed_bad_x = []
        self.speed_bad_y = []

        self.sound1 = arcade.sound.load_sound("Sounds/impactMining_003.ogg")
        self.sound2 = arcade.sound.load_sound("Sounds/impactWood_medium_004.ogg")

        self.set_mouse_visible(self.fin)

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
            self.speed_bad_y.append(randrange(-5, 5, 1))

    def on_draw(self):
        arcade.start_render()

        self.player.draw()
        self.good.draw()
        self.bad.draw()
        self.life.draw()
        arcade.draw_text(str(self.num_life), 35, 567, arcade.color.WHITE, 18)
        arcade.draw_text("Score: " + str(self.score), 0, 0, arcade.color.WHITE, 18)
        if self.num_life == 0:
            arcade.draw_text("GAME OVER", 280, 300, arcade.color.RED, 40)
            arcade.draw_text("Press ENTER to continue", 230, 250, arcade.color.RED, 28)

    def on_update(self, delta_time: float):
        if not self.fin:
            self.move_objects(self.good, self.speed_good_x, self.speed_good_y)
            self.move_objects(self.bad, self.speed_bad_x, self.speed_bad_y)
            self.collision(self.good, self.sound1, 1, 0)
            self.collision(self.bad, self.sound2, -10, -1)

    @staticmethod
    def move_objects(list_objects: arcade.SpriteList, speed_x: list, speed_y: list):
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

    def collision(self, list_objects: arcade.SpriteList, sound: arcade.sound, points: int, life: int):
        hit_list = arcade.check_for_collision_with_list(self.player, list_objects)
        for impact in hit_list:
            self.score += points
            self.num_life += life
            arcade.sound.play_sound(sound)
            impact.center_x = randrange(SCREEN_WIDTH)
            impact.center_y = randrange(SCREEN_HEIGHT)
        if self.num_life == 0:
            self.fin = True

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """Player movement"""
        if not self.fin:
            self.player.center_x = x
            self.player.center_y = y

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.ENTER and self.fin:
            self.fin = False
            self.num_life = 3
            self.score = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()