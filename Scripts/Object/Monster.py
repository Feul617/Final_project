import random

from Scripts.FrameWork.FrameWork_AFX import *

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 30.0 # km/h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
UP_SPEED_PPS = 10.0 * 1000 / 60.0 / 60.0 * PIXEL_PER_METER

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

        self.state = 0 # 0:init / 1:in bubble / 2:death
        self.type = 0
        self.count = 0
        self.in_bubble = 0
        self.is_up = False
        self.time = 0

        self.gravity = 3
        self.start_delay = 0


    def update(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.start_delay < 200:
            self.start_delay += 1
        if self.start_delay >= 200:
            self.transform.position.y -= UP_SPEED_PPS * game_framework.frame_time * self.gravity * 2
        self.Monster_type()
        self.image_Type = [(int(self.frame) + self.in_bubble) * 54, self.type, 54, 54]

        self.floating()

    def get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 27, \
               self.transform.position.x + 20, self.transform.position.y + 27

    def tile_get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 20, \
               self.transform.position.x + 20, self.transform.position.y - 15

    def handle_collision(self, other, group):
        if group == 'character:monster':
            if self.state == 1:
                self.state = 2
                match self.name:
                    case 'zen_chan':
                        self.in_bubble = 12
                        self.frame_set = 4.0
                        self.is_up = False
                        self.gravity = 2

        elif group == 'attack:monster':
            if self.state == 0 and other.state == 1:
                self.state = 1
                self.dir = 0
                self.is_up = True
                if self.name == 'zen_chan':
                    self.in_bubble = 16
                    self.frame_set = 3.0

    def map_handle_collision(self, other, group):
        if group == 'monster:tile':
            if self.state == 0:
                self.gravity = 0
            elif self.state == 2:
                self.start_timer()
                self.gravity = 0
                self.frame_set = 1.0
                self.in_bubble = 12

    def Monster_type(self):
        match self.name:
            case 'zen_chan':
                self.type = 810

            case 'mighta':
                self.type = 700

    def floating(self):
        if self.transform.position.y < 540 and self.is_up:
            self.transform.position.y += UP_SPEED_PPS * game_framework.frame_time * 2
        elif self.transform.position.y >= 540:
            self.is_up = False


    def start_timer(self):
        self.time += 1
        if self.time >= 1000:
            remove_object(self)


class Make_Monster(Object):
    def __init__(self):
        super(Make_Monster, self).__init__()