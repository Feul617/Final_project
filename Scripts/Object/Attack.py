from Scripts.FrameWork.FrameWork_AFX import *


PIXEL_PER_METER = (10.0 / 0.3)
SHOOT_SPEED_KMPH = 300.0 # km/h 마라토너의 평속
SHOOT_SPEED_MPM = SHOOT_SPEED_KMPH * 1000 / 60.0
SHOOT_SPEED_MPS = SHOOT_SPEED_MPM / 60.0
SHOOT_SPEED_PPS = SHOOT_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 4

class Bubble(Object):
    def __init__(self, x = 400, y = 300, velocity = 1):
        super(Bubble, self).__init__()
        self.image = load_image('./character/attack.png')
        self.transform.position.x,\
        self.transform.position.y, \
        self.velocity = x, y, velocity

        self.frame = 0

        self.start_x = None

        self.transform.scale.x = 2



    def update(self):
        self.image_Type = [int(self.frame) * 17, 0, 15, 50]
        self.transform.position.x += SHOOT_SPEED_KMPH * game_framework.frame_time * self.velocity

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6.0

        self.transform.position.x = clamp(80, self.transform.position.x, 720)
        if self.transform.position.x == 80 or self.transform.position.x == 720:
            remove_object(self)

    def get_bb(self):
        pass
