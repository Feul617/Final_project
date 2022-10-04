from pico2d import *

open_canvas()
title = load_image('title.png')
title_banner = load_image('insert_coin.png')
map1 = load_image('stage1 Fairy_land map.png')
map2 = load_image('stage2 dessert_land map.png')
map3 = load_image('stage3 toy_land map.png')


def handle_event():
    global running
    global start_title

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            start_title = False
            if event.key == SDLK_ESCAPE:
                running = False
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
    update_canvas()


def draw_second_map():
    clear_canvas()
    map2.clip_draw(0, stage * 610, 800, 600, 400, 300)
    update_canvas()


def draw_third_map():
    clear_canvas()
    map3.clip_draw(0, stage * 610, 800, 600, 400, 300)
    update_canvas()


def draw_character():
    clear_canvas()


#변수
running = True
banner_on = True
start_title = False
insert_coin = True
first_step = True
second_step = False
stage = 5
frame = 0


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


close_canvas()