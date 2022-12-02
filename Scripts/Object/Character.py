import game_framework
from Scripts.FrameWork.FrameWork_AFX import *
from Scripts.Object.Attack import *
from Scripts.FrameWork.game_world import GameWorld
from Scripts.FrameWork.Camera import Camera

#1 : 이벤트 정의
RD, LD, RU, LU, TIMER, UP, SPACE = range(7)
event_name = ['RD', 'LD', 'RU', 'LU', 'TIMER', 'UP', 'SPACE']

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT): LD,
    (SDL_KEYUP, SDLK_RIGHT): RU,
    (SDL_KEYUP, SDLK_LEFT): LU,
    (SDL_KEYDOWN, SDLK_UP): UP
}

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAME_PER_ACTION = 8

#2 : 상태의 정의
class IDLE:
    @staticmethod
    def enter(self,event):
        self.dir = 0
        if self.face_dir == 1:
            self.flip = 'h'
        else:
            self.flip = ' '
        if event == UP and self.velocity == 'stand':
            self.jump_sound.play(1)
            self.velocity = 'up'
            self.now_y = self.transform.position.y
            self.transform.position.y += self.gravity * 3


    @staticmethod
    def exit(self, event):
        if event == SPACE:
            self.attack()
            self.attack_sound.play(1)

    @staticmethod
    def do(self):
        if self.transform.position.y - self.now_y <= self.jump_high and self.velocity == 'up':
            self.transform.position.y += self.gravity * 3
            if self.transform.position.y - self.now_y > self.jump_high:
                self.velocity = 'down'
        pass

class RUN:
    def enter(self, event):
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        elif event == UP and self.velocity == 'stand':
            self.jump_sound.play(1)
            self.velocity = 'up'
            self.now_y = self.transform.position.y
            self.transform.position.y += self.gravity * 3

    def exit(self, event):
        self.face_dir = self.dir
        if event == SPACE:
            self.attack()
            self.attack_sound.play(1)


    def do(self):

        self.face_dir = self.dir
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7.0
        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.transform.position.x = clamp(80, self.transform.position.x, 720)

        if self.face_dir == 1:
            self.flip = 'h'
        else:
            self.flip = ' '

        if self.transform.position.y - self.now_y <= self.jump_high and self.velocity == 'up':
            self.transform.position.y += self.gravity * 3
            if self.transform.position.y - self.now_y > self.jump_high:
                self.velocity = 'down'
        pass


class HURRY_UP:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

#3. 상태 변환 구현

next_state = {
    IDLE:  {RU: RUN,  LU: RUN,  RD: RUN,  LD: RUN, SPACE: IDLE, UP: IDLE},
    RUN:   {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, SPACE: RUN, UP: RUN},
    HURRY_UP: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, SPACE: IDLE}
}

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 40.0 # km/h 마라토너의 평속
FALLING_SPEED = (RUN_SPEED_KMPH + 10) * 1000 / 60.0 / 60.0 * PIXEL_PER_METER
JUMP_SPEED_PPS = (RUN_SPEED_KMPH) * 1000 / 60.0 / 60.0 * PIXEL_PER_METER
RUN_SPEED_MPM = RUN_SPEED_KMPH * 1000 / 60.0
RUN_SPEED_MPS = RUN_SPEED_MPM / 60.0
RUN_SPEED_PPS = RUN_SPEED_MPS * PIXEL_PER_METER

class Character(Object):
    Instance = None
    def __init__(self):
        super(Character, self).__init__()
        self.transform.position = Vector2(100, 100)
        self.frame = 0
        self.frame_set = 7
        self.dir, self.face_dir = 0, 1
        self.velocity = 'stand'
        self.jump_high = 120 # 수정필요
        self.image = load_image('./character/character3.png')
        self.image_Type = [self.frame * 60, 410, 60, 40]
        self.jump_sound = load_wav('./sound/jump_sound.mp3')
        self.jump_sound.set_volume(10)
        self.is_Next = False

        self.attack_sound = load_wav('./sound/attack_sound.mp3')
        self.attack_sound.set_volume(10)

        self.isHandle = True
        self.gravity = 0
        self.now_x, self.now_y = 0, 0
        self.is_collide_set = True
        self.char_camera = Camera.mainCamera.transform.position.y

        self.life = 3
        self.invincibility_time = 100
        self.start_timer = False

        self.event_que = []
        self.is_event_init = False
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.monster = None

        if Character.Instance is None:
            Character.Instance = self

        #collision Box 크기
        self.collisionBox = [30, 20]
        self.tile_collisionBox = [30, 23, 30, 15]

        #충돌체크
        Object.gameWorld.add_collision_group(self, None, 'character:tile')
        Object.gameWorld.add_collision_group(self, None, 'character:monster')
        Object.gameWorld.add_collision_group(None, self, 'attack:character')

    def update(self):
        self.gravity = FALLING_SPEED * game_framework.frame_time
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % self.frame_set

        #if self.char_camera is not Camera.mainCamera.transform.position.y:
        if self.is_Next:
            # if self.isHandle:
            #     self.event_que.clear()
            self.dir = 0
            self.isHandle = False
            self.gravity = 0
            self.frame_set = 1.0
            self.image_Type = [300, 0 ,80 ,80]
            self.is_collide_set = False
            if self.transform.position.x != 80:
                if self.transform.position.x >= 80:
                    self.transform.position.x -= (self.transform.position.x - 80) / 100
                elif self.transform.position.x < 80:
                    self.transform.position.x += game_framework.frame_time * 10

            if self.transform.position.y >= 50:
                self.transform.position.y -= (self.transform.position.y - 50) / 100
        else:
            self.frame_set = 7
            self.image_Type = [int(self.frame) * 60, 410, 60, 40]
            self.is_collide_set = True
            self.isHandle = True

            #self.transform.position.y -= game_framework.frame_time * 3


        self.transform.position.y -= self.gravity

        if self.transform.position.y <= -10:
            self.gravity = 0
            self.transform.position.y = 570

        self.invincibility_timer()

        self.cur_state.do(self)

        if self.life == 0:
            pass

        if self.event_que and self.is_Next == False:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        pos = Vector2(30, 20)
        # print(self.transform.position.x - pos.x, self.transform.position.y - pos.y)
        return self.transform.position.x - pos.x, self.transform.position.y - pos.y, \
               self.transform.position.x + pos.x, self.transform.position.y + pos.y

    def tile_get_bb(self):
        pos1 = Vector2(30, 23)
        pos2 = Vector2(30, 15)
        return self.transform.position.x - pos1.x, self.transform.position.y - pos1.y, \
               self.transform.position.x + pos2.x, self.transform.position.y - pos2.y

    def map_handle_collision(self, other, group):
        if group == 'character:tile' and self.is_collide_set:
            self.transform.position.y += self.gravity
            if self.velocity == 'down':
                self.velocity = 'stand'

    def handle_collision(self, other, group):
        if group == 'character:monster' and self.is_collide_set \
                and self.invincibility_time == 100 and other.state == 0:
            #self.image_Type = [(self.frame + 10) * 60, 200, 50, 50]
            self.life -= 1
            self.start_timer = True
            pass

    def attack(self):
        bubble = Bubble(self.transform.position.x, self.transform.position.y + Camera.mainCamera.transform.position.y, self.face_dir * 2)

        #return bubble

    def Draw(self):
        pos = self.transform.position
        scale = self.transform.scale
        self.image.clip_composite_draw(self.image_Type[0], self.image_Type[1], self.image_Type[2], self.image_Type[3], 0, self.flip,\
                                       pos.x, pos.y,
                             scale.x * self.image_Type[2], scale.y * self.image_Type[3])

    def invincibility_timer(self):
        if self.start_timer:
            self.invincibility_time -= 1
        if self.invincibility_time == 0:
            self.start_timer = False
            self.invincibility_time = 100
