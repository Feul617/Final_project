from pico2d import *
import game_framework
import play_state

next_stage = None
banner_delay = None

def enter():
    global image, banner, banner_on, banner_time
    global count, bgm, bgm_on, next_stage, banner_delay
    image = load_image('./map/title.png')
    banner = load_image('./map/insert_coin.png')
    bgm = load_music('./sound/Invincible(start screen) .mp3')
    bgm.set_volume(10)
    bgm_on = True
    banner_on = True
    banner_time = 200
    banner_delay = 1
    count = 0
    next_stage = False
    pass


def exit():
    global image, banner
    del image, banner
    pass

def handle_events():
    global banner_time, count, next_stage, banner_delay

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            next_stage = True
            banner_time = 1
            banner_delay = 4

    pass


def draw():
    global banner_on
    clear_canvas()
    image.draw(400, 305, 800, 610)
    if banner_on:
        banner.draw(400, 30)
    update_canvas()

def update():
    global banner_on, count, bgm, bgm_on, banner_time, next_stage, banner_delay

    banner_time -= 1
    if banner_time == 0:
        banner_time = 200 / banner_delay
        banner_on = not banner_on

    if bgm_on:
        bgm.play(1)
        bgm_on = False

    if next_stage:
        count += 1
        if count == 700:
            game_framework.change_state(play_state)

def pause():
    pass

def resume():
    pass

def Banner_on():
    global banner_on
    banner_on = not banner_on

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면
    test_self()