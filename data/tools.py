import pygame as pg
import os

keybinding={
    'action':pg.K_s,
    'jump':pg.K_UP,
    'left':pg.K_BACKSPACE,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}

#deve conter a classe de controle e a classe de estados


class _State(object):
