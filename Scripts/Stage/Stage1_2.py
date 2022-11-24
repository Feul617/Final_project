
from Scripts.Stage.MainStage import *


class Stage1_2(MainStage):

    def __init__(self):
        super(Stage1_2, self).__init__()
        self.stage = 1
        self.isActive = False

        # 객채 초기화

        # background 초기화
        self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        self.background.transform.position = Vector2(800 // 2, 600 // 2 - 600)
        self.background.image_Type = [0, (6-self.stage) * self.frame, 800, 600]

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(62, 28)
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(330, 28)
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(580, 28)
        self.tiles.append(tile)

        # 1층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(165, 133)
        self.tiles.append(tile)

        # 1층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(450, 133)
        self.tiles.append(tile)

        # 2층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(120, 240)
        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(490, 240)
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(200, 345)
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(450, 345)
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(200, 450)
        self.tiles.append(tile)