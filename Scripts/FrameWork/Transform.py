from Scripts.FrameWork.Vector2 import *

class Trasform:

    def __init__(self):
        self.position = Vector2()
        self.scale = Vector2(1,1)
        pass

    def __del__(self):
        pass

    def Info(self):
        print(self.position)
        print(self.scale)
        pass
    pass