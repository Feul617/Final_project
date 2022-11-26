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
        if event == UP and self.jump_on == False:
            self.jump_on = True
            self.transform.position.y += 5

    @staticmethod
    def exit(self, event):
        if event == SPACE:
            self.attack()

    @staticmethod
    def do(self):
        if self.jump_on:
            self.jump_count += 1
            if self.jump_count < self.jump_high:
                self.transform.position.y += 4 * JUMP_SPEED_PPS * game_framework.frame_time
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.flip = ' '
        else:
            self.flip = 'h'
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
            self.jump_on = True
            self.now_y = self.transform.position.y
            self.transform.position.y += game_framework.frame_time * 2
            self.velocity = 'up'

    def exit(self, event):
        self.face_dir = self.dir
        if event == SPACE:
            self.attack()

    def do(self):
        self.face_dir = self.dir
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 7.0
        self.transform.position.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time

        self.transform.position.x = clamp(80, self.transform.position.x, 720)

        if self.face_dir == 1:
            self.flip = 'h'
        else:
            self.flip = ' '

        if self.transform.position.y - self.now_y <= 100 and self.velocity == 'up':
            self.transform.position.y += 4 * JUMP_SPEED_PPS * game_framework.frame_time
            if self.transform.position.y - self.now_y > 100 and self.velocity == 'up':
                self.velocity = 'down'
        pass

    def draw(self):
        pass


class HURRY_UP:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAME_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

    def draw(self):
        pass

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

    def __init__(self):
        super(Character, self).__init__()
        self.transform.position.x, self.transform.position.y = 100, 300
        self.gravity = 0
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.jump_on = False
        self.jump_count = 0
        self.jump_high = 68 # 수정필요
        self.velocity = 'stand'
        self.image = load_image('./character/character3.png')
        self.image_Type = [self.frame * 60, 410, 60, 40]

        self.now_x, self.now_y = 0, 0
        self.char_camera = Camera.mainCamera.transform.position.y

        self.event_que = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

        self.monster = None
        self.charac = None

        #충돌체크
        Object.gameWorld.add_collision_group(self, None, 'character:tile')
        Object.gameWorld.add_collision_group(self, None, 'character:monster')

    def update(self):
        if self.char_camera != Camera.mainCamera.transform.position.y:
            self.gravity = 0
            self.transform.position.y -= game_framework.frame_time

        self.transform.position.y -= self.gravity
        if self.transform.position.y <= -10 - Camera.mainCamera.transform.position.y:
            self.transform.position.y = 570 - Camera.mainCamera.transform.position.y

        self.gravity = FALLING_SPEED * game_framework.frame_time

        self.cur_state.do(self)

        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}    Event {event_name[event]}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())

    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_events(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

    def get_bb(self):
        return self.transform.position.x - 30, self.transform.position.y - 20, \
               self.transform.position.x + 30, self.transform.position.y + 20

    def tile_get_bb(self):
        return self.transform.position.x - 30, self.transform.position.y - 20, \
               self.transform.position.x + 30, self.transform.position.y - 19

    def map_handle_collision(self, other, group):
        if group == 'character:tile':
            self.transform.position.y += self.gravity
            self.jump_on = False
            self.jump_count = 0

    def handle_collision(self, other, group):
        if group == 'character:monster':
            #remove_object(self)
            pass

    def attack(self):
        bubble = Bubble(self.transform.position.x, self.transform.position.y, self.face_dir * 2)
        Object.gameWorld.add_object(bubble, 2)
        Object.gameWorld.add_collision_group(bubble, self.monster, 'attack:monster')
        Object.gameWorld.add_collision_group(bubble, self.charac, 'attack:character')
        return bubble
