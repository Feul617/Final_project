import Scripts.FrameWork.game_world
import game_framework
import title_state
from Scripts.Object.Object_AFX import *

Renderlist = []

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def map_collide(a, b):
    left_a, bottom_a, right_a, top_a = a.tile_get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def Monster_move():
    global zen_chan
    zen_chan[0].transform.position.x = clamp(130, zen_chan[0].transform.position.x, 305)
    if zen_chan[0].transform.position.x == 130 or zen_chan[0].transform.position.x == 305:
        zen_chan[0].dir *= -1

    zen_chan[1].transform.position.x = clamp(500, zen_chan[1].transform.position.x, 675)
    if zen_chan[1].transform.position.x == 500 or zen_chan[1].transform.position.x == 675:
        zen_chan[1].dir *= -1

    zen_chan[2].transform.position.x = clamp(215, zen_chan[2].transform.position.x, 370)
    if zen_chan[2].transform.position.x == 215 or zen_chan[2].transform.position.x == 370:
        zen_chan[2].dir *= -1

    zen_chan[3].transform.position.x = clamp(460, zen_chan[3].transform.position.x, 615)
    if zen_chan[3].transform.position.x == 460 or zen_chan[3].transform.position.x == 615:
        zen_chan[3].dir *= -1
def enter():
    global Renderlist
    global character
    global stage1
    global zen_chan

    #캐릭터
    character = Character()
    add_object(character, 2)

    #맵 & 타일
    stage1 = MainStage()
    stage1.Tile_init()

    add_object(stage1.background, 0)

    for tile in stage1.tiles:
        add_objects(tile.tiles, 1)

    #몬스터
    zen_chan = [Monster() for i in range(4)]
    for i in range(4):
        zen_chan[i].name = 'zen_chan'
        zen_chan[i].name_type()
    #시작위치지정
    zen_chan[0].transform.position.x, zen_chan[0].transform.position.y = 140, 260
    zen_chan[1].transform.position.x, zen_chan[1].transform.position.y = 650, 260
    zen_chan[2].transform.position.x, zen_chan[2].transform.position.y = 300, 365
    zen_chan[3].transform.position.x, zen_chan[3].transform.position.y = 500, 365


    add_objects(zen_chan, 2)


    #충돌체크
    add_collision_group(character, stage1.tiles, 'character:tile')
    add_collision_group(character, zen_chan, 'character:monster')

    pass

def exit():
    pass

def handle_events():
    global stage1, character

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_events(event)

def draw():
    pico2d.clear_canvas()
    global Renderlist
    global character
    global monster1

    for game_object in all_objects():
        game_object.Draw()

    pico2d.update_canvas()
    pass

def update():
    for game_object in all_objects():
        game_object.update()

    for a, b, group in all_collision_pairs():
        if map_collide(a, b):
            a.map_handle_collision(b, group)
            b.handle_collision(a, group)

    for a, b, group in all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    Monster_move()

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
