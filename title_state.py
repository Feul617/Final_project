from pico2d import *
import game_framework
import play_state

def enter():
    global image, banner
    image = load_image('./map/title.png')
    banner = load_image('./map/insert_coin.png')
    pass


def exit():
    global image, banner
    del image, banner
    pass

def handle_events():
    global running
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            running = False
            game_framework.change_state(play_state)
    pass


def draw():
    global banner_on
    clear_canvas()
    image.draw(400, 300)
    if banner_on:
        banner.draw(400, 30)
    update_canvas()

banner_on = True
running = True

def update():
    global banner_on

    delay(0.8)
    banner_on = not banner_on

def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    open_canvas()
    game_framework.run(this_module)
    close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면
    test_self()