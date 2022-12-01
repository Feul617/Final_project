from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Monster.Monster import *


class Mighta(Monster):
    def __init__(self):
        super(Mighta, self).__init__()
        self.name = 'mighta'
        self.frame_set = 4
        self.image_Type[1] = 700
        self.type = 700

        Object.gameWorld.add_object(self, 2)
        Object.gameWorld.add_collision_group(self, None, 'monster:tile')
        Object.gameWorld.add_collision_group(None, self, 'attack:monster')
        Object.gameWorld.add_collision_group(None, self, 'character:monster')

    def update(self):
        super(Mighta, self).update()

        pass
        # self.face_dir = self.dir
        # if self.face_dir == -1:
        #     self.flip = ' '
        # else:
        #     self.flip = 'h'
        #
        # self.gravity = game_framework.frame_time * 60
        #
        # self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set
        # self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        #
        # self.image_Type[0] = (int(self.frame) + self.in_bubble) * 54
        # self.Move()
        # self.floating()

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.state == 'bubble':
            self.state = 'death'
            self.in_bubble = 12
            self.is_up = False
            self.transform.position.y -= self.gravity * 3

    def map_handle_collision(self, other, group):
        if group == 'monster:tile':
            if self.state == 'init':
                pass

            elif self.state == 'death':
                self.start_timer()
                self.gravity = 0
                self.frame_set = 1.0
                self.in_bubble = 12
