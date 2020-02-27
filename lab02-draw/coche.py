import arcade

arcade.open_window(1000, 600, "Coche")
arcade.set_background_color(arcade.color.GRAPE)
arcade.start_render()

arcade.draw_lrtb_rectangle_filled(0, 1000, 450, 0, arcade.color.BITTER_LIME)
arcade.draw_lrtb_rectangle_filled(0, 1000, 300, 0, arcade.color.DARTMOUTH_GREEN)
arcade.draw_lrtb_rectangle_filled(0, 1000, 250, 0, arcade.color.DARK_GREEN)

#árbol
arcade.draw_rectangle_filled(50, 175, 50, 500, arcade.color.BLACK_BEAN)
arcade.draw_rectangle_filled(450, 175, 50, 500, arcade.color.BLACK_BEAN)
arcade.draw_rectangle_filled(850, 175, 50, 500, arcade.color.BLACK_BEAN)

arcade.draw_rectangle_filled(250, 175, 35, 350, arcade.color.BLACK_BEAN)
arcade.draw_rectangle_filled(650, 175, 35, 350, arcade.color.BLACK_BEAN)

#Hojas de los árboles
arcade.draw_circle_filled(255, 450, 110, arcade.color.ENGLISH_GREEN)
arcade.draw_circle_outline(255, 450, 110, arcade.color.BLACK, 2)
arcade.draw_circle_filled(655, 450, 110, arcade.color.ENGLISH_GREEN)
arcade.draw_circle_outline(655, 450, 110, arcade.color.BLACK, 2)

arcade.draw_circle_filled(55, 550, 190, arcade.color.ENGLISH_GREEN)
arcade.draw_circle_outline(55, 550, 190, arcade.color.BLACK, 3)
arcade.draw_circle_filled(455, 550, 190, arcade.color.ENGLISH_GREEN)
arcade.draw_circle_outline(455, 550, 190, arcade.color.BLACK, 3)
arcade.draw_circle_filled(855, 550, 190, arcade.color.ENGLISH_GREEN)
arcade.draw_circle_outline(855, 550, 190, arcade.color.BLACK, 3)

#Esqueleto del coche
arcade.draw_triangle_outline(91, 275, 180, 275, 143, 375, arcade.color.BLACK, 5)
arcade.draw_rectangle_outline(130, 250, 75,55, arcade.color.BLACK, 5)
arcade.draw_rectangle_outline(425, 260, 175,75, arcade.color.BLACK, 5)
arcade.draw_rectangle_filled(280, 300, 275, 155, arcade.color.BYZANTINE)
arcade.draw_rectangle_outline(280, 300, 275, 155, arcade.color.BLACK, 3)
arcade.draw_rectangle_filled(130, 250, 75,55, arcade.color.BYZANTINE)
arcade.draw_rectangle_filled(425, 262, 175,73, arcade.color.BYZANTINE)

arcade.draw_triangle_filled(91, 275, 180, 275, 143, 375, arcade.color.BYZANTINE)

#Ruedas
arcade.draw_circle_filled(170, 210, 40, arcade.color.GRAPE)
arcade.draw_circle_filled(420, 210, 40, arcade.color.GRAPE)
arcade.draw_circle_filled(170, 210, 35, arcade.color.BLACK)
arcade.draw_circle_filled(420, 210, 35, arcade.color.BLACK)
arcade.draw_circle_filled(170, 210, 20, arcade.color.HONEYDEW)
arcade.draw_circle_filled(420, 210, 20, arcade.color.HONEYDEW)

#suelo
arcade.draw_lrtb_rectangle_filled(0, 1000, 175, 0, arcade.color.AUROMETALSAURUS)
arcade.draw_lrtb_rectangle_filled(0, 1000, 125, 0, arcade.color.APPLE_GREEN)

#Ventanas
arcade.draw_rectangle_filled(350, 335, 110, 70, arcade.color.BLACK_LEATHER_JACKET)
arcade.draw_rectangle_outline(350, 335, 110, 70, arcade.color.BLACK, 3)
arcade.draw_rectangle_filled(220, 335, 110, 70, arcade.color.BLACK_LEATHER_JACKET)
arcade.draw_rectangle_outline(220, 335, 110, 70, arcade.color.BLACK, 3)

arcade.finish_render()
arcade.run()