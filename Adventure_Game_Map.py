import arcade
arcade.open_window(800, 800, "Adventure Game Map")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()
arcade.draw_circle_filled(400,400,380, arcade.color.WHITE)

arcade.draw_circle_outline(400, 400, 12, arcade.color.BLACK)
width =
for i in range(18):






arcade.finish_render()
arcade.run()