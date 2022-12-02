from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.FrameWork.Camera import Camera

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 15.0 # km/h 마라토너의 평속
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER
UP_SPEED_PPS = 10.0 * 1000 / 60.0 / 60.0 * PIXEL_PER_METER

TIME_PER_ACTION = 2.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

class Monster(Object):
    monster_count = 8
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
        self.image_Type = [0, 0, 54, 54]
        self.size = 0

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
        self.isActive = False

        #충돌 처리
        Object.gameWorld.add_object(self, depth)
        Object.gameWorld.add_collision_group(self, None, 'monster:tile')
        Object.gameWorld.add_collision_group(None, self, 'attack:monster')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):

        # if self.start_delay > 0:
        #     self.start_delay -= 1
        # if self.start_delay <= 0:
        #     self.transform.position.y -= self.gravity

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set

        self.image_Type = [(int(self.frame) + self.in_bubble) * self.size, self.type, 54, 54]
        self.floating()

    def get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 27 - Camera.mainCamera.transform.position.y, \
               self.transform.position.x + 20, self.transform.position.y + 27 - Camera.mainCamera.transform.position.y

    def tile_get_bb(self):
        return self.transform.position.x - 20, self.transform.position.y - 20 - Camera.mainCamera.transform.position.y, \
               self.transform.position.x + 20, self.transform.position.y - 15 - Camera.mainCamera.transform.position.y

    def handle_collision(self, other, group):
        pass

    def map_handle_collision(self, other, group):
        pass

    def floating(self):
        if self.transform.position.y < 541 + Camera.mainCamera.transform.position.y and self.is_up:
            self.transform.position.y += self.gravity * 3
        elif self.transform.position.y >= 540 + Camera.mainCamera.transform.position.y:
            self.transform.position.y += self.gravity
            self.is_up = False


    def start_timer(self):
        self.time += 1
        if self.time <= 10:
            Monster.monster_count -= 1
            Object.gameWorld.remove_object(self)

    def Patrol(self):
        self.transform.position.x = clamp(self.patrolDistance[0], self.transform.position.x, self.patrolDistance[1])
        if self.transform.position.x == self.patrolDistance[0] or self.transform.position.x == self.patrolDistance[1]:
            self.dir *= -1

    def Move(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'

        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

    def Gravity(self):
        self.gravity = game_framework.frame_time * 60
        pass