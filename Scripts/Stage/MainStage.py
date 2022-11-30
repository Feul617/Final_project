from Scripts.Object.Object_AFX import *
from Scripts.Object.Monster import Monster
from Scripts.FrameWork.Camera import Camera

class MainStage(Object):
    is_Next = False
    def __init__(self):
        super(MainStage, self).__init__()
        self.background = Object()
        self.tiles = []

        self.height = 610

        #self.is_Next = False
        self.nextStage = None

        self.in_Main_character = None

        #몬스터
        self.zen_chan = [Monster() for _ in range(8)]
        for zen_chan in self.zen_chan:
            zen_chan.name = 'zen_chan'
            zen_chan.isActive = False

        self.mighta = [Monster() for _ in range(4)]
        for mighta in self.mighta:
            mighta.name = 'mighta'
            mighta.isActive = False

        self.monsta = [Monster() for _ in range(8)]
        for monsta in self.monsta:
            monsta.name = 'monsta'
            monsta.isActive = False

        Object.gameWorld.add_object(self.background, 0)
        Object.gameWorld.add_object(self, 0)

        Camera.mainCamera.transform.position.y = 0

    def update(self):
        if Monster.monster_count <= 0:
            MainStage.is_Next = True

        if MainStage.is_Next:
            Camera.mainCamera.transform.position.y -= game_framework.frame_time * 300
            if Camera.mainCamera.transform.position.y < self.nextStage.transform.position.y - self.height / 2:
                Camera.mainCamera.transform.position.y = self.nextStage.transform.position.y - self.height / 2
                MainStage.is_Next = False
                Monster.monster_count = 4
                self.isActive = False
                self.nextStage.isActive = True
                #print(self.nextStage.transform.position.y)
                #print(Camera.mainCamera.transform.position.y)
    def Draw(self):
        pass

    def handle_events(self, event):
        pass