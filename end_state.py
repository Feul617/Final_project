from pico2d import *
import game_framework
import title_state

#변수
bg_image = None

def enter():
    global bg_image
    bg_image = load_image('./map/thank you for playing.png')
    pass


def exit():
    global bg_image
    del bg_image
    pass

def handle_events():

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_state(title_state)

    pass

def draw():
    global bg_image
    clear_canvas()
    bg_image.draw(400,305,800,610)
    update_canvas()
    pass

def update():
    pass

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