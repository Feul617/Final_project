from Scripts.Object.Tile.Tile import MakeTile_X
from Scripts.Stage.MainStage import *
from Scripts.Object.Monster.MonsterContain import *


class Stage1_1(MainStage):
    def __init__(self):
        super(Stage1_1, self).__init__()
        self.stage = 1
        self.name = 'Stage1'
        self.isActive = True

        # for i in range(4):
        #     print('on')
        #     self.zen_chan[i].isActive = True

        # background 초기화
        self.background.image = load_image('./map/Background/stage1-1 bg.png')
        self.background.transform.position = Vector2(800 // 2, 610 // 2 - (self.height * (self.stage - 1)))
        self.background.image_Type = [0, 0, 800, 610]

        self.transform.position.y = int(self.background.transform.position.y)

        # monster 초기화
        self.monsters = [Zen_chan() for _ in range(4)]
        for zen_chan in self.monsters:
            zen_chan.name = 'zen_chan'
            zen_chan.isActive = True

    def handle_events(self, event):
        pass

    def Init(self):

        # 공용 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(62, 33)
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
        self.monsters[0].transform.position = Vector2(140, 280)
        self.monsters[0].patrolDistance = [130, 305]

        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(490, 240)
        self.monsters[1].transform.position = Vector2(490, 280)
        self.monsters[1].patrolDistance = [500, 675]
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(200, 345)
        self.monsters[2].transform.position = Vector2(200, 400)
        self.monsters[2].patrolDistance = [215, 370]
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(450, 345)
        self.monsters[3].transform.position = Vector2(450, 380)
        self.monsters[3].patrolDistance = [460, 615]
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(150, 450)
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(500, 450)
        self.tiles.append(tile)

