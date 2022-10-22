from Scripts.Object.Tile.Tile import *

open_canvas()

tile_01 = None
tile_02 = None

RenderList = None

def e():
    global RenderList
    global tile_01, tile_02

    RenderList = []

    tile_01 = TileType(0)
    tile_02 = TileType(1)

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