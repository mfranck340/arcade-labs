import arcade
def draw_fondo():
    """ Dibuja el fondo"""
    arcade.draw_lrtb_rectangle_filled(0, 1000, 450, 0, arcade.color.BITTER_LIME)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 0, arcade.color.DARTMOUTH_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 250, 0, arcade.color.DARK_GREEN)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 175, 0, arcade.color.AUROMETALSAURUS)
    arcade.draw_lrtb_rectangle_filled(0, 1000, 125, 0, arcade.color.APPLE_GREEN)

def draw_arbol_pequeño(x):
    "Dibujar árbol pequeño"
    arcade.draw_rectangle_filled(250 + x, 351, 35, 350, arcade.color.BLACK_BEAN)
    arcade.draw_circle_filled(255 + x, 450, 110, arcade.color.ENGLISH_GREEN)
    arcade.draw_circle_outline(255 + x, 450, 110, arcade.color.BLACK, 2)

def draw_arbol_grande(x):
    "Dibujar árbol grande"
    arcade.draw_rectangle_filled(50 + x, 426, 50, 500, arcade.color.BLACK_BEAN)
    arcade.draw_circle_filled(55 + x, 550, 190, arcade.color.ENGLISH_GREEN)
    arcade.draw_circle_outline(55 + x, 550, 190, arcade.color.BLACK, 3)

def draw_coche(x):
    "Dibuja un coche"
    arcade.draw_triangle_outline(91 + x, 275, 180 + x, 275, 143 + x, 375, arcade.color.BLACK, 5)
    arcade.draw_rectangle_outline(130 + x, 250, 75, 55, arcade.color.BLACK, 5)
    arcade.draw_rectangle_outline(425 + x, 260, 175, 75, arcade.color.BLACK, 5)
    arcade.draw_rectangle_filled(280 + x, 300, 275, 155, arcade.color.BYZANTINE)
    arcade.draw_rectangle_outline(280 + x, 300, 275, 155, arcade.color.BLACK, 3)
    arcade.draw_rectangle_filled(130 + x, 250, 75, 55, arcade.color.BYZANTINE)
    arcade.draw_rectangle_filled(425 + x, 262, 175, 73, arcade.color.BYZANTINE)
    arcade.draw_triangle_filled(91 + x, 275, 180 + x, 275, 143 + x, 375, arcade.color.BYZANTINE)
    # Ruedas
    arcade.draw_circle_filled(170 + x, 210, 40, arcade.color.GRAPE)
    arcade.draw_circle_filled(420 + x, 210, 40, arcade.color.GRAPE)
    arcade.draw_circle_filled(170 + x, 210, 35, arcade.color.BLACK)
    arcade.draw_circle_filled(420 + x, 210, 35, arcade.color.BLACK)
    arcade.draw_circle_filled(170 + x, 210, 20, arcade.color.HONEYDEW)
    arcade.draw_circle_filled(420 + x, 210, 20, arcade.color.HONEYDEW)
    # Ventanas
    arcade.draw_rectangle_filled(350 + x, 335, 110, 70, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_rectangle_outline(350 + x, 335, 110, 70, arcade.color.BLACK, 3)
    arcade.draw_rectangle_filled(220 + x, 335, 110, 70, arcade.color.BLACK_LEATHER_JACKET)
    arcade.draw_rectangle_outline(220 + x, 335, 110, 70, arcade.color.BLACK, 3)

def on_draw(delta_time):
    "Animación del coche"
    arcade.start_render()

    draw_fondo()
    draw_arbol_pequeño(0)
    draw_arbol_pequeño(400)
    draw_arbol_grande(0)
    draw_arbol_grande(400)
    draw_arbol_grande(800)
    draw_coche(on_draw.mov_x)


    on_draw.mov_x += 1 * delta_time

on_draw.mov_x = 0

def main():
    arcade.open_window(1000, 600, "Coche")
    arcade.set_background_color(arcade.color.GRAPE)

    arcade.schedule(on_draw, 1/60)

    arcade.run()

main()