import pygame as pg
from . import setup
from . import constants as c

class Sound(object):
    
    def __init__(self, status):
        self.sfx_dict = setup.SFX
        self.music_dict = setup.MUSIC
        self.state = status
        self.set_music_mixer()
        

    def set_music_mixer(self):
        if self.state == c.MAIN_MENU:
            pg.mixer.music.load(self.music_dict['menu'])
            pg.mixer.music.play(-1)
            #self.state = c.NORMAL
        elif self.state == c.GAME_OVER:
            pg.mixer.music.load(self.music_dict['game_over'])
            pg.mixer.music.play()
            self.state = c.GAME_OVER
    
    def update(self):
        self.handle_state()

    def handle_state(self):
        pass

    def play_music(self):
        pass

    def stop_music(self):
        pg.mixer.music.stop()
