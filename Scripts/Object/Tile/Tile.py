from Scripts.FrameWork.Object import *



class Tile(Object):

    def __init__(self):
        super(Tile, self).__init__()
        pass

    def __del__(self):
        pass

    def collide(self, index):
        if index == 1:
            return self.transform.position.x - 18, self.transform.position.y + 32, self.transform.position.x + 18, self.transform.position.y + 32
        elif index == 0 or index == 2:
            return self.transform.position.x - 9, self.transform.position.y + 32, self.transform.position.x + 9, self.transform.position.y + 32
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