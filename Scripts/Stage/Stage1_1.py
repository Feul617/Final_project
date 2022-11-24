from Scripts.Stage.MainStage import *

class Stage1_1(MainStage):
    def __init__(self):
        super(Stage1_1, self).__init__()
        self.background = Object()
        self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        self.background.transform.position = Vector2(800 // 2, 600 // 2)
        self.frame = 610
        self.stage = 2
        self.background.image_Type = [0, self.stage * self.frame, 800, 600]
        self.tiles = []
        self.frame_move_time = 0
        self.is_Next = False


        Object.gameWorld.add_object(self.background, 0)
        Object.gameWorld.add_object(self, 0)

    def update(self):
        self.background.image_Type = [0, self.stage * self.frame, 800, 600]
        if MainStage.monster_count == 0 and self.frame_move_time >= 100:
            self.frame += 10

        self.frame_move_time += 1
        if self.frame_move_time >= 100:
            self.frame_move_time = 0

        if Monster.monster_count == 0:
            self.is_Next = True
            Monster.monster_count = 4
            self.nextStage.isActive = True

        if self.is_Next:
            Camera.mainCamera.transform.position.y += game_framework.frame_time

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
        self.zen_chan[0].transform.position = Vector2(120, 280)
        self.zen_chan[0].patrolPos = Vector2(130, 305)

        self.tiles.append(tile)

        # 2층 오른쪽 타일
        tile = MakeTile_X(7, self.stage)
        tile.MakeTile(490, 240)
        self.zen_chan[1].transform.position = Vector2(490, 280)
        self.zen_chan[1].patrolPos = Vector2(500, 675)
        self.tiles.append(tile)

        # 3층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(200, 345)
        self.zen_chan[2].transform.position = Vector2(200, 380)
        self.zen_chan[2].patrolPos = Vector2(215, 370)
        self.tiles.append(tile)

        # 3층 오른쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(450, 345)
        self.zen_chan[3].transform.position = Vector2(450, 380)
        self.zen_chan[3].patrolPos = Vector2(460, 615)
        self.tiles.append(tile)

        # 4층 왼쪽 타일
        tile = MakeTile_X(6, self.stage)
        tile.MakeTile(200, 450)
        self.tiles.append(tile)