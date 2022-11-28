from Scripts.Object.Object_AFX import *
from Scripts.Object.Monster import Monster
from Scripts.FrameWork.Camera import Camera

class MainStage(Object):
    #monster_count = 0
    is_Next = False
    def __init__(self, monsterCount = 4):
        super(MainStage, self).__init__()
        self.background = Object()
        self.tiles = []

        self.height = 610

        #self.is_Next = False
        self.nextStage = None

        self.in_Main_character = None

        #몬스터
        self.zen_chan = [Monster() for i in range(monsterCount)]
        for zen_chan in self.zen_chan:
            zen_chan.name = 'zen_chan'
            zen_chan.count += 1
            zen_chan.isActive = False

        Object.gameWorld.add_object(self.background, 0)
        Object.gameWorld.add_object(self, 0)

        Camera.mainCamera.transform.position.y = 0

    def update(self):
        if Monster.monster_count == 0:
            MainStage.is_Next = True

        if MainStage.is_Next:
            Camera.mainCamera.transform.position.y -= game_framework.frame_time * 300
            if Camera.mainCamera.transform.position.y < self.nextStage.transform.position.y - self.height / 2:
                Camera.mainCamera.transform.position.y = self.nextStage.transform.position.y - self.height / 2
                MainStage.is_Next = False
                Monster.monster_count = 4
                self.nextStage.isActive = True

    def Draw(self):
        pass

    def handle_events(self, event):
        pass