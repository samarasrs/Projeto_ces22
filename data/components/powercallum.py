import pygame as pg
from .. import setup, tools
from .. import constants as c

class Power1(pg.sprite.Sprite):
    def __init__(self,looking):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['lightning']
        self.looking = looking
        #if looking == c.RIGHT:
        #    self.direction = c.RIGHT
            #self.x_vel = 12
        #else:
        #    self.direction = c.LEFT
            #self.x_vel = -12
        #self.y_vel = 10
        #self.gravity = .9
        self.frame_index = 0
        self.animation_timer = 0
        self.state = c.FLYING
        self.setup_frames()
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        #self.rect.right = x
        #self.rect.y = y
        self.name = c.POWER1
        
        
        
    def setup_frames(self):
        #criar os frames da direita
        self.frames_r = []

        #self.frames_r.append(
        #    self.get_image(36, 6, 31,23))   #Frame 1 of flying
        self.frames_r.append(
            self.get_image(127, 6, 39, 49))  #Frame 2 of Flying
        #self.frames_r.append(
        #    self.get_image(210, 6, 59, 79))   #Frame 3 of Flying
        self.frames_r.append(
            self.get_image(311, 6, 63, 109))  #Frame 4 of flying
        #self.frames_r.append(
        #    self.get_image(410, 6, 64, 140))   #frame 5 
        self.frames_r.append(
            self.get_image(509, 6, 64, 164))  #frame 6 


        #criar os frames da esquerda
        self.frames_l = []

        self.frames_l = []
        for frame in self.frames_r:
            frame.set_colorkey(c.BLACK)
            #frame = pg.transform.flip(frame,False,True)
            self.frames_l.append(pg.transform.flip(frame, True, False))   

        #if self.looking == c.RIGHT:
        self.frames = self.frames_r
        #else:
        #    self.frames = self.frames_l  

    def get_image(self, x, y, width, height):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER_POWER), #verificar se necessita mudar o SIZE_MULTIPLIER (esta o mesmo do callum)
                                    int(rect.height * c.SIZE_MULTIPLIER_POWER)))
        image = pg.transform.rotate(image, 90)
        return image  

    def update(self,game_info):
        self.current_time = game_info[c.CURRENT_TIME]
        self.handle_state()
        #self.check_if_off_screen(viewport)

    def handle_state(self):
        """Manipula o comportamento com base no estado"""
        if self.state == c.FLYING:
            self.animation()
        #elif self.state == c.BOUNCING:
        #    self.animation()
        elif self.state == c.EXPLODING:
            self.animation()

    def animation(self):
        
        # mudando o lado do poder de acordo pra onde heroi olha
        if self.looking == c.LEFT:
            self.frames = self.frames_l

        if self.state == c.FLYING:        
            if (self.current_time - self.animation_timer) > 200:
                if self.frame_index < 2:
                    self.frame_index += 1
                else:
                    self.frame_index = 0
                    self.kill()
                self.animation_timer = self.current_time
                self.image = self.frames[self.frame_index]
                self.rect = self.image.get_rect()


        elif self.state == c.EXPLODING:
            if (self.current_time - self.animation_timer) > 50:
                if self.frame_index < 2:
                    self.frame_index += 1
                    self.image = self.frames[self.frame_index]
                    self.animation_timer = self.current_time
                else:
                    self.kill()

    def explode_transition(self):
        
        self.frame_index = 4
        centerx = self.rect.centerx
        self.image = self.frames[self.frame_index]
        self.rect.centerx = centerx
        self.state = c.EXPLODING

    #nao usarei essa funcao a principio(apenas pro power 2)
    def check_if_off_screen(self, viewport):
        """Remove o grupo de sprite se fora da tela"""
        if (self.rect.x > viewport.right) or (self.rect.y > viewport.bottom) \
            or (self.rect.right < viewport.x):
            self.kill()