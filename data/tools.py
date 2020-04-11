import pygame as pg
import os

#definindo as teclas a serem utilizadas no jogo
keybinding={
    'action':pg.K_s,
    'jump':pg.K_UP,
    'left':pg.K_BACKSPACE,
    'right':pg.K_RIGHT,
    'down':pg.K_DOWN
}

#deve conter a classe de controle e a classe de estados


class _State(object):
    #atributos de instância
    def __init__(self):
        #tempo atual
        self.current_time = 0.0
        #tempo de inicio
        self.start_time = 0.0
        #variavel para guardar se botao de sair (x) foi pressionado
        self.quit = False
        #variavel p guardar se a tela esta aberta
        self.done = False
        #proximo estado
        self.next=None
        #dados necessarios para o estado atual (qnt de vidas, qnt de poder etc)
        self.persist ={}

    def get_event(self, event):
        pass

    def startup(self, current_time, persist):
        #transferindo os dados persist do estado para a variavel
        self.persist = persist
        #o tempo inicial do estado é o tempo atual no momento do inicio
        self.start_time= current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass


class Control(object):
    def __init__(self, caption):
        #obter uma referencia para uma superficie de exibição
        self.screen = pg.display.get_surface()
        #variavel p guardar se a tela esta aberta
        self.done = False
        #criando uma variavel para auxiliar na marcação do tempo
        self.clock=pg.time.Clock()
        #definindo a quantidade de frames por segundos
        self.fps= 60
        #variavel para armazenar o estado de todas as teclas do teclado (as teclas do definidas para controle do jogo)
        self.keys = pg.key.get_pressed()
        #dicionario de estados (estamos criando um dicionario para facilitar a edição)
        #as chaves e as variaveis do dicionario estao no arquivo constant
        self.state_dict={}
        #variavel para armazenar a chave do estado
        self.state_name = None
        #variavel para armazenar o dado do estado
        self.state = None

    def setup_state (self, start_state, state_dict):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict([self.state_name])

    def update(self):
        #pega o tempo em milisegundos
        self.current_time = pg.time.get_ticks()
        #verificando se botao de sair foi pressionado
        if self.state.quit: