from . import setup, tools
from .states import main_menu
from . import constants as c


def main():
    rodar_jogo = tools.Control(setup.TITULO)
    dicionario_estados = {
        c.MAIN_MENU: main_menu.Menu()
        }
    rodar_jogo.setup_states(dicionario_estados, c.MAIN_MENU)
    rodar_jogo.main()

