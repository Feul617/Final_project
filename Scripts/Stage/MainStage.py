from Scripts.Object.Object_AFX import *


class MainStage:
    def __init__(self):
        self.background = Object()
        self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        self.background.transform.position = Vector2(800//2, 600//2)
        self.frame = 5
        self.background.image_Type = [0, self.frame * 590, 800, 600]
        self.tiles = []


    def Tile_init(self):
        #1층 왼쪾 타일
        tile = MakeTile_X(10)
        tile.MakeTile(50, 50)
        self.tiles.append(tile)

        #1층 오른쪽 타일
        tile = MakeTile_X(10)
        tile.MakeTile(400, 50)
        self.tiles.append(tile)
    pass