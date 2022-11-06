from Scripts.Object.Object_AFX import *


class MainStage:
    def __init__(self):
        self.background = Object()
        self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        self.background.transform.position = Vector2(800//2, 600//2)
        self.frame = 5
        self.background.image_Type = [0, self.frame * 610, 800, 600]
        self.tiles = []


    def Tile_init(self):
        #1층 왼쪾 타일
        tile = MakeTile_X(7)
        tile.MakeTile(165, 133)
        self.tiles.append(tile)

        #1층 오른쪽 타일
        tile = MakeTile_X(7)
        tile.MakeTile(450, 133)
        self.tiles.append(tile)

        #2층 왼쪽 타일
        tile = MakeTile_X(7)
        tile.MakeTile(120, 240)
        self.tiles.append(tile)

        #2층 오른쪽 타일
        tile = MakeTile_X(7)
        tile.MakeTile(500, 240)
        self.tiles.append(tile)

        #3층 왼쪽 타일
        tile = MakeTile_X(6)
        tile.MakeTile(200, 345)
        self.tiles.append(tile)

        #3층 오른쪽 타일
        tile = MakeTile_X(6)
        tile.MakeTile(450, 345)
        self.tiles.append(tile)
    pass