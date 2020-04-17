import pygame as pg
from pygame.math import Vector2
from .. import setup, tools
from .. import constants as c
vec = pg.math.Vector2

class Callum(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['callum']
        self.state = c.STAND
        self.state_ant = None
        self.walking_timer = 0
        self.jumping_timer = 0
        self.current_frame = 0
        self.allow_jump = True
        self.setup_force()
        self.load_images()

        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)


    def get_image(self, x, y, width, height):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        # faz com que os pixels da cor do argumento da figura nao fiquem transparentes
        #image.set_colorkey((47, 47, 46))
        image.set_colorkey(c.WHITE)
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER),
                                    int(rect.height * c.SIZE_MULTIPLIER)))
        return image

    def setup_force(self):
        self.vel = vec(0, 0)
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL
        self.jump_vel = c.JUMP_VEL
        self.gravity = c.GRAVITY

    def load_images(self):
        self.standing_frames = [self.get_image(68, 10, 20, 21)]

        self.walking_normal_frames_r = [self.get_image(5, 42, 20, 20),
                               self.get_image(35, 40, 20, 20),
                               self.get_image(68, 41, 20, 20),
                               self.get_image(100, 43, 20, 20),
                               self.get_image(132, 42, 20, 20),
                               self.get_image(164, 40, 20, 20)]

        self.walking_normal_frames_l = []
        for frame in self.walking_normal_frames_r:
            self.walking_normal_frames_l.append(pg.transform.flip(frame, True, False))

        self.jump_frame_r = [self.get_image(68, 168, 19, 23),
                             self.get_image(101, 166, 19, 21),
                             self.get_image(132, 166, 19, 22),
                             self.get_image(163, 172, 21, 21)]
        self.jump_frame_l = []
        for frame in self.jump_frame_r:
            self.jump_frame_l.append(pg.transform.flip(frame, True, False))


        self.dying_frames_r = [self.get_image(241, 167, 23, 17)]
        self.dying_frames_l = [pg.transform.flip(self.get_image(241, 167, 23, 17), True, False)]

    def check_to_allow_jump(self, keys):
        if not keys[tools.keybinding['jump']]:
            self.allow_jump = True

    def jumping(self, keys):
        self.allow_jump = False
        self.gravity = c.JUMP_GRAVITY
        self.vel.y += self.gravity
        self.jumping_timer = self.current_time
        if (self.current_time - self.jumping_timer >
                    self.calculate_animation_speed()):
            self.current_frame = (self.current_frame + 1) % len(self.jump_frame_r[self.current_frame])
        if self.vel.x == 0:
            self.image = self.standing_frames[0]
        elif self.vel.x > 0:
            self.image = self.jump_frame_r[self.current_frame]
        else:
            self.image = self.jump_frame_l[self.current_frame]

        if 0 <= self.vel.y < self.max_y_vel:
            self.gravity = c.GRAVITY
            self.state = c.FALL

        if keys[tools.keybinding['left']]:
            if abs(self.vel.x) < self.max_x_vel:
                self.vel.x -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.vel.x < self.max_x_vel:
                self.vel.x += self.x_accel

        if not keys[tools.keybinding['jump']]:
            self.gravity = c.GRAVITY
            self.state = c.FALL

    def walking(self, keys):
        self.check_to_allow_jump(keys)
        if self.state_ant == c.STAND:
            self.state_ant = None
            self.walking_timer = self.current_time
            self.current_frame = 0
        else:
            if (self.current_time - self.walking_timer >
                    self.calculate_animation_speed()):
                self.current_frame = (self.current_frame + 1) % len(self.walking_normal_frames_r)

        if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                if self.vel.x > 4.5 or self.vel.x < -4.5:
                    self.vel.y = c.JUMP_VEL - .5
                else:
                    self.vel.y = c.JUMP_VEL

        if keys[tools.keybinding['left']]:
            self.image = self.walking_normal_frames_l[self.current_frame]
            if abs(self.vel.x) < self.max_x_vel:
                self.vel.x -= self.x_accel
                if self.vel.x > -0.5:
                    self.vel.x= -0.5
            elif abs(self.vel.x) > self.max_x_vel:
                self.vel.x += self.x_accel

        elif keys[tools.keybinding['right']]:
            self.image = self.walking_normal_frames_r[self.current_frame]
            if self.vel.x < self.max_x_vel:
                self.vel.x += self.x_accel
                if self.vel.x < 0.5:
                    self.vel.x= 0.5
            elif abs(self.vel.x) > self.max_x_vel:
                self.vel.x -= self.x_accel

        else:
            if self.x_vel > 0:
                self.image = self.walking_normal_frames_r[self.current_frame]
                self.x_vel -= self.x_accel
            else:
                self.x_vel = 0
                self.state = c.STAND

            if self.x_vel < 0:
                self.image = self.walking_normal_frames_l[self.current_frame]
                self.x_vel += self.x_accel
            else:
                self.x_vel = 0
                self.state = c.STAND

    def standing(self, keys):
        self.check_to_allow_jump(keys)
        self.image = self.standing_frames[0]
        self.vel = vec(0, 0)

        if keys[tools.keybinding['left']] or keys[tools.keybinding['right']]:
            self.state = c.WALK
            self.state_ant = c.STAND
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.vel.y = c.JUMP_VEL
        else:
            self.state = c.STAND

    def falling(self, keys):
        if self.vel.y < c.MAX_Y_VEL:
            self.vel.y += self.gravity

        if keys[tools.keybinding['left']]:
            if self.vel.x > (self.max_x_vel * - 1):
                self.vel.x -= self.x_accel

        elif keys[tools.keybinding['right']]:
            if self.vel.x < self.max_x_vel:
                self.vel.x += self.x_accel

    def calculate_animation_speed(self):
        if self.x_vel == 0:
            animation_speed = 130
        elif self.x_vel > 0:
            animation_speed = 130 - (self.x_vel * (13))
        else:
            animation_speed = 130 - (self.x_vel * (13) * -1)
        return animation_speed

    def dead(self):
        if self.vel.x >= 0:
            self.image = self.dying_frames_r[0]
        else:
            self.image = self.dying_frames_l[0]

    def handle_states(self,keys):
        if self.state == c.STAND:
            self.standing(keys)
        elif self.state == c.WALK:
            self.walking(keys)
        elif self.state == c.JUMP:
            self.jumping(keys)
        elif self.state == c.FALL:
            self.falling(keys)
        elif self.state == c.DEAD:
            self.dead()

    def update(self, keys, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_states(keys)

