import game_framework
from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Monster.Monster import Monster
from Scripts.Object.Character import Character
from Scripts.FrameWork.Camera import Camera


class Mighta(Monster):
    def __init__(self):
        super(Mighta, self).__init__()
        self.name = 'mighta'
        self.frame_set = 4
        self.image_Type[1] = 700
        self.type = 710
        self.gravity = 0
        self.size = 54

        self.target = None
        self.speed = 20

        Object.gameWorld.add_object(self, 3)
        Object.gameWorld.add_collision_group(self, None, 'monster:tile')
        Object.gameWorld.add_collision_group(None, self, 'attack:monster')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        super(Mighta, self).update()
        self.transform.position.y -= self.gravity
        if self.state == 'init':
            self.dir = self.transform.Look_At_Target(Character.Instance.transform.position + Camera.mainCamera.transform.position, self.speed * game_framework.frame_time)

        if self.dir.x >= 0:
            self.flip = 'h'
        else:
            self.flip = ' '
        pass

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.state == 'bubble':
            self.state = 'death'
            self.image = load_image('./character/mighta_death.png')
            self.size = 63
            self.frame_set = 4
            self.type = 0
            self.in_bubble = 0
            self.is_up = False
            self.gravity = game_framework.frame_time * 60

        elif group == 'attack:monster':
            if self.state == 'init' and other.state == 1:
                self.state = 'bubble'
                self.gravity = game_framework.frame_time * 60
                self.type = 660
                self.is_up = True
                self.in_bubble = 7
                self.frame_set = 3.0

    def map_handle_collision(self, other, group):
        if group == 'monster:tile':
            if self.state == 'init':
                pass

            elif self.state == 'death':
                self.start_timer()
                self.gravity = 0
                self.frame_set = 1.0
                self.in_bubble = 27
