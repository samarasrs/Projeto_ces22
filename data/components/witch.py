import pygame as pg
from pygame.math import Vector2
from .. import setup, tools
from .. import constants as c
vec = pg.math.Vector2

class Witch(pg.sprite.Sprite):
    def __init__(self, is_witch):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['witch']
        self.sprite_sheet_death = setup.GFX['deathwitch']
        self.sprite_sheet_morcego = setup.GFX['morcego']

        self.state = c.STAND
        self.state_ant = c.STAND
        self.walking_timer = 0
        self.jumping_timer = 0
        self.current_frame = 0
        self.die_timer = 0
        self.is_witch = is_witch
        self.allow_jump = True
        self.dead = False
        self.setup_force()
        self.load_images()



        self.image = self.standing_frames[0]
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

#SETUP

    def setup_force(self):
        self.vel = vec(-2, 0)
        self.max_x_vel = c.MAX_WALK_SPEED
        self.max_y_vel = c.MAX_Y_VEL
        self.x_accel = c.WALK_ACCEL

        self.gravity = c.GRAVITY

# IMAGEM

    def get_image(self, x, y, width, height):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        rect = image.get_rect()
        if self.is_witch:
            image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        else:
            #print("morcego")
            image.blit(self.sprite_sheet_morcego, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER),
                                    int(rect.height * c.SIZE_MULTIPLIER)))
        return image
    def get_image_death(self, x, y, width, height):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.sprite_sheet_death, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER),
                                    int(rect.height * c.SIZE_MULTIPLIER)))
        return image
    def load_images(self):

        if self.is_witch:
            self.standing_frames = [self.get_image(5, 7, 21, 25)]
            for frame in self.standing_frames:
                frame.set_colorkey(c.BLACK)
            self.walking_normal_frames_r = [self.get_image(5, 39, 21, 25),
                                   self.get_image(37, 38, 20, 23),
                                   #self.get_image(68, 41, 20, 20),
                                   #self.get_image(69, 36, 20, 23),
                                   self.get_image(101, 40, 20, 23),
                                   self.get_image(164, 38, 22, 24)]

            self.walking_normal_frames_l = []
            for frame in self.walking_normal_frames_r:
                frame.set_colorkey(c.BLACK)
                self.walking_normal_frames_l.append(pg.transform.flip(frame, True, False))
        else:
            self.standing_frames = [self.get_image(1, 2, 13, 8)]
            for frame in self.standing_frames:
                frame.set_colorkey(c.BLACK)
            self.walking_normal_frames_r = [self.get_image(18, 2, 12, 9),
                                            self.get_image(35, 3, 10, 10)]

            self.walking_normal_frames_l = []
            for frame in self.walking_normal_frames_r:
                frame.set_colorkey(c.BLACK)
                self.walking_normal_frames_l.append(pg.transform.flip(frame, True, False))




        self.dying_frames_r = [self.get_image_death(9, 15, 11, 9),
                               self.get_image_death(40, 14, 13, 11),
                               self.get_image_death(71, 11, 19, 17),
                               self.get_image_death(100, 8, 24, 23)]

        for frame in self.dying_frames_r:
            frame.set_colorkey(c.BLACK)


# ESTADOS

    def star_death(self):
        self.dead = True
        self.die()

    def die(self):
        self.image = self.dying_frames_r[0]

        if (self.current_time - self.walking_timer >
                50):
            self.current_frame = (self.current_frame + 1) % len(self.dying_frames_r)
            self.image = self.dying_frames_r[self.current_frame]
            self.walking_timer = self.current_time

        self.die_timer += 1
        self.vel.x = 0
        if self.die_timer == 5:
            self.kill()

    def calculate_animation_speed(self):
        if self.vel.x == 0:
            animation_speed = 90
        elif self.vel.x > 0:
            animation_speed = 90 - (self.vel.x * (9))
        else:
            animation_speed = 90 - (self.vel.x * (9) * -1)
        return animation_speed

    def walking(self):
        if self.dead == False:
            if self.vel.x >= 0:
                if (self.current_time - self.walking_timer >
                        250):
                    self.current_frame = (self.current_frame + 1) % len(self.walking_normal_frames_r)
                    self.image = self.walking_normal_frames_r[self.current_frame]
                    self.walking_timer = self.current_time
            if self.vel.x < 0:
                if (self.current_time - self.walking_timer >
                        250):
                    self.current_frame = (self.current_frame + 1) % len(self.walking_normal_frames_l)
                    self.image = self.walking_normal_frames_l[self.current_frame]
                    self.walking_timer = self.current_time


        """if keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.current_frame = 0
                self.state_ant = c.WALK
                if self.vel.x > 4.5 or self.vel.x < -4.5:
                    self.vel.y = c.JUMP_VEL - .5
                else:
                    self.vel.y = c.JUMP_VEL"""


        """if keys[tools.keybinding['left']]:
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
            if self.vel.x > 0:
                self.image = self.walking_normal_frames_r[self.current_frame]
                self.vel.x -= self.x_accel

            else:
                self.vel.x = 0
                self.state = c.STAND
                self.state_ant = c.WALK

            if self.vel.x < 0:
                self.image = self.walking_normal_frames_l[self.current_frame]
                self.vel.x += self.x_accel


            else:
                self.vel.x = 0
                self.state = c.STAND
                self.state_ant = c.WALK  """

    """def standing(self, keys):
        #self.check_to_allow_jump(keys)
        self.image = self.standing_frames[0]
        self.vel = vec(0, 0)

        if keys[tools.keybinding['left']] or keys[tools.keybinding['right']]:
            self.state = c.WALK
            self.state_ant = c.STAND
        elif keys[tools.keybinding['jump']]:
            if self.allow_jump:
                self.state = c.JUMP
                self.current_frame = 0
                self.state_ant = c.STAND
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
                self.vel.x += self.x_accel """

    """def die(self):
        if self.vel.x >= 0:
            self.image = self.dying_frames_r[0]
        else:
            self.image = self.dying_frames_l[0]
        self.vel.x = 0"""


    """def star_death(self, game_info):
        self.dead = True
        game_info[c.CALLUM_DEAD] = True
        self.die()"""


# UPDATE

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        #self.handle_states(keys)
        self.walking()

