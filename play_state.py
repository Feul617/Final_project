import pico2d
import game_framework
import title_state

class Map:
    def __init__(self):
        self.step = 5
        self.image = None

    def draw(self):
        self.image.clip_draw(0, self.step * 610, 800, 600, 400, 300)

    pass

class Character:
    def __init__(self):
        self.x, self.y = 50, 50
        self.dir_x, self.dir_y = 0, 0
        self.gravity = 1
        self.frame = 3
        self.life = 3
        self.image = pico2d.load_image('./character/character2.png')

    def draw(self):
        self.image.clip_draw(self.frame * 50, 550, 70, 70, self.x, self.y)


def enter():
    global character, stage1, stage2, stage3

    character = Character()
    stage1 = Map()
    stage1.image = pico2d.load_image('./map/stage1 Fairy_land map.png')
    pass

def exit():
    pass

def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()

        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                #캐릭터 조종
                case pico2d.SDLK_RIGHT:
                    character.dir_x += 1
                case pico2d.SDLK_LEFT:
                    character.dir_x -= 1
                case pico2d.SDLK_SPACE:
                    character.y += 50

        elif event.type == pico2d.SDL_KEYUP:
            match event.key:
                #캐릭터 조종
                case pico2d.SDLK_RIGHT:
                    character.dir_x -= 1
                case pico2d.SDLK_LEFT:
                    character.dir_x += 1

def draw():
    pico2d.clear_canvas()
    stage1.draw()
    character.draw()
    pico2d.update_canvas()
    pass

def update():
    character.x += character.dir_x
    character.y -= character.gravity

    if character.y < 0:
        character.y = 600
    pass

def pause():
    pass

def resume():
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면
    test_self()