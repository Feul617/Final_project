from Scripts.FrameWork.FrameWork_AFX import *

class Monster(Object):
    def __init__(self):
        super(Monster, self).__init__()
        self.dir_x, self.dir_y = 0, 0
        self.image = load_image('./character/monster2.png')

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60

def Monster_Type(index):
    monster = Monster()

    if index == 0:
        monster.image_type = [0, 500, 52, 52]
    elif index == 1:
        monster.image_type = [0, 450, 52, 52]

    return monster