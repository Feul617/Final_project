from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Monster.Monster import *


class Boss(Monster):
    def __init__(self):
        super(Boss, self).__init__()
        self.image = load_image('./character/Boss.png')
        self.name = 'Boss'
        self.frame_set = 4
        self.frame_height = 2
        self.image_Type = [0, 0, 200, 200]
        self.in_bubble = 0
        self.gravity = game_framework.frame_time * 30

        self.life = 100
        self.attack_delay = 200

        Object.gameWorld.add_object(self, 2)
        Object.gameWorld.add_collision_group(None, self, 'attack:boss')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        self.Boss_Move()
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.image_Type[0] = (int(self.frame) + self.in_bubble) * 70
        self.image_Type[1] = self.frame_height * 70

        self.floating()
        pass

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.state == 'bubble':
            self.state = 'death'
            self.is_up = False
            self.transform.position.y -= self.gravity * 3

        elif group == 'attack:boss':
            if self.life > 0:
                self.life -= 1

            elif self.life <= 0:
                self.state = 'bubble'
                self.frame_height = 1
                self.frame_set = 2
                self.in_bubble = 4


    def map_handle_collision(self, other, group):
        pass

    def Boss_Move(self):
        if self.state == 'init':
            self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
            self.transform.position.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time
            if self.transform.position.x <= 80 or self.transform.position.x >= 720:
                self.dir *= -1
            if self.transform.position.y <= 30 or self.transform.position.y >= 550:
                self.dir_y *= -1




