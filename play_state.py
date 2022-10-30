import pico2d
import game_framework
import title_state
from Scripts.Object.Tile.Tile import *

class Map:
    score = 0
    #font = pico2d.load_font('./map/STENCIL.ttf', 40)
    def __init__(self):
        self.step = 1
        self.image = None
        self.block = []
        self.monster_count = 0;
        self.map_pass = 0
        self.move_start = False
        self.frame = (6 - self.step) * 61

    def draw(self):
        #self.image.clip_draw(0, (6 - self.step) * 610, 800, 600, 400, 300)
        self.image.clip_draw(0, self.frame * 10, 800, 600, 400, 300)

    pass

class Character:
    def __init__(self):
        self.x, self.y = 100, 60
        self.dir_x, self.dir_y = 0, 0
        self.gravity = 0
        self.frame = 0
        self.life = 3
        self.flip = ' '
        self.image = pico2d.load_image('./character/character3.png')

        self.now_x = 0
        self.now_y = 0

        self.move_on = False

    def draw(self):
        if character.dir_x == -1:
            self.image.clip_composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)
        else:
            self.image.clip_    composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60

class Attack():
    #attack = pico2d.load_image('./character/attack.png')
    def __init__(self):
        self.attack_x, self.attack_y = 0, 0
        self.attack_frame = 0
        self.count = []
        self.time = 0

    def draw(self):
        self.attack.clip_draw(self.attack_frame * 50, 100, 30, 30, self.attack_x, self.attack_y)

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

def make_stool():
    global stage1, stage2

    stage1.block.clear()

    if stage1.step == 1:
        #                    좌, 아래, 우, 위
        stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
        stage1.block.append([330, 60, 470, 60])  # 1층 중앙
        stage1.block.append([610, 60, 730, 60])  # 1층 오른쪽
        stage1.block.append([185, 165, 370, 165])  # 2층 왼쪽
        stage1.block.append([455, 165, 635, 165])  # 2층 오른쪽
        stage1.block.append([120, 270, 330, 270])  # 3층 왼쪽
        stage1.block.append([515, 270, 705, 270])  # 3층 오른쪽
        stage1.block.append([210, 375, 370, 375])  # 4층 왼쪽
        stage1.block.append([450, 375, 620, 375])  # 4층 오른쪽
        stage1.block.append([230, 480, 370, 480])  # 5층 왼쪽
        # stage1.block.append([190, 480, 200, 600])  # 5층 왼쪽 벽
        stage1.block.append([450, 480, 580, 480])  # 5층 오른쪽

    elif stage1.step == 2:
        stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
        stage1.block.append([340, 60, 470, 60])  # 1층 중앙
        stage1.block.append([610, 60, 730, 60])  # 1층 오른쪽
        stage1.block.append([115, 165, 270, 165])  # 2층 왼쪽
        stage1.block.append([370, 165, 430, 165])  # 2층 중앙
        stage1.block.append([530, 165, 670, 165])  # 2층 오른쪽
        stage1.block.append([160, 270, 350, 270])  # 3층 왼쪽
        stage1.block.append([440, 270, 630, 270])  # 3층 오른쪽
        stage1.block.append([160, 375, 350, 375])  # 4층 왼쪽
        stage1.block.append([440, 375, 630, 375])  # 4층 오른쪽
        stage1.block.append([120, 480, 350, 480])  # 5층 왼쪽
        stage1.block.append([440, 480, 670, 480])  # 5층 오른쪽

    elif stage1.step == 3:
        stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
        stage1.block.append([340, 60, 470, 60])  # 1층 중앙
        stage1.block.append([600, 60, 730, 60])  # 1층 오른쪽
        stage1.block.append([120, 165, 350, 165])  # 2층 왼쪽
        stage1.block.append([460, 165, 680, 165])  # 2층 오른쪽
        stage1.block.append([160, 270, 770, 270])  # 3층
        stage1.block.append([0, 375, 630, 375])  # 4층
        stage1.block.append([160, 480, 770, 480])  # 5층

    elif stage1.step == 4:
        stage1.block.append([60, 60, 200, 60])  # 1층 왼쪽
        stage1.block.append([340, 60, 470, 60])  # 1층 중앙
        stage1.block.append([600, 60, 730, 60])  # 1층 오른쪽
        stage1.block.append([140, 165, 320, 165])  # 2층 왼쪽
        stage1.block.append([490, 165, 670, 165])  # 2층 오른쪽
        stage1.block.append([0, 270, 240, 270])  # 3층 왼쪽
        stage1.block.append([570, 270, 770, 270])  # 3층 오른쪽
        stage1.block.append([0, 375, 190, 375])  # 4층 왼쪽
        stage1.block.append([630, 375, 770, 375])  # 4층 오른쪽

        stage1.block.append([330, 355, 360, 355])  # 3.5층 오른쪽
        stage1.block.append([450, 355, 470, 355])  # 3.5층 왼쪽

        stage1.block.append([300, 420, 330, 420])  # 4.5층 왼쪽
        stage1.block.append([470, 420, 530, 420])  # 4.5층 오른쪽

        stage1.block.append([0, 480, 130, 480])  # 5층 왼쪽
        stage1.block.append([200, 480, 280, 480])  # 5층 중앙 왼쪽
        stage1.block.append([530, 480, 610, 480])  # 5층 중앙 오른쪽
        stage1.block.append([680, 480, 770, 480])  # 5층 오른쪽

def monster_set():
    if stage1.step == 1:
        for i in range(4):
            zen[i].type = 810
        zen[0].x, zen[0].y = 470, 375
        zen[1].x, zen[1].y = 330, 375
        zen[2].x, zen[2].y = 530, 270
        zen[3].x, zen[3].y = 280, 270

def monster_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    pass

def character_animation():
    global character

    if character.move_on:
        character.frame += 1
        character.frame %= 4

    pass

def enter():
    global character, stage1, stage2, stage3, zen, mighta, start_jump, attack

    character = Character()
    start_jump = 60

    attack = Attack()

    stage1 = Map()
    stage1.image = pico2d.load_image('./map/stage1 Fairy_land map.png')

    stage2 = Map()
    stage2.image = pico2d.load_image('./map/stage2 dessert_land map.png')

    stage3 = Map()
    stage3.image = pico2d.load_image('./map/stage3 toy_land map.png')

    zen = [Monster() for i in range(10)]

    mighta = Monster()

    monster_set()
    make_stool()
    pass

def exit():
    global character, stage1, stage2, stage3, zen
    del character, stage1, stage2, stage3, zen
    pass

def handle_events():
    global start_jump, stage1

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
                    character.flip = 'h'
                case pico2d.SDLK_LEFT:
                    character.flip = ' '
                    character.dir_x -= 1
                case pico2d.SDLK_SPACE:
                    if character.gravity == 0:
                        start_jump = 0
                case pico2d.SDLK_a:
                    attack.count.append()
                #임시 맵 조정 코드
                case pico2d.SDLK_0:
                    character.gravity = 0
                    character.now_x = character.x - 100
                    character.now_y = character.y - 60

                    character.now_x /= 61
                    character.now_y /= 61

                    stage1.move_start = True
                    stage1.step += 1
                    make_stool()


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

    if stage1.step == 1:
        for i in range(4):
            zen[i].draw()

    #stage1.font.draw(400, 570, 'SCORE : ' % stage1.score, (255, 255, 0))

    pico2d.update_canvas()
    pass

def update():
    global character, start_jump, zen
    character.x += character.dir_x
    character.y -= character.gravity

    character_animation()

    #캐릭터 점프
    if start_jump < 70:
        character.y += 3
        start_jump += 1

    #monster_collide(character, zen)

    #1스테이지 발판 충돌 체크
    if not stage1.move_start:
        if map_collide():
            character.gravity = 0
        elif not map_collide():
            character.gravity = 1



    if stage1.move_start:
        if stage1.map_pass % 10 == 0:
            stage1.frame -= 1
            character.x -= character.now_x
            character.y -= character.now_y
        stage1.map_pass += 1

    if stage1.map_pass >= 610:
        stage1.move_start = False
        stage1.map_pass = 0
        character.y = 65
        character.gravity = 1
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
