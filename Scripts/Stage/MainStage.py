from Scripts.Object.Object_AFX import *
from Scripts.Object.Monster import Monster
from Scripts.FrameWork.Camera import Camera

class MainStage(Object):
    monster_count = 0
    def __init__(self,):
        super(MainStage, self).__init__()
        self.background = Object()
        self.tiles = []

        self.height = 610

        self.is_Next = False
        self.nextStage = None

        self.character = None

        #몬스터
        self.zen_chan = [Monster() for i in range(4)]
        for i in range(4):
            self.zen_chan[i].name = 'zen_chan'
            self.zen_chan[i].count += 1

        Object.gameWorld.add_object(self.background, 0)
        Object.gameWorld.add_object(self, 0)

    def update(self):
        if Monster.monster_count == 0:
            self.is_Next = True
            Monster.monster_count = 4
            self.nextStage.isActive = True

        if self.is_Next:
            Camera.mainCamera.transform.position.y += game_framework.frame_time
            self.character.transform.position.y += Camera.mainCamera.transform.position.y
            if self.nextStage.transform.position >= Camera.mainCamera.transform.position:
                self.is_Next = False

    def Draw(self):
        pass

    def handle_events(self, event):
        if event.type == SDL_KEYDOWN and event.key == SDLK_a:
            self.frame -= 600