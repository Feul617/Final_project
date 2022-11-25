
from Scripts.Stage.MainStage import *


class Stage1_2(MainStage):

    def __init__(self):
        super(Stage1_2, self).__init__()
        self.stage = 2
        self.isActive = True

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-2 bg.png')
        self.background.transform.position = Vector2(800 // 2, 600 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 600]

        Camera.mainCamera.transform.position.y -= 600

    def handle_events(self, event):
        pass

    def Init(self):
        if self.isActive:
            # 공용 타일
            tile = MakeTile_X(6, self.stage)
            tile.MakeTile(62, 33 - self.height)
            self.tiles.append(tile)

            tile = MakeTile_X(6, self.stage)
            tile.MakeTile(330, 33)
            self.tiles.append(tile)

            tile = MakeTile_X(6, self.stage)
            tile.MakeTile(580, 33)
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