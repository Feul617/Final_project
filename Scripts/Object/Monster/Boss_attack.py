from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Character import Character

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

# 직선운동 공식 (1 - u)p1 + u * p2
class Boss_attack(Object):
    def __init__(self, this):
        super(Boss_attack, self).__init__()
        self.name = 'Boss_attack'
        self.transform.position = this.transform.position.Copy()

        self.image = load_image('./character/Boss_attack.png')
        self.image_Type = [0, 0, 17, 17]
        self.transform.scale *= 3

        self.target_position = Character.Instance.transform.position
        self.frame = 0
        self.frame_set = 4.0
        norm = Vector2.Normalize(self.target_position -self.transform.position)
        self.target_position += norm* 100000

        self.speed = 6
        self.this = this

        Object.gameWorld.add_object(self, 3)
        Object.gameWorld.add_collision_group(self, None, 'Boss_attack:character')

    def update(self):
        if self.transform.position.x < 80 or self.transform.position.x > 720 or self.transform.position.y < 0 or self.transform.position.y > 550:
            Object.gameWorld.remove_object(self)

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.image_Type[0] = int(self.frame) * 17
        self.transform.Look_At_Target(self.target_position, self.speed)
        pass

    def get_bb(self):
        return self.transform.position.x - 25, self.transform.position.y - 25, self.transform.position.x + 25, self.transform.position.y + 25

    def handle_collision(self, other, group):
        if group == 'Boss_attack:character':
            Object.gameWorld.remove_object(self)
