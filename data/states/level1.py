import pygame as pg
from .. import setup, tools
from .. import constants as c

class Level1(tools._State):
    def __init__(self):
        tools._State.__init__(self)

    def startup(self, current_time, persist):
        self.game_info = persist
        self.setup_background()

    def setup_background(self):
        self.background = setup.GFX['Map_jogo_teste']
        self.back_rect = self.background.get_rect()
        largura = self.back_rect.width
        altura = self.back_rect.height
        self.level = pg.Surface((largura, altura)).convert()
        self.level_rect = self.level.get_rect()
        self.camera = setup.TELA.get_rect(bottom=self.level_rect.bottom)
        self.camera.x = self.game_info[c.CAMERA_INICIAL_X]

