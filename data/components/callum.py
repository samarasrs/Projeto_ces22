import pygame as pg
from .. import setup, tools
from .. import constants as c

class Spritesheet:
    # Carrega os sprites
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, width, height, player):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        if player:
            image = pg.transform.scale(image, (width * 3, height * 3))
        else:
            image = pg.transform.scale(image, (width, height // 3))

        return image


class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.game = game

        # setup states
        self.walking = False
        self.jumping = False
        self.crouching= False
        self.attacking = False
        self.dying = False

        self.life_number = 3
        self.bullet_number = 0

        self.with_eggs = False

        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        #self.image = self.standing_frames[0]
        self.image = self.game.spritesheet_player.get_image(68, 41, 20, 20, True)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.pos = vec(40, HEIGHT - 100)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def show_heart(self):
        self.heart_image = self.game.spritesheet_heart.get_image(0, 0, 16, 16, True)
        self.heart_image.set_colorkey(BLACK)
        self.heart_rect = self.heart_image.get_rect()
        self.heart_rect.x = 0
        self.heart_rect.y = 0
        self.game.screen.blit(self.heart_image, self.heart_rect)
        if self.life_number > 1:
            self.heart_image2 = self.game.spritesheet_heart.get_image(0, 0, 16, 16, True)
            self.heart_image2.set_colorkey(BLACK)
            self.heart_rect2 = self.heart_image2.get_rect()
            self.heart_rect2.x = 49
            self.heart_rect2.y = 0
            self.game.screen.blit(self.heart_image2, self.heart_rect2)
        if self.life_number > 2:
            self.heart_image3 = self.game.spritesheet_heart.get_image(0, 0, 16, 16, True)
            self.heart_image3.set_colorkey(BLACK)
            self.heart_rect3 = self.heart_image3.get_rect()
            self.heart_rect3.x = 98
            self.heart_rect3.y = 0
            self.game.screen.blit(self.heart_image3, self.heart_rect3)



    def load_images(self):

        self.life_heart_frame = self.game.spritesheet_heart.get_image(0, 0, 16, 16, True)
        self.standing_frames = [self.game.spritesheet_player.get_image(68, 10, 20, 21, True)]
        for frame in self.standing_frames:
            frame.set_colorkey(WHITE)
        self.walking_normal_frames_r = [self.game.spritesheet_player.get_image(5, 42, 20, 20, True),
                               self.game.spritesheet_player.get_image(35, 40, 20, 20, True),
                               self.game.spritesheet_player.get_image(68, 41, 20, 20, True),
                               self.game.spritesheet_player.get_image(100, 43, 20, 20, True),
                               self.game.spritesheet_player.get_image(132, 42, 20, 20, True),
                               self.game.spritesheet_player.get_image(164, 40, 20, 20, True)]
        self.walking_normal_frames_l = []
        for frame in self.walking_normal_frames_r:
            frame.set_colorkey(WHITE)
            self.walking_normal_frames_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame = self.game.spritesheet_player.get_image(293, 11, 18, 20, True)
        self.jump_frame.set_colorkey(WHITE)

        self.dying_frames = [
                               self.game.spritesheet_player.get_image(36, 202, 20, 21, True),
                               self.game.spritesheet_player.get_image(65, 201, 25, 25, True),]

        for frame in self.dying_frames:
            frame.set_colorkey(WHITE)

        self.attacking_frames_r = [self.game.spritesheet_player.get_image(4, 203, 20, 20, True),
                                   self.game.spritesheet_player.get_image(33, 203, 25, 20, True),
                                   self.game.spritesheet_player.get_image(65, 200, 25, 25, True),
                                   self.game.spritesheet_player.get_image(100, 203, 20, 20, True)]
        for frame in self.attacking_frames_r:
            frame.set_colorkey(WHITE)

        self.attacking_frames_l = []
        for frame in self.attacking_frames_r:
            frame.set_colorkey(WHITE)
            self.attacking_frames_l.append(pg.transform.flip(frame, True, False))
        self.crouching_frames_r = [
                                self.game.spritesheet_player.get_image(134, 501, 21, 11, True),
                                self.game.spritesheet_player.get_image(165, 501, 21, 11, True),
                                self.game.spritesheet_player.get_image(197, 501, 21, 11, True)]
        for frame in self.crouching_frames_r:
            frame.set_colorkey(WHITE)

        self.crouching_frames_l = []
        for frame in self.crouching_frames_r:
            frame.set_colorkey(WHITE)
            self.crouching_frames_l.append(pg.transform.flip(frame, True, False))


    def jump_cut(self):
        if self.jumping:
            if self.vel.y < -3:
                self.vel.y = -3

    def jump(self):
        # jump only if standing on a platform
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2
        if hits and not self.jumping:
            self.jumping = True
            self.vel.y = -PLAYER_JUMP

    def Crouch(self):
        # Crouch only if standing on a platform
        self.rect.y += 2
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2

        hits = pg.sprite.spritecollide(self, self.game.platforms, False)

        if hits and not self.crouching:
            self.crouching = True
            self.vel.x = 0

    def crouch_cut(self):
        if self.crouching:
            self.crouching = False

    def update(self, surface, keys, current_time):
        self.animate(current_time)

        self.acc = vec(0, PLAYER_GRAV)
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC

        # apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        # equations of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5 * self.acc
        # wrap around the sides of the screen
        if self.pos.x > WIDTH + self.rect.width / 2:
            self.pos.x = 0 - self.rect.width / 2
        if self.pos.x < 0 - self.rect.width / 2:
            self.pos.x = WIDTH + self.rect.width / 2

        self.rect.midbottom = self.pos

    def animate(self, current_time):
        if not self.dying:
            if self.vel.x != 0:
                self.walking = True
            else:
                self.walking = False

            if self.walking and not self.crouching and not self.jumping:
                if current_time - self.last_update > 50:
                    self.last_update = current_time
                    self.current_frame = (self.current_frame + 1) % len(self.walking_normal_frames_r)
                    bottom = self.rect.bottom
                    if self.vel.x > 0:
                        self.image = self.walking_normal_frames_r[self.current_frame]
                    else:
                        self.image = self.walking_normal_frames_l[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

            if not self.jumping and not self.walking and not self.crouching:
                if (current_time - self.last_update) > 200:
                    self.last_update = current_time
                    self.current_frame = (self.current_frame + 1) % len(self.standing_frames)
                    bottom = self.rect.bottom
                    self.image = self.standing_frames[self.current_frame]
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

            if self.jumping:
                if current_time - self.last_update > 100:
                    self.last_update = current_time
                    bottom = self.rect.bottom
                    self.image = self.jump_frame
                    self.rect = self.image.get_rect()
                    self.rect.bottom = bottom

            if self.crouching:
                if self.vel.x < 0:
                    if (current_time - self.last_update) > 100:
                        self.last_update = current_time
                        self.current_frame = (self.current_frame + 1) % len(self.crouching_frames_r)
                        bottom = self.rect.bottom
                        self.image = self.crouching_frames_r[self.current_frame]
                        self.rect = self.image.get_rect()
                        self.rect.bottom = bottom
                else:
                    if (current_time - self.last_update) > 200:
                        self.last_update = current_time
                        self.current_frame = (self.current_frame + 1) % len(self.crouching_frames_l)
                        bottom = self.rect.bottom
                        self.image = self.crouching_frames_l[self.current_frame]
                        self.rect = self.image.get_rect()
                        self.rect.bottom = bottom
        else:
            if (current_time - self.last_update) > 200:
                self.last_update = current_time
                self.current_frame = (self.current_frame + 1) % len(self.dying_frames)
                bottom = self.rect.bottom
                self.image = self.dying_frames[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom