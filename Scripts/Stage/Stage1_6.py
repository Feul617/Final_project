from Scripts.Stage.MainStage import *


class Stage1_6(MainStage):

    def __init__(self):
        super(Stage1_6, self).__init__()
        self.stage = 6
        self.isActive = False

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-6 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        #Camera.mainCamera.transform.position.y -= 610

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(20, self.stage)
        tile.MakeTile(60, 35 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(135, 140 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 중앙 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(390, 140 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(640, 140 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(215, 245 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 중앙 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(390, 245 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(560, 245 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(140, 350 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 중앙 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(390, 350 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(635, 350 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(215, 455 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(560, 455 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)