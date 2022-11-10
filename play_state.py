import Scripts.FrameWork.game_world
import game_framework
import title_state
from Scripts.Object.Object_AFX import *

def enter():
    global RenderList
    global character, stage1_1
    global monster1

    RenderList = []

    stage1_1 = MainStage()
    stage1_1.Tile_init()

    character = Character()

    monster1 = Monster()
    monster1 = Monster_Type(0)

    RenderList.append(stage1_1.background)
    for tile in stage1_1.tiles:
        RenderList += tile.tiles

    add_collision_group(character)


    pass

def exit():
    pass

def handle_events():
    global stage1, character

    events = pico2d.get_events()
    character.handle_events(events)
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()

        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
def draw():
    pico2d.clear_canvas()
    global RenderList, character
    global monster1

    for obj in RenderList:
        obj.Draw()

    character.Draw()
    monster1.Draw()


    pico2d.update_canvas()
    pass

def update():
    global character

    character.update()
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
