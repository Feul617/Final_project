from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Stage.MainStage import *


class Stage1_3(MainStage):
    def __init__(self):
        super(Stage1_3, self).__init__()
        self.stage = 3
        self.name = 'Stage3'
        self.isActive = False

        # 객채 초기화

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-3 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        #Camera.mainCamera.transform.position.y -= 610
        self.transform.position.y = int(self.background.transform.position.y)

        # monster 초기화
        self.monsters = [Monsta() for _ in range(4)]
        for zen_chan in self.monsters:
            zen_chan.name = 'monsta'

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(50, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(5, self.stage)
        tile.MakeTile(340, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(580, 30 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(120, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 1층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(450, 133 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[0].transform.position = Vector2(460, 163 - (self.height * (self.stage - 1)))

        # 2층 타일
        tile = MakeTile_X(18, self.stage)
        tile.MakeTile(160, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[1].transform.position = Vector2(160, 270 - (self.height * (self.stage - 1)))

        # 3층 타일
        tile = MakeTile_X(18, self.stage)
        tile.MakeTile(60, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 타일
        tile = MakeTile_X(18, self.stage)
        tile.MakeTile(160, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[2].transform.position = Vector2(500, 480 - (self.height * (self.stage - 1)))
        self.monsters[3].transform.position = Vector2(580, 480 - (self.height * (self.stage - 1)))

