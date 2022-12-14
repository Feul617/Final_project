from Scripts.Stage.MainStage import *
from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Object.Monster.MonsterContain import *


class Stage1_5(MainStage):

    def __init__(self):
        super(Stage1_5, self).__init__()
        self.stage = 5
        self.name = 'Stage5'
        self.isActive = False

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-5 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        self.black_background.image = load_image('./map/Background/background.png')
        self.black_background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.black_background.image_Type = [0, 0, 800, 610]

        #Camera.mainCamera.transform.position.y -= 610
        self.transform.position.y = int(self.background.transform.position.y)

        # monster 초기화
        self.monsters = [Mighta() for _ in range(4)]
        for zen_chan in self.monsters:
            zen_chan.name = 'mighta'

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(62, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(580, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 중앙 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(360, 95 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 왼쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(200, 200 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(550, 200 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(275, 245 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(3, self.stage)
        tile.MakeTile(480, 245 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(340, 285 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 오른쪽 타일
        tile = MakeTile_X(2, self.stage)
        tile.MakeTile(455, 285 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 5층 중앙 타일
        tile = MakeTile_X(4, self.stage)
        tile.MakeTile(360, 335 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 6층 중앙 타일
        tile = MakeTile_X(16, self.stage)
        tile.MakeTile(145, 455 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[0].transform.position = Vector2(200, 485 - (self.height * (self.stage - 1)))
        self.monsters[1].transform.position = Vector2(240, 485 - (self.height * (self.stage - 1)))
        self.monsters[2].transform.position = Vector2(560, 485 - (self.height * (self.stage - 1)))
        self.monsters[3].transform.position = Vector2(580, 485 - (self.height * (self.stage - 1)))

