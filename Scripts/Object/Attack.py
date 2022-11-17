from Scripts.FrameWork.FrameWork_AFX import *


PIXEL_PER_METER = (10.0 / 0.3)
SHOOT_SPEED_KMPH = 300.0 # km/h 마라토너의 평속
SHOOT_SPEED_MPM = SHOOT_SPEED_KMPH * 1000 / 60.0
SHOOT_SPEED_MPS = SHOOT_SPEED_MPM / 60.0
SHOOT_SPEED_PPS = SHOOT_SPEED_MPS * PIXEL_PER_METER
UP_SPEED_PPS = 10.0 * 1000 / 60.0 / 60.0 * PIXEL_PER_METER

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 4
PONG_PER_ACTION = 0.01

class Bubble(Object):
    def __init__(self, x = 400, y = 300, velocity = 1):
        super(Bubble, self).__init__()
        self.image = load_image('./character/attack.png')
        self.transform.position.x,\
        self.transform.position.y, \
        self.velocity = x, y, velocity

        self.frame = 0
        self.delay = 0
        self.holding_time = 0
        self.is_up = 1

        self.state = 1 # 1: 공격 / 2: 상승하는 방울 / 3: 퐁

        self.start_x = x

        self.transform.scale.x = 2


    def update(self):
        self.image_Type = [int(self.frame) * 17, 0, 15, 50]
        self.transform.position.x += SHOOT_SPEED_KMPH * game_framework.frame_time * self.velocity

        if self.transform.position.x - self.start_x > 150:
            if self.velocity != 0:
                self.image = load_image('./character/bubble.png')
                self.state = 2
            self.velocity = 0

            self.transform.position.y += UP_SPEED_PPS * game_framework.frame_time * self.is_up
            self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3.0

            pass

        if abs(self.start_x - self.transform.position.x) >= 80:
            pass

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 6.0

        self.transform.position.x = clamp(80, self.transform.position.x, 720)
        if self.transform.position.x == 80 or self.transform.position.x == 720:
            self.pong()

        if self.transform.position.y >= 530:
            self.is_up = 0
            self.holding_time += 1

            if self.holding_time >= 1500:
                self.pong()


    def get_bb(self):
        return self.transform.position.x - 9, self.transform.position.y - 10, self.transform.position.x + 9, self.transform.position.y + 10
        pass

    def tile_get_bb(self):
        return self.transform.position.x - 9, self.transform.position.y - 10, self.transform.position.x + 9, self.transform.position.y + 10


    def pong(self):
        self.state = 3
        self.image = load_image('./character/pong.png')
        self.frame = (self.frame + FRAME_PER_ACTION * PONG_PER_ACTION * game_framework.frame_time) % 2.0
        self.delay += 1

        if self.delay >= 40:
            remove_object(self)

    def handle_collision(self, other, group):
        if group == 'attack:monster':
            remove_object(self)

    def map_handle_collision(self, other, group):
        pass