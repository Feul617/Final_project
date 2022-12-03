from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Stage.MainStage import *
from Scripts.Object.Monster.MonsterContain import *


class Stage1_2(MainStage):

    def __init__(self):
        super(Stage1_2, self).__init__()
        self.stage = 2
        self.name = 'Stage2'
        self.isActive = False


        # background 초기화
        self.background.image = load_image('./map/Background/stage1-2 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        self.black_background.image = load_image('./map/Background/background.png')
        self.black_background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.black_background.image_Type = [0, 0, 800, 610]

        self.transform.position.y = int(self.background.transform.position.y)
        #Camera.mainCamera.transform.position.y -= 610

        # monster 초기화
        self.monsters = [Zen_chan() for _ in range(4)]
        for zen_chan in self.monsters:
            zen_chan.name = 'zen_chan'

    def handle_events(self, event):
        pass

    def Init(self):
        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(62, 35 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(330, 35 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(580, 35 - (self.height * (self.stage - 1)))
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
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(140, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[0].transform.position = Vector2(140, 280  - (self.height * (self.stage - 1)))
        self.monsters[0].patrolDistance = [150, 340]

        # 2층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(450, 240 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[1].transform.position = Vector2(470, 280 - (self.height * (self.stage - 1)))
        self.monsters[1].patrolDistance = [450, 610]

        # 3층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(140, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(450, 345 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(140, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[2].transform.position = Vector2(140, 470 - (self.height * (self.stage - 1)))
        self.monsters[2].patrolDistance = [150, 340]

        # 4층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(450, 450 - (self.height * (self.stage - 1)))
        self.tiles.append(tile)
        self.monsters[3].transform.position = Vector2(140, 470 - (self.height * (self.stage - 1)))
        self.monsters[3].patrolDistance = [460, 650]