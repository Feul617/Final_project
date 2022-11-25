import Scripts.FrameWork.game_world
import game_framework
import title_state
from Scripts.Object.Object_AFX import *
from Scripts.Stage.StageContain import *
from Scripts.FrameWork.Camera import Camera

gameWorld = None
camera = None

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

def enter():
    global character
    global step, stages
    global zen_chan
    global gameWorld
    global camera

    camera = Camera()
    Camera.mainCamera = camera

    gameWorld = GameWorld()

    Object.gameWorld = gameWorld
    #캐릭터
    character = Character()
    gameWorld.add_object(character, 2)

    #맵 & 타일
    step = 1

    stages = [Stage1_1(), Stage1_2()]

    for i in range(len(stages) - 1):
        stages[i].nextStage = stages[i+1]
        stages[i + 1].isActive = False

    #몬스터
    # zen_chan = [Monster() for i in range(4)]
    # for i in range(4):
    #     zen_chan[i].name = 'zen_chan'
    #     zen_chan[i].count += 1
    character.charac = character


    #충돌체크
    for i in range(len(stages)):
        gameWorld.add_collision_group(character, stages[i].tiles, 'character:tile')
    # add_collision_group(character, zen_chan, 'character:monster')
    # add_collision_group(zen_chan, stage1.tiles, 'monster:tile')

    for game_object in gameWorld.all_objects():
        game_object.Init()

    pass

def exit():
    pass

def handle_events():
    global character
    global step, stages

    events = pico2d.get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            character.handle_events(event)
            for i in range(len(stages)):
                stages[i].handle_events(event)

def draw():
    pico2d.clear_canvas()
    global character
    global monster1

    for game_object in gameWorld.all_objects():
        if not game_object.isActive:
            continue
        game_object.Draw()

    pico2d.update_canvas()
    pass

def update():
    for game_object in gameWorld.all_objects():
        if not game_object.isActive:
            continue
        game_object.update()

    for a, b, group in gameWorld.all_collision_pairs():
        if map_collide(a, b):
            a.map_handle_collision(b, group)
            b.handle_collision(a, group)

    for a, b, group in gameWorld.all_collision_pairs():
        if collide(a, b):
            a.handle_collision(b, group)
            b.handle_collision(a, group)

    pass

def pause():
    pass

def resume():
    pass


def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas(800, 610)
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면
    test_self()
