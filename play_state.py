import game_framework
import title_state
from Scripts.Object.Object_AFX import *

class Monster:
    def __init__(self):
        self.x, self.y = 470, 375
        self.dir_x, self.dir_y = 0, 0
        self.frame = 0
        self.flip = ' '
        self.image = pico2d.load_image('./character/monster2.png')
        self.type = 0

    def draw(self):
        self.image.clip_composite_draw(self.frame * 50, self.type, 50, 50, 0, self.flip, self.x, self.y, 50, 50)

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60

def monster_set():
    pass

def enter():
    global RenderList
    global stage1_1

    RenderList = []

    stage1_1 = MainStage()
    stage1_1.Tile_init()

    RenderList.append(stage1_1.background)
    for tile in stage1_1.tiles:
        RenderList += tile.tiles

    pass

def exit():
    pass

def handle_events():
    global start_jump, stage1

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
                    character.flip = 'h'
                case pico2d.SDLK_LEFT:
                    character.flip = ' '
                    character.dir_x -= 1
                case pico2d.SDLK_SPACE:
                    if character.gravity == 0:
                        start_jump = 0
                #임시 맵 조정 코드
                case pico2d.SDLK_0:
                    character.gravity = 0
                    character.now_x = character.x - 100
                    character.now_y = character.y - 60

                    character.now_x /= 61
                    character.now_y /= 61

                    stage1.move_start = True
                    stage1.step += 1


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
    global RenderList

    for obj in RenderList:
        obj.Draw()

    pico2d.update_canvas()
    pass

def update():
    # global character, start_jump, zen
    # character.x += character.dir_x
    # character.y -= character.gravity
    #
    # character_animation()
    #
    # #캐릭터 점프
    # if start_jump < 70:
    #     character.y += 3
    #     start_jump += 1
    #
    # #monster_collide(character, zen)
    #
    # #1스테이지 발판 충돌 체크
    # if not stage1.move_start:
    #     if map_collide():
    #         character.gravity = 0
    #     elif not map_collide():
    #         character.gravity = 1
    #
    #
    #
    # if stage1.move_start:
    #     if stage1.map_pass % 10 == 0:
    #         stage1.frame -= 1
    #         character.x -= character.now_x
    #         character.y -= character.now_y
    #     stage1.map_pass += 1
    #
    # if stage1.map_pass >= 610:
    #     stage1.move_start = False
    #     stage1.map_pass = 0
    #     character.y = 65
    #     character.gravity = 1
    pass


def map_collide():
    global stage1, stage2, character

    # y축 맵 이탈 금지
    if character.y > 550:
        character.y -= 1

    # 구멍 이동
    if character.y < 0:
        character.y = 600

    # x축 맵 이탈 금지
    if character.get_bb()[2] > 750:
        character.x -= 1
    elif character.get_bb()[0] < 55:
        character.x += 1

    # 1-1 스테이지 벽
    if stage1.step == 1:
        if (209 <= character.get_bb()[0] <= 210 or 560 <= character.get_bb()[0] <= 615) and  character.get_bb()[1] >= 460:
            character.x += 1

        elif (550 <= character.get_bb()[0] <= 555 or 150 <= character.get_bb()[0] <= 208) and character.get_bb()[1] >= 460:
            character.x -= 1

    # 1-2 스테이지 벽
    if stage1.step == 2:
        if (155 <= character.get_bb()[0] <= 160 or 680 <= character.get_bb()[0] <= 685) and 250 <= character.get_bb()[1] <= 475:
            character.x += 1

        elif (610 <= character.get_bb()[0] <= 615 or 80 <= character.get_bb()[0] <= 115) and 250 <= character.get_bb()[1] <= 475:
            character.x -= 1

    # 1 - 4스테이지 벽
    if stage1.step == 4:
        if (280 <= character.get_bb()[0] <= 290 or 500 <= character.get_bb()[0] <= 540) and 420 <= character.get_bb()[1] <= 479:
            character.x += 1

        elif (475 <= character.get_bb()[0] <= 485 or 240 <= character.get_bb()[0] <= 279) and 420 <= character.get_bb()[1] <= 479:
            character.x -= 1

        if (330 <= character.get_bb()[0] <= 340 or 470 <= character.get_bb()[0] <= 480) and 335 <= character.get_bb()[1] <= 415:
            character.x += 1

        elif (420 <= character.get_bb()[0] <= 425 or 260 <= character.get_bb()[0] <= 270) and 345 <= character.get_bb()[1] <= 415:
            character.x -= 1



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
