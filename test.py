from Scripts.Object.Object_AFX import *

open_canvas()

tile_01 = None
tile_02 = None

RenderList = None

def e():
    global RenderList
    global stage1_1, tile_02

    RenderList = []

    stage1_1 = MainStage()
    stage1_1.Tile_init()

    #character = Character()

    RenderList.append(stage1_1.background)
    for tile in stage1_1.tiles:
        RenderList += tile.tiles

    pass

def d():
    global RenderList

    for obj in RenderList:
        obj.Draw()

    update_canvas()
    pass

e()
d()

delay(2)