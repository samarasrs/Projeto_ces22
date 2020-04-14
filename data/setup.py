import pygame as pg
import os
from . import tools
from . import constants as c


TITULO = c.TITULO

# deixando o video centralizado
os.environ['SDL_VIDEO_CENTERED'] = '1'
# iniciando o pygame
pg.init()
# definindo os eventos permitidos de teclado (controles do jogo)
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
# colocando o titulo da tela
pg.display.set_caption(c.TITULO)
# iniciando uma tela
TELA = pg.display.set_mode(c.TELA_TAMANHO)
# recebe uma area retangular
TELA_RECT = TELA.get_rect()


# completar os caminhos para as pastas de imagens e sons
FONTS = tools.load_all_fonts(os.path.join("resources", "fonts"))
MUSIC = tools.load_all_music(os.path.join("resources", "music"))
GFX = tools.load_all_gfx(os.path.join("resources", "graphics"))
SFX = tools.load_all_sfx(os.path.join("resources", "sound"))
