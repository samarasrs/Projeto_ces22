from . import setup, tools
from . import constants as c

def main ():
    rodar_jogo=tools.Control(setup.TITULO)
    dicionario_estados ={
        c.MAIN_MENU: main_menu.Menu(),
        c.LOAD_SCREEN: load_screen.LoadScreen(),
        c.TIME_OUT: load_screen.TimeOut(),
        c.GAME_OVER: load_screen.GameOver(),
        c.LEVEL1: level1.Level1()
        }
    rodar.setup_states(dicionario_estados, c.MAIN_MENU)
    rodar_jogo.main()

