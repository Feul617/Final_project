from Scripts.Object.Tile.Tile import *
from Scripts.Object.Character import  *

open_canvas()

tile_01 = None
tile_02 = None
character = None

RenderList = None

def e():
    global RenderList
    global tile_01, tile_02, character

    RenderList = []

    tile_01 = TileType(0)
    tile_02 = TileType(1)
    tile_01.transform.position.x = 400
    tile_01.transform.position.y = 50

    character = Character()


    RenderList += [tile_01, tile_02]

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