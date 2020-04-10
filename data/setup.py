import pygame as pg
import os
from . import tools
from . import constants as c

#deixando o video centralizado
os.environ['SDL_VIDEO_CENTERED']='1'
#iniciando o pygame
pg.init()
#definindo os eventos permitidos de teclado (controles do jogo)
pg.event.set_allowed([pg.KEYDOWN, pg.KEYUP, pg.QUIT])
#colocando o titulo da tela
pg.display.set_caption(c.TITULO)
#iniciando uma tela
TELA = pg.display.set_mode(c.TELA_TAMANHO)
#recebe uma area retangular
TELA_RECT = TELA.get_rect()


#completar os caminhos para as pastas de imagens e sons
FONTS=''
MUSIC=''
GFFX=''
SFX=''
