from . import setup, tools
from .states import main_menu, level1, game_over, vc_venceu, esqueceu
from . import constants as c


def main():
    # rodar_jogo vira um objeto da classe Control. É ele que vai controlar os estados do jogo
    rodar_jogo = tools.Control(setup.TITULO,c.MAIN_MENU)
    # criando o dicionario de estados.ele ditará em qual momento do jogo o jogo estará
    dicionario_estados = {
        c.MAIN_MENU: main_menu.Menu(),
        c.LEVEL1: level1.Level1(),
        c.GAME_OVER: game_over.Game_Over(),
        c.VITORIA: vc_venceu.Vencer(),
        c.ESQUECEU: esqueceu.Esqueceu()
        }
    # atribui o MAIN_MENU como início do jogo
    rodar_jogo.setup_states(dicionario_estados, c.MAIN_MENU)
    # inicia o jogo
    rodar_jogo.main()

