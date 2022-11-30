import random
from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.FrameWork.Camera import Camera

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
    monster_count = 4
    def __init__(self , depth = 2):
        super(Monster, self).__init__()
        # 이미지 초기화
        self.frame = 0
        self.frame_set = 4.0
        self.dir = 1
        self.dir_y = 1
        self.flip = ' '
        self.name = ' '
        self.image = load_image('./character/monster2.png')
        self.image_Type = [0, 0, 0, 0]

        # 상태
        self.state = 'init' # 0:init / 1:in bubble / 2:death
        self.type = 0
        self.in_bubble = 0
        self.is_up = False
        self.time = 0

        self.gravity = 0
        self.start_delay = 50

        # 인공지능
        self.patrolDistance = [0, 0]

        #충돌 처리
        Object.gameWorld.add_object(self, depth)
        Object.gameWorld.add_collision_group(self, None, 'monster:tile')
        Object.gameWorld.add_collision_group(None, self, 'attack:monster')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'

        self.gravity = game_framework.frame_time * 60
        if self.start_delay > 0:
            self.start_delay -= 1
        if self.start_delay <= 0:
            self.transform.position.y -= self.gravity

        match self.name:
            case 'zen_chan':
                self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
                self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

            # case 'mighti':
            #     self.gravity = 0
            #     self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
            #     self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            #     self.transform.position.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
            #
            # case 'monsta':
            #     pass

        self.Monster_type()
        self.image_Type = [(int(self.frame) + self.in_bubble) * 54, self.type, 54, 54]
        self.Move()
        self.floating()

    def get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 27 - Camera.mainCamera.transform.position.y, \
               self.transform.position.x + 20, self.transform.position.y + 27 - Camera.mainCamera.transform.position.y

    def tile_get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 20 - Camera.mainCamera.transform.position.y, \
               self.transform.position.x + 20, self.transform.position.y - 15 - Camera.mainCamera.transform.position.y

    def handle_collision(self, other, group):
        if group == 'character:monster':
            if self.state == 'bubble':
                self.state = 'death'
                match self.name:
                    case 'zen_chan':
                        self.in_bubble = 12
                        self.frame_set = 4.0
                        self.is_up = False
                        self.transform.position.y -= self.gravity * 5

                    case 'mighta':

                        pass

        elif group == 'attack:monster':
            if self.state == 'init' and other.state == 1:
                self.state = 'bubble'
                self.dir = 0
                self.is_up = True
                if self.name == 'zen_chan':
                    print('attack')
                    print(other.transform.position.x)
                    self.in_bubble = 16
                    self.frame_set = 3.0
                elif self.name == 'might':
                    pass

    def map_handle_collision(self, other, group):
        if group == 'monster:tile':
            match self.name:
                case 'zen_chan':
                    if self.state == 'init':
                        self.transform.position.y += self.gravity
                        #self.gravity = 0

                    elif self.state == 'death':
                        self.start_timer()
                        self.gravity = 0
                        self.frame_set = 1.0
                        self.in_bubble = 12

                case 'mighta':
                    if self.state == 'death':
                        self.start_timer()
                        self.gravity = 0
                        self.frame_set = 1.0
                        self.in_bubble = 29

                case 'monsta':
                    if self.state == 'init':
                        self.transform.position.y += self.gravity
                    elif self.state == 'death':
                        self.start_timer()
                        self.gravity = 0
                        self.frame_set = 1.0

    def Monster_type(self):
        match self.name:
            case 'zen_chan':
                self.type = 810

            case 'mighta':
                self.type = 700

    def floating(self):
        if self.transform.position.y < 540 + Camera.mainCamera.transform.position.y and self.is_up:
            self.transform.position.y += self.gravity * 3
        elif self.transform.position.y >= 540 + Camera.mainCamera.transform.position.y:
            self.transform.position.y += self.gravity
            self.is_up = False


    def start_timer(self):
        self.time += 1
        if self.time >= 10:
            Monster.monster_count -= 1
            Object.gameWorld.remove_object(self)

    def Move(self):
        self.transform.position.x = clamp(self.patrolDistance[0], self.transform.position.x, self.patrolDistance[1])
        if self.transform.position.x == self.patrolDistance[0] or self.transform.position.x == self.patrolDistance[1]:
            self.dir *= -1
        pass


class Make_Monster(Object):
    def __init__(self):
        super(Make_Monster, self).__init__()