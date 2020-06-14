import pygame as pg
from pygame.math import Vector2
from .. import setup, tools
from .. import constants as c
vec = pg.math.Vector2

class Egg(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.sprite_sheet = setup.GFX['egg']
        self.current_frame = 0
        self.load_images()
        self.image = self.get_image(68, 52, 120, 165)
        self.image.set_colorkey(c.BLACK)
        self.rect = self.image.get_rect()
        self.mask = pg.mask.from_surface(self.image)

# IMAGEM

    def get_image(self, x, y, width, height):
        # Pega imagem do arquivo filename
        image = pg.Surface((width, height))
        rect = image.get_rect()
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        
        image = pg.transform.scale(image,
                                   (int(rect.width *c.SIZE_EGG),
                                    int(rect.height * c.SIZE_EGG)))
        return image

    def load_images(self):
        self.standing_frames = [self.get_image(68, 52, 120, 165)]
        for frame in self.standing_frames:
            frame.set_colorkey(c.BLACK)

# ESTADOS

    def update(self, game_info):
        self.current_time = game_info[c.CURRENT_TIME]

