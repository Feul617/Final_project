import pico2d

from Scripts.FrameWork.Transform import *
from Scripts.FrameWork.Camera import Camera

class Object:
    count = -1
    gameWorld = None
    def __init__(self):
        self.image = None
        self.image_Type = None # frame
        self.flip = ' '

        self.transform = Transform()
        self.ID = Object.count
        self.name = "None"
        self.isActive = True

        # collide 박스
        self.collisionBox = [0,0]
        self.tile_collisionBox = [0, 0, 0, 0]

        Object.count += 1
        pass

    def __del__(self):
        pass

    def Enable(self):
        pass

    def Disable(self):
        pass

    def SetActive(self, value):
        if self.isActive is True and value is False:
            self.Enable()
        elif self.isActive is False and value is True:
            self.Disable()
        self.isActive = value
        pass

    def Init(self):
        pass

    def Draw(self):
        pos = self.transform.position - Camera.mainCamera.transform.position
        scale = self.transform.scale
        self.image.clip_composite_draw(self.image_Type[0], self.image_Type[1], self.image_Type[2], self.image_Type[3], 0, self.flip,\
                                       pos.x, pos.y,
                             scale.x * self.image_Type[2], scale.y * self.image_Type[3])
        pass

    def update(self):
        pass

    def get_bb(self):
        return 0, 0, 0, 0

    def tile_get_bb(self):
        return 0, 0, 0, 0
    # def get_bb(self):
    #     pos =  [self.collisionBox[0] - Camera.mainCamera.transform.position.x, self.collisionBox[1] - Camera.mainCamera.transform.position.y]
    #     return self.transform.position.x - pos[0], self.transform.position.y - pos[1], \
    #            self.transform.position.x + pos[0], self.transform.position.y + pos[1]
    #
    # def tile_get_bb(self):
    #     tile_pos = [self.tile_collisionBox[0] - Camera.mainCamera.transform.position.x,\
    #            self.tile_collisionBox[1] - Camera.mainCamera.transform.position.y,\
    #                 self.tile_collisionBox[2] - Camera.mainCamera.transform.position.x,\
    #                 self.tile_collisionBox[3] - Camera.mainCamera.transform.position.y]
    #
    #     return self.transform.position.x - tile_pos[0], self.transform.position.y - tile_pos[1], \
    #            self.transform.position.x + tile_pos[2], self.transform.position.y - tile_pos[3]

    pass