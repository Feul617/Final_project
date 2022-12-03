from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Character import Character
from Scripts.FrameWork.Camera import Camera
import schedule
import time

class UI(Object):
    def __init__(self):
        super(UI, self).__init__()
        self.font = load_font('./map/Background/ENCR10B.TTF', 30)
        self.time = 0
        schedule.every(1).second.do(self.Timer)

    def update(self):
        schedule.run_pending()
        pass

    def Draw(self):
        self.font.draw(40, 590, 'SCORE:%d' % (Character.Instance.score), (255, 255, 0))
        self.font.draw(330, 590, 'TIME:%d' % (self.time), (0, 0, 255))
        self.font.draw(600, 590, 'LIFE:%d' % (Character.Instance.life / 2), (0, 255, 0))

        pass

    def Timer(self):
        self.time += 1


