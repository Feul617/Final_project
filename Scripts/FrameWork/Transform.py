from Scripts.FrameWork.Vector2 import Vector2

class Transform:

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

    def Look_At_Target(self, position, speed):
        dir = Vector2.Normalize(position - self.position)
        self.position += dir * speed
        return dir
    pass