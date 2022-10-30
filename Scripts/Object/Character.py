from Scripts.FrameWork.Object import *

class Character(Object):
    def __init__(self):
        super(Character, self).__init__()
        self.dir_x = 0
        self.gravity = 0
        self.life = 0
        self.image = load_image('./character/character3.png')

        self.now_x = 0
        self.now_y = 0

    def handle_events(self, event):
        for event in events:
            if event.type == SDL_KEYDOWN:
                match event.key:
                    case SDLK_RIGHT:
                        self.dir_x += 1
                    case SDLK_LEFT:
                        self.dir_x -= 1

            elif event.type == SDL_KEYUP:
                match event.key:
                    case SDLK_RIGHT:
                        self.dir_x -= 1
                    case SDLK_LEFT:
                        self.dir_x += 1




    def collide(self):
        return self.transform.position.x + 20




class Character:
    def __init__(self):
        self.x, self.y = 100, 60
        self.dir_x, self.dir_y = 0, 0
        self.gravity = 0
        self.frame = 0
        self.life = 3
        self.flip = ' '
        self.image = pico2d.load_image('./character/character3.png')

        self.now_x = 0
        self.now_y = 0

        self.move_on = False

    def draw(self):
        if character.dir_x == -1:
            self.image.clip_composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)
        else:
            self.image.clip_composite_draw(self.frame * 60, 410, 60, 40, 0, self.flip, self.x, self.y, 60, 40)

    def get_bb(self):
        return self.x - 20, self.y, self.x + 20, self.y + 60



