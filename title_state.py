from pico2d import *
import game_framework
import play_state

def enter():
    global image, banner
    image = load_image('title.png')
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_KP_ENTER):
            running = False
            game_framework.change_state(play_state)
    pass


def draw():
    global banner_on
    clear_canvas()
    image.draw(400,300)
    if banner_on:
        banner.draw(400,30)
    update_canvas()


banner_on = True
running = True

while running:
    delay(0.8)
    banner_on = not banner_on