from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Monster.Monster import *
from Scripts.Object.Monster.Boss_attack import Boss_attack
from Scripts.Object.Character import Character
import math
import end_state


class Boss(Monster):
    def __init__(self):
        super(Boss, self).__init__()
        self.transform.position = Vector2(400, 300)
        self.image = load_image('./character/Boss.png')
        self.name = 'Boss'
        self.size = 72
        self.frame_set = 4
        self.frame_height = 1
        self.image_Type = [0, 0, 72, 72]
        self.in_bubble = 0
        self.transform.scale *= 2.5

        self.life = 10
        self.attack_delay = 200
        self.delay_regulate = 1
        self.speed = 1

        self.ending_timer = 500


        Object.gameWorld.add_object(self, 3)
        Object.gameWorld.add_collision_group(None, self, 'attack:boss')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        self.Boss_Move()
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        self.image_Type[0] = (int(self.frame) + self.in_bubble) * self.size
        self.image_Type[1] = self.frame_height * 72

        self.floating()
        if self.state != 'death':
            self.Boss_attack()

        if self.state == 'death':
            if self.transform.position.y > 80:
                self.transform.position.y -= self.gravity * 2

            elif self.transform.position.y <= 85:
                self.frame_set = 1
                self.in_bubble = 3
                self.ending_timer -= 1
                if self.ending_timer <= 0:
                    game_framework.change_state(end_state)
        pass

    def get_bb(self):
        return self.transform.position.x - 72, self.transform.position.y - 72 - Camera.mainCamera.transform.position.y, \
               self.transform.position.x + 72, self.transform.position.y + 72 - Camera.mainCamera.transform.position.y

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.state == 'bubble':
            self.state = 'death'
            self.frame_set = 4
            self.in_bubble = 0
            self.is_up = False
            self.gravity = game_framework.frame_time * 30

        elif group == 'attack:boss' and other.state == 1:
            if self.life > 0:
                self.life -= 1

            elif 0 < self.life <= 50:
                self.state = 'angry'
                self.frame_set = 2
                self.in_bubble = 4

            elif self.life <= 0:
                self.state = 'bubble'
                self.frame_height = 0
                self.frame_set = 2
                self.in_bubble = 4


    def map_handle_collision(self, other, group):
        pass

    def Boss_Move(self):
        if self.state == 'init':
            self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time * self.speed
            self.transform.position.y += self.dir_y * RUN_SPEED_PPS * game_framework.frame_time * self.speed

        if self.state == 'angry':
            self.speed = 1.3
            self.delay_regulate = 2


        if self.transform.position.x <= 100 or self.transform.position.x >= 700:
                self.dir *= -1
        if self.transform.position.y <= 60 or self.transform.position.y >= 500:
                self.dir_y *= -1

        self.face_dir = self.dir
        if self.face_dir == -1:
            self.flip = ' '
        else:
            self.flip = 'h'


    def Boss_attack(self):
        self.attack_delay -= 1
        pos = Character.Instance.transform.position

        if self.attack_delay == 0:
            attack = Boss_attack(self)
            self.attack_delay = 200 / self.delay_regulate




