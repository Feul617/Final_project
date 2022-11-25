from pico2d import *
import game_framework
import title_state
import play_state

open_canvas(800, 610)
game_framework.run(title_state)
close_canvas()