from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.FrameWork.Camera import Camera

class Tile(Object):
    def __init__(self):
        super(Tile, self).__init__()
        Object.gameWorld.add_object(self, 1)
        pass

    def __del__(self):
        pass
    pass

def TileType(index):
    tile = Tile()
    if index == 0:
        tile.image = load_image('map/Tile/stage1-1 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    elif index == 1:
        tile.image = load_image('map/Tile/stage1-2 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    elif index == 2:
        tile.image = load_image('map/Tile/stage1-3 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    elif index == 3:
        tile.image = load_image('map/Tile/stage1-4 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    elif index == 4:
        tile.image = load_image('map/Tile/stage1-5 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    elif index == 5:
        tile.image = load_image('map/Tile/stage1-6 middle_tile.png')
        tile.image_Type = [0, 0, 36, 32]

    return tile


class MakeTile_X(Object):
    def __init__(self, lenth, stage):
        super(MakeTile_X, self).__init__()
        # 객체 초기화
        self.lenth = lenth
        self.tiles = []
        for i in range(lenth):
            self.tiles.append(TileType(stage - 1))

        # self.tiles.append(TileType(3 * stage - 3))
        # for i in range(1, lenth - 1):
        #     self.tiles.append(TileType(3 * stage - 2))
        # self.tiles.append(TileType(3 * stage - 1))

        # collision Box 크기
        self.collisionBox = [30, 20]
        self.tile_collisionBox = [30, 23, 30, 15]

        Object.gameWorld.add_object(self, 5)
        Object.gameWorld.add_collision_group(None, self, 'character:tile')
        Object.gameWorld.add_collision_group(None, self, 'monster:tile')

    def MakeTile(self, x, y):
        Pos = Vector2(x, y)
        self.tiles[0].transform.position.x = Pos.x  # pivot
        for i in range(1, self.lenth):
            self.tiles[i].transform.position.x = self.tiles[i-1].transform.position.x + 36
        # self.tiles[1].transform.position.x = Pos.x + 27
        # for i in range(2, self.lenth - 1):
        #     self.tiles[i].transform.position.x += self.tiles[i-1].transform.position.x + 36
        # if self.lenth <= 2:
        #     self.tiles[self.lenth - 1].transform.position.x = self.tiles[self.lenth - 2].transform.position.x + 18
        # else:
        #     self.tiles[self.lenth - 1].transform.position.x = self.tiles[self.lenth - 2].transform.position.x + 27

        for i in range(self.lenth):
            self.tiles[i].transform.position.y = Pos.y

    def get_bb(self):
        return self.tiles[0].transform.position.x + 4, self.tiles[0].transform.position.y - Camera.mainCamera.transform.position.y, \
        self.tiles[0].transform.position.x + ((self.lenth - 1) * 36), self.tiles[0].transform.position.y + 8 - Camera.mainCamera.transform.position.y
        pass

    def Draw(self):
        pass

    def handle_collision(self, other, group):
        pass
    pass

class Make_Wall(Object):
    def __init__(self):
        super(Make_Wall, self).__init__()

