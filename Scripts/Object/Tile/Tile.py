from Scripts.FrameWork.FrameWork_AFX import *


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
        tile.image = load_image('./map/Tile/stage1-1 scaffolding_left.png')
        tile.image_Type = [0, 0, 18, 32]
    elif index == 1:
        tile.image = load_image('map/Tile/stage1-1 scaffolding_middle.png')
        tile.image_Type = [0, 0, 36, 32]
    elif index == 2:
        tile.image = load_image('map/Tile/stage1-1 scaffolding_right.png')
        tile.image_Type = [0, 0, 18, 32]

    return tile

class MakeTile_X(Object):

    def __init__(self, lenth):
        super(MakeTile_X, self).__init__()
        # 객체 초기화
        self.lenth = lenth
        self.tiles = []
        self.tiles.append(TileType(0))
        for i in range(1, lenth - 1):
            self.tiles.append(TileType(1))
        self.tiles.append(TileType(2))

    def MakeTile(self, x, y):
        Pos = Vector2(x, y)
        self.tiles[0].transform.position.x = Pos.x  # pivot
        self.tiles[1].transform.position.x = Pos.x + 27
        for i in range(2, self.lenth - 1):
            self.tiles[i].transform.position.x += self.tiles[i-1].transform.position.x + 36
        self.tiles[self.lenth - 1].transform.position.x = self.tiles[self.lenth - 2].transform.position.x + 27

        for i in range(self.lenth):
            self.tiles[i].transform.position.y = Pos.y
    pass