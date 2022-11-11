from Scripts.FrameWork.Transform import *

class Object:

    def __init__(self):
        self.image = None
        self.image_Type = None # frame
        self.flip = ' '

        self.transform = Transform()
        pass

    def __del__(self):
        pass

    def Draw(self):
        pos = self.transform.position
        scale = self.transform.scale
        self.image.clip_composite_draw(self.image_Type[0], self.image_Type[1], self.image_Type[2], self.image_Type[3], 0, self.flip, pos.x, pos.y,
                             scale.x * self.image_Type[2], scale.y * self.image_Type[3])

        pass

    def update(self):
        pass
    pass