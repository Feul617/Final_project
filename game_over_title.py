from pico2d import *
import game_framework
import play_state

def enter():
    global image
    image = load_image('./map/game_over_title.png')
    pass


def exit():
    global image
    del image
    pass

def handle_events():
    global banner_time, count

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            banner_time = 0.1

    pass


def draw():
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def update():
    global banner_on, count

    delay(banner_time)
    banner_on = not banner_on
    count += 1
    if count >= 20:
        game_framework.change_state(play_state)

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