from Scripts.FrameWork.FrameWork_AFX import *

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0 # km/h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

class Monster(Object):
    def __init__(self):
        super(Monster, self).__init__()
        self.frame = 0
        self.dir = 1
        self.flip = ' '
        self.name = None
        self.image = load_image('./character/monster2.png')

    def update(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7.0
        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60

    def name_type(self):
        if self.name == 'zen_chan':
            self.image_Type = [0, 800, 40, 60]

    def handle_collide(self):
        pass

def Monster_Type(index):
    monster = Monster()

    if index == 0:
        monster.image_type = [0, 500, 52, 52]
    elif index == 1:
        monster.image_type = [0, 450, 52, 52]


class Make_Monster(Object):
    def __init__(self):
        super(Make_Monster, self).__init__()