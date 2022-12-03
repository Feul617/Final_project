from Scripts.Object.Object_AFX import *
from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.FrameWork.Camera import Camera
from Scripts.Object.Character import Character
from Scripts.Object.Monster.Monster import Monster

class MainStage(Object):
    is_Next = False
    def __init__(self):
        super(MainStage, self).__init__()
        self.background = Object()
        self.black_background = Object()
        self.bgm = load_music('./sound/Introduction _ Main Theme.mp3')
        self.bgm.set_volume(10)
        self.bgm.repeat_play()
        self.tiles = []

        self.height = 610

        self.nextStage = None

        self.in_Main_character = None

        #몬스터
        self.monsters = []

        Object.gameWorld.add_object(self.background, 2)
        Object.gameWorld.add_object(self.black_background, 0)
        Object.gameWorld.add_object(self, 0)

        Camera.mainCamera.transform.position.y = 0

    def Disable(self):
        for monster in self.monsters:
            monster.SetActive(True)
        pass

    def Enable(self):
        for monster in self.monsters:
            monster.SetActive(False)
        pass

    def update(self):
        if Monster.monster_count <= 0:
            MainStage.is_Next = True

        if MainStage.is_Next:
            Character.Instance.is_Next = True
            Camera.mainCamera.transform.position.y -= game_framework.frame_time * 300
            if Camera.mainCamera.transform.position.y < self.nextStage.transform.position.y - self.height / 2:
                Camera.mainCamera.transform.position.y = self.nextStage.transform.position.y - self.height / 2
                MainStage.is_Next = False
                Character.Instance.is_Next = False
                Monster.monster_count = 8
                self.SetActive(False)
                self.nextStage.SetActive(True)

    def Draw(self):
        pass

    def handle_events(self, event):
        pass

