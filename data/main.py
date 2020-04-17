from . import setup, tools
from .states import main_menu, level1, game_over
from . import constants as c


def main():
    rodar_jogo = tools.Control(setup.TITULO,c.MAIN_MENU)
    dicionario_estados = {
        c.MAIN_MENU: main_menu.Menu(),
        c.LEVEL1: level1.Level1(),
        c.GAME_OVER: game_over.Game_Over()
        }
    rodar_jogo.setup_states(dicionario_estados, c.MAIN_MENU)
    rodar_jogo.main()

