from Scripts.Object.Object_AFX import *


class MainStage:
    def __init__(self):
        self.background = Object()
        self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        self.background.transform.position = Vector2(800//2, 600//2)
        self.frame = 6100000000000000000000000000000000000000000000000000000000000000000000000000000000000000
        self.stage = 5
        self.background.image_Type = [0, self.stage * self.frame, 800, 600]
        self.tiles = []

    def update(self):
        self.background.image_Type = [0, self.stage * self.frame, 800, 600]

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            self.frame -= 10


    def Tile_init(self, stage):
        #공용 타일
        tile = MakeTile_X(6, stage)
        tile.MakeTile(62, 28)
        self.tiles.append(tile)

        tile = MakeTile_X(6, stage)
        tile.MakeTile(330, 28)
        self.tiles.append(tile)

        tile = MakeTile_X(6, stage)
        tile.MakeTile(580, 28)
        self.tiles.append(tile)

        #1층 왼쪽 타일
        tile = MakeTile_X(7, stage)
        tile.MakeTile(165, 133)
        self.tiles.append(tile)

        #1층 오른쪽 타일
        tile = MakeTile_X(7, stage)
        tile.MakeTile(450, 133)
        self.tiles.append(tile)

        #2층 왼쪽 타일
        tile = MakeTile_X(7, stage)
        tile.MakeTile(120, 240)
        self.tiles.append(tile)

        #2층 오른쪽 타일
        tile = MakeTile_X(7, stage)
        tile.MakeTile(490, 240)
        self.tiles.append(tile)

        #3층 왼쪽 타일
        tile = MakeTile_X(6, stage)
        tile.MakeTile(200, 345)
        self.tiles.append(tile)

        #3층 오른쪽 타일
        tile = MakeTile_X(6, stage)
        tile.MakeTile(450, 345)
        self.tiles.append(tile)

    pass