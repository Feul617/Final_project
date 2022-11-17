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
        self.frame_set = 4.0
        self.dir = 1
        self.flip = ' '
        self.name = ' '
        self.image = load_image('./character/monster2.png')
        self.image_Type = [0, 0, 0, 0]

        self.state = 0 # 0:init / 1:in bubble
        self.type = 0
        self.count = 0
        self.in_bubble = 0

    def update(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        self.Monster_type()
        self.image_Type = [(int(self.frame) + self.in_bubble) * 55, self.type, 40, 60]

    def get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 30, \
               self.transform.position.x + 20, self.transform.position.y + 30


    def handle_collision(self, other, group):
        if group == 'character:monster':
            print('캐릭터충돌')
            self.count -= 1
            remove_object(self)
        elif group == 'attack:monster':
            if self.name == 'zen_chan':
                self.in_bubble = 16
                self.frame_set = 3.0

    def Monster_type(self):
        match self.name:
            case 'zen_chan':
                self.type = 800

            case 'mighta':
                self.type = 700


class Make_Monster(Object):
    def __init__(self):
        super(Make_Monster, self).__init__()