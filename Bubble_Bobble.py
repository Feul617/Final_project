from pico2d import *
import game_framework
import title_state

open_canvas()
game_framework.run(title_state)

def draw_first_map():
    global character_x
    global character_y
    global dirx, diry
    global gravity

    clear_canvas()
    map1.clip_draw(0, stage * 610, 800, 600, 400, 300)
    if stage == 5:
        if 60 <= character_x <= 200 or 360 <= character_x <= 470 or 610 <= character_x <= 730 and character_y < 120:
            gravity = 0
        else:
            gravity = 3




def draw_second_map():
    clear_canvas()
    map2.clip_draw(0, stage * 610, 800, 600, 400, 300)


def draw_third_map():
    clear_canvas()
    map3.clip_draw(100, stage * 610, 800, 600, 400, 300)


def draw_character():
    global character_x
    global character_y
    global dirx, diry
    global gravity

    character_x += dirx
    character_y -= gravity
    character.clip_draw(0, 550, 60, 60, character_x, character_y)
    if character_y < 10:
        character_y = 600

    if character_x < 65:
        character_x += 1
    elif character_x > 730:
        character_x -= 1


close_canvas()