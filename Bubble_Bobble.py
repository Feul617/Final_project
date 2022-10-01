from pico2d import *


def handle_event():
    global running
    global start

    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            start = False
            if event.key == SDLK_ESCAPE:
                running = False
    pass


def draw_title():
    clear_canvas()
    title.draw(400, 300)
    title_banner.draw(400, 30)
    update_canvas()
    pass


open_canvas()
title = load_image('title.png')
title_banner = load_image('insert_coin.png')
map1 = load_image('stage1 Fairy_land map.png')
map2 = load_image('stage2 dessert_land map.png')
map3 = load_image('stage3 toy_land map.png')

running = True
start = True
frame = 0

while running:
    if start:
        draw_title()
    handle_event()


close_canvas()