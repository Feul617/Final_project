from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Stage.MainStage import *


class Stage1_4(MainStage):

    def __init__(self):
        super(Stage1_4, self).__init__()
        self.stage = 4
        self.name = 'Stage4'
        self.isActive = False

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-4 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        #Camera.mainCamera.transform.position.y -= 610
        self.transform.position.y = int(self.background.transform.position.y)

        # monster 초기화
        self.monsters = [Monsta() for _ in range(4)]
        for zen_chan in self.monsters:
            zen_chan.name = 'monsta'
            zen_chan.isActive = False

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
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(140, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(480, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(60, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(550, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2.5층 중앙 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(340, 325 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2.5층 중앙 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(450, 325 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(5, self.stage)
        tile.MakeTile(60, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(5, self.stage)
        tile.MakeTile(620, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3.5층 중앙 왼쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(290, 390 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3.5층 중앙 오른쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(470, 390 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(60, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 중앙 왼쪽 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(220, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 중앙 오른쪽 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(510, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 오른쪽 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(660, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)