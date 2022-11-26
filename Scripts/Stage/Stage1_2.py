
from Scripts.Stage.MainStage import *


class Stage1_2(MainStage):

    def __init__(self):
        super(Stage1_2, self).__init__()
        self.stage = 2
        self.isActive = False

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-2 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 610 * 4, 800, 610]

        #Camera.mainCamera.transform.position.y -= 610

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(62, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(330, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(580, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(120, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 중앙 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(380, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 오른쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(525, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 왼쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(140, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(450, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(140, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(450, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(140, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 오른쪽 타일
        tile = MakeTile_X(8, self.stage)
        tile.MakeTile(450, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)