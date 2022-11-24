from Scripts.Object.Object_AFX import *
from Scripts.Object.Monster import Monster
from Scripts.FrameWork.Camera import Camera

class MainStage(Object):
    monster_count = 0
    def __init__(self):
        super(MainStage, self).__init__()
        # self.background = Object()
        # self.background.image = load_image('./map/stage1 Fairy_land map_temp.png')
        # self.background.transform.position = Vector2(800//2, 600//2)
        # self.frame = 610
        # self.stage = 5
        # self.background.image_Type = [0, self.stage * self.frame, 800, 600]
        # self.tiles = []
        self.nextStage = None

        #몬스터
        self.zen_chan = [Monster() for i in range(4)]
        for i in range(4):
            self.zen_chan[i].name = 'zen_chan'
            self.zen_chan[i].count += 1

    def update(self):
        self.background.image_Type = [0, self.stage * self.frame, 800, 600]

    def Draw(self):
        pass
    def handle_events(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            self.frame -= 600