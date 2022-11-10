from Scripts.FrameWork.FrameWork_AFX import *

class Bubble(Object):
    image = None

    def __init__(self, x = 400, y = 300, velocity = 1):
        if Bubble.image == None:
            Bubble.image = load_image('ball21x21.png')
        self.x, self.y, self.velocity = x, y, velocity

    def draw(self):
        self.image.draw(self.x, self.y)

    def update(self):
        self.x += self.velocity

        if self.x < 25 or self.x > 1600 - 25:
            game_world.remove_object(self)
