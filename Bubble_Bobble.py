from pico2d import *

open_canvas()
title = load_image('title.png')
title_banner = load_image('insert_coin.png')
map1 = load_image('stage1 Fairy_land map.png')
map2 = load_image('stage2 dessert_land map.png')
map3 = load_image('stage3 toy_land map.png')
character = load_image('character.png')


class Monster:
    def __init__(self):
        self.x, self.y = 100, 50
        self.frame

    def update(self):
        self.x += 2


def handle_event():
    global running
    global start_title
    global insert_coin
    global character_x
    global character_y
    global dirx, diry

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                sight = 100
                dirx += 1
            elif event.key == SDLK_LEFT:
                dirx -= 1
                sight = 0
            elif event.key == SDLK_SPACE:
                for i in range(5):
                    character_y += 10
                    delay(0.01)
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dirx -= 1
            elif event.key == SDLK_LEFT:
                dirx += 1

    pass


def draw_title():
    clear_canvas()
    title.draw(400, 300)
    if banner_on:
        title_banner.draw(400, 30)

    update_canvas()
    pass


def draw_first_map():
    clear_canvas()
    map1.clip_draw(0, stage * 610, 800, 600, 400, 300)


def draw_second_map():
    clear_canvas()
    map2.clip_draw(0, stage * 610, 800, 600, 400, 300)
    update_canvas()


def draw_third_map():
    clear_canvas()
    map3.clip_draw(100, stage * 610, 800, 600, 400, 300)
    update_canvas()


def draw_character():
    global character_x
    global character_y
    global dirx, diry
    global gravity

    character_x += dirx
    character_y -= gravity
    character.clip_draw(0, 180, 30, 30, character_x, character_y)
    if character_y < 10:
        character_y = 600

    if character_x < 0:
        character_x = 800
    elif character_x > 800:
        character_x = 0


#변수
running = True
banner_on = True
start_title = False
insert_coin = True
first_step = True
second_step = False
stage = 5
frame = 0
character_x = 50
character_y = 50
dirx, diry = 0, 0;
gravity = 3


#메인문
while running:
    handle_event()
    if start_title:
        draw_title()
        delay(0.8)
        banner_on = not banner_on

    if insert_coin:
        if first_step:
            draw_first_map()

        if second_step:
            draw_second_map()

        draw_character()
        update_canvas()

close_canvas()