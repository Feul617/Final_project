from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Monster.Monster import *

MONSTA_SPEED_PPS = 3 * 1000 / 60.0 / 60.0 * PIXEL_PER_METER
class Monsta(Monster):
    def __init__(self):
        super(Monsta, self).__init__()
        self.name = 'monsta'
        self.frame_set = 2
        self.image_Type[1] = 570
        self.type = 570
        self.size = 54
        self.patrolDistance = [80, 720]

        Object.gameWorld.add_object(self, 2)
        Object.gameWorld.add_collision_group(self, None, 'monster:tile')
        Object.gameWorld.add_collision_group(None, self, 'attack:monster')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'

        if self.state == 'init':
            self.gravity = game_framework.frame_time * 300

        self.transform.position.y -= self.gravity

        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.transform.position.x += self.dir * MONSTA_SPEED_PPS * game_framework.frame_time * 5

        self.image_Type = [(int(self.frame) + self.in_bubble) * self.size, self.type, 54, 54]
        self.floating()
        self.Patrol()

        if self.transform.position.y < -10 + Camera.mainCamera.transform.position.y:
            print(self.transform.position.y)
            print(Camera.mainCamera.transform.position.y)
            self.gravity = 0
            self.transform.position.y = 530 + Camera.mainCamera.transform.position.y
            print(self.transform.position.y)

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.state == 'bubble':
            self.state = 'death'
            self.size = 56
            self.frame_set = 4
            self.in_bubble = 25
            self.is_up = False
            self.transform.position.y -= self.gravity * 5

        elif group == 'attack:monster':
            if self.state == 'init' and other.state == 1:
                self.gravity = game_framework.frame_time * 60
                self.state = 'bubble'
                self.dir = 0
                self.is_up = True
                self.in_bubble = 14
                self.frame_set = 3.0

    def map_handle_collision(self, other, group):
        if group == 'monster:tile':
            if self.state == 'init':
                self.transform.position.y += self.gravity

            elif self.state == 'death':
                self.start_timer()
                self.gravity = 0
                self.frame_set = 1.0
                self.in_bubble = 25
