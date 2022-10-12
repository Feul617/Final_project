from pico2d import *
import game_framework
import title_state

class Map:

    def __init__(self):
        self.image = None
        self.step = 5

    def draw(self):
        self.image.clip_draw(0, self.step * 610, 800, 600, 400, 300)

    pass


class Character:
    def __init__(self):
        self.x, self.y = 50, 50
        self.dir_x, self.dir_y = 0, 0
        self.gravity = 1
        self.frame = None
        self.image = load_image('./character/character2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 50, 550, 60, 60, self.x, self.y - self.gravity)

    def handle(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    self.dir_x += 1
                elif event.key == SDLK_LEFT:
                    self.dir_x -= 1
                elif event.key == SDLK_SPACE:
                    self.dir_y += 10




    pass


def handle_events():

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

def enter():
    global character, stage1, stage2, stage3

    character = Character()
    stage1, stage2, stage3 = Map()
    stage1.image = load_image('./map/stage1 Fairy_land map.png')
    stage2.image = load_image('./map/stage2 dessert_land map.png')
    pass

def exit():
    global character, stage1, stage2, stage3
    del character, stage1, stage2, stage3
    pass

def map_draw():
    global stage

    if stage == 1:
        stage1.draw()
    elif stage == 2:
        stage2.draw()
    elif stage == 3:
        stage3.draw()
    pass

def character_move():
    global character

    if 60 < character.x < 730:
        character.x += character.dir_x * 3
    elif character.x >= 730 or character.x <= 60:
        character.x -= 1

running = True
stage = 1

while running:
    clear_canvas()

    character_move()

    update_canvas()
