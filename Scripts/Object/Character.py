from Scripts.FrameWork.FrameWork_AFX import *

class Character(Object):
    def __init__(self):
        super(Character, self).__init__()
        self.transform.position = Vector2(400, 300)
        self.dir_x = 0
        self.gravity = 1
        self.state = 0
        self.image = load_image('./character/character3.png')

        self.image_Type = [0, 400, 40, 60]

        self.life = 0


        self.now_x = 0
        self.now_y = 0

    def handle_events(self, events):
        for event in events:
            if event.type == SDL_KEYDOWN:
                match event.key:
                    case pico2d.SDLK_RIGHT:
                        print('오른쪽')
                        self.dir_x += 1
                    case pico2d.SDLK_LEFT:
                        print('오른쪽 땜')
                        self.dir_x -= 1

            elif event.type == SDL_KEYUP:
                match event.key:
                    case pico2d.SDLK_RIGHT:
                        self.dir_x += 1
                    case pico2d.SDLK_LEFT:
                        self.dir_x -= 1

    def update(self):
        self.transform.position.x += self.dir_x
        self.transform.position.y -= self.gravity
        if self.transform.position.y < 0:
            self.transform.position.y = 680


    def collide(self):
        return self.transform.position.x + 20


class Attack():
    #attack = pico2d.load_image('./character/attack.png')
    def __init__(self):
        self.attack_x, self.attack_y = 0, 0
        self.attack_frame = 0
        self.count = []
        self.time = 0

    def draw(self):
        self.attack.clip_draw(self.attack_frame * 50, 100, 30, 30, self.attack_x, self.attack_y)

# class Character:
#     def __init__(self):
#         self.x, self.y = 100, 60
#         self.dir_x, self.dir_y = 0, 0
#         self.gravity = 0
#         self.frame = 0
#         self.life = 3
#         self.flip = ' '
#         self.image = pico2d.load_image('./character/character3.png')
#
#         self.now_x = 0
#         self.now_y = 0
#
#         self.move_on = False
#
#     def draw(self):
#         if character.dir_x == -1:
#             self.image.clip_composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)
#         else:
#             self.image.clip_composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)
#
#     def get_bb(self):
#         return self.x - 20, self.y, self.x + 20, self.y + 60



