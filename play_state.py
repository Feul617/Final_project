import pico2d
import game_framework
import title_state

class Map:
    def __init__(self):
        self.step = 5
        self.image = None
        self.block = []

    def draw(self):
        self.image.clip_draw(0, self.step * 610, 800, 600, 400, 300)


    pass

class Character:
    def __init__(self):
        self.x, self.y = 515, 280
        self.dir_x, self.dir_y = 0, 0
        self.gravity = 0
        self.frame = 0
        self.life = 3
        self.image = pico2d.load_image('./character/character3.png')

        self.move_on = False

    def draw(self):
        self.image.clip_draw(self.frame * 60, 410, 60, 40, self.x, self.y)

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60

class Monster:
    def __init__(self):
        self.x, self.y = 500, 500
        self.dir_x, self.dir_y = 0, 0
        self.frame = 0
        self.image = None

    def draw(self):
        self.image.clip_draw(self.frame * 50, 550, 60, 40, self.x, self.y)


def enter():
    global character, stage1, stage2, stage3

    character = Character()

    stage1 = Map()
    stage1.image = pico2d.load_image('./map/stage1 Fairy_land map.png')
    #                    좌, 아래, 우, 위
    stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
    stage1.block.append([330, 60, 470, 60]) # 1층 중앙
    stage1.block.append([610, 60, 730, 60]) # 1층 오른쪽
    stage1.block.append([185, 165, 370, 165])  # 2층 왼쪽
    stage1.block.append([455, 165, 635, 165])  # 2층 오른쪽
    stage1.block.append([120, 270, 330, 270])  # 3층 왼쪽
    stage1.block.append([515, 270, 705, 270])  # 3층 오른쪽
    stage1.block.append([210, 375, 370, 375])  # 4층 왼쪽
    stage1.block.append([450, 375, 620, 375])  # 4층 오른쪽
    stage1.block.append([210, 480, 370, 480])  # 5층 왼쪽
    # stage1.block.append([190, 480, 200, 600])  # 5층 왼쪽 벽
    stage1.block.append([450, 480, 620, 480])  # 5층 오른쪽
    stage2 = Map()


    stage3 = Map()
    pass

def exit():
    global character, stage1, stage2, stage3
    del character, stage1, stage2, stage3
    pass

def handle_events():
    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()

        elif event.type == pico2d.SDL_KEYDOWN:
            character.move_on = True
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                #캐릭터 조종
                case pico2d.SDLK_RIGHT:
                    character.dir_x += 1
                case pico2d.SDLK_LEFT:
                    character.dir_x -= 1
                case pico2d.SDLK_SPACE:
                    character.gravity = 0
                    for i in range(60):
                        if character.y <= 550:
                            character.y += 2
                    character.gravity = 1

        elif event.type == pico2d.SDL_KEYUP:
            character.move_on = False
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
    global character
    character.x += character.dir_x
    character.y -= character.gravity

    print(character.get_bb())
    print('\n')

    #움직이는 에니메이션
    if character.move_on:
        character.frame += 1
        character.frame %= 4

    # y축 맵 이탈 금지
    if character.y < 0:
        character.y = 600

    #1스테이지 발판 충돌 체크
    if stage1.step == 5:
        if map_collide():
            character.gravity = 0
        elif not map_collide():
            character.gravity = 1
    pass

def map_collide():
    global stage1, character

    if character.get_bb()[2] > 750:
        character.x -= 1
    elif character.get_bb()[0] < 55:
        character.x += 1


    for i in stage1.block:
        if character.get_bb()[2] > i[0] and character.get_bb()[0] < i[2] \
                and i[3] <= character.get_bb()[1] <= i[1]:
            return True

    return False

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