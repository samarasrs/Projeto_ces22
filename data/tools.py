import pygame as pg
import os
from . import game_sound as gs

# definindo as teclas a serem utilizadas no jogo
keybinding = {
    'action1': pg.K_s,
    'action2': pg.K_a,
    'jump': pg.K_UP,
    'left': pg.K_LEFT,
    'right': pg.K_RIGHT,
    'down': pg.K_DOWN
}

# deve conter a classe de controle e a classe de estados


class _State(object):
    # atributos de instância
    def __init__(self):
        # tempo atual
        self.current_time = 0.0
        # tempo de inicio
        self.start_time = 0.0
        # variavel para guardar se botao de sair (x) foi pressionado
        self.quit = False
        # variavel p guardar se a tela esta aberta
        self.done = False
        # proximo estado
        self.next = None
        # dados necessarios para o estado atual (qnt de vidas, qnt de poder etc)
        self.persist = {}

    def get_event(self, event):
        pass

    def startup(self, current_time, persist):
        # transferindo os dados persist do estado para a variavel
        self.persist = persist
        # o tempo inicial do estado é o tempo atual no momento do inicio
        self.start_time = current_time

    def cleanup(self):
        self.done = False
        return self.persist

    def update(self, surface, keys, current_time):
        pass


class Control(object):
    def __init__(self,caption,estado_inicial):
        self.caption = caption
        # obter uma referencia para uma superficie de exibição
        self.screen = pg.display.get_surface()
        # variavel p guardar se a tela esta aberta
        self.done = False
        # criando uma variavel para auxiliar na marcação do tempo
        self.clock = pg.time.Clock()
        # definindo a quantidade de frames por segundos
        self.fps = 60
        # variavel para armazenar o estado de todas as teclas do teclado (as teclas do definidas para controle do jogo)
        self.keys = pg.key.get_pressed()
        # dicionario de estados (estamos criando um dicionario para facilitar a edição)
        # as chaves e as variaveis do dicionario estao no arquivo constant
        self.state_dict = {}
        # variavel para armazenar a chave do estado
        self.state_name = None
        # variavel para armazenar o dado do estado
        self.state = estado_inicial
        self.trocou = False
        #criando o gerenciador de som
        self.som = gs.Sound(self.state)

    def setup_states(self, state_dict, start_state):
        self.state_dict = state_dict
        self.state_name = start_state
        self.state = self.state_dict[self.state_name]

    def update(self):
        # pega o tempo em milisegundos
        self.current_time = pg.time.get_ticks()
        # verificando se botao de sair foi pressionado
        if self.state.done:
            self.flip_state()
        # executa a função update do arquivo main_menu
        self.state.update(self.screen, self.keys, self.current_time)
        self.som.update()

    def flip_state(self):
        previous, self.state_name = self.state_name, self.state.next
        persist = self.state.cleanup()
        self.state = self.state_dict[self.state_name]
        self.state.startup(self.current_time, persist)

    def event_loop(self):
        for event in pg.event.get():
            # verificando se o evento foi quit
            if event.type == pg.QUIT:
                self.done = True
            # verificando se a tecla esta apertada
            elif event.type == pg.KEYDOWN:
                self.keys = pg.key.get_pressed()
            # verificando se a tecla foi solta
            elif event.type == pg.KEYUP:
                self.keys = pg.key.get_pressed()
            # pegando um novo evento
            self.state.get_event(event)



    def main(self):
        # enquando a tela nao foi fechada
        while not self.done:
            # executa a funçao de pegar eventos
            self.event_loop()
            # atualiza o estado
            self.update()
            # atualiza a tela
            pg.display.update()
            # atualiza o relogio
            self.clock.tick(self.fps)


def load_all_gfx(directory, colorkey=(255, 0, 255), accept=('.png', 'jpg', 'bmp')):
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pg.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def load_all_fonts(directory, accept='.ttf'):
    fonts = {}
    for font in os.listdir(directory):
        name, ext = os.path.splitext(font)
        if ext.lower() in accept:
            fonts[name] = os.path.join(directory, font)
    return fonts


def load_all_music(directory, accept=('.wav', '.mp3', '.ogg', '.mdi')):
    songs = {}
    for song in os.listdir(directory):
        name, ext = os.path.splitext(song)
        if ext.lower() in accept:
            songs[name] = os.path.join(directory, song)
    return songs


def load_all_sfx(directory, accept=('.wav', '.mpe', '.ogg', '.mdi')):
    effects = {}
    for fx in os.listdir(directory):
        name, ext = os.path.splitext(fx)
        if ext.lower() in accept:
            effects[name] = pg.mixer.Sound(os.path.join(directory, fx))
    return effects
