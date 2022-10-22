from Scripts.FrameWork.Object import *


class Tile(Object):

    def __init__(self):
        super(Tile, self).__init__()
        pass

    def __del__(self):
        pass

    pass

def TileType(index):
    tile = Tile()
    if index == 0:
        tile.image = load_image('map/Tile/stage1-1 scaffolding_left.png')
        tile.image_Type = [0, 0, 18, 32]
    elif index == 1:
        tile.image = load_image('map/Tile/stage1-1 scaffolding_middle.png')
        tile.image_Type = [0, 0, 36, 32]
    elif index == 2:
        tile.image = load_image('map/Tile/stage1-1 scaffolding_right.png')
        tile.image_Type = [0, 0, 18, 32]

    return tile