
import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. import game_sound as gs


class Game_Over(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        persist = {c.SCORE: 0,
                   c.VIDAS: 3,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_INICIAL_X: 0,
                   c.DEAD: False,
                   c.PODER_1: 5,
                   c.PODER_2: 0,
                   c.EGG: False}
        self.startup(0.0, persist)
        self.keys = None
        #self.som = gs.Sound()

    def startup(self, current_time, persist):
        self.next = c.MAIN_MENU
        self.persist = persist
        self.setup_background()
        self.setup_botoes_default()
        self.setup_cursor()

    # retorna o texto pronto para ser apresentado na tela (aguardando apenas o blit)
    def w_text(self, msg, color, font):
        self.font = font
        self.text = font.render(msg, True, color)
        return self.text

    # cria os botoes e os textos dos botoes como eles devem aparecer quando a cada tela é carregada
    # botao redondo selecionado e demais normal (amarelos)
    def setup_botoes_default(self):
        self.botao_perm2 =  pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)
        self.botao_sim = self.setup_botao()
        self.botao_nao = self.setup_botao()

        self.text_sim = self.setup_texto_botao(c.TEXT_SIM, c.FONT_BOTOES_TAMANHO)
        self.text_nao = self.setup_texto_botao(c.TEXT_NAO, c.FONT_BOTOES_TAMANHO)


    # configura os botoes no seu estado deselecionados (amarelos)
    def setup_botao(self):
        self.botao = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        return self.botao

    # configura o texto no seu estado deselecionado (preto)
    def setup_texto_botao(self, texto, tamanho_fonte):
        self.texto = self.w_text(texto, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_BOTOES], tamanho_fonte))
        return self.texto

    # configura os botoes no seu estado selecionados (azul)
    def setup_botao_selecionado(self):
        self.botao = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        return self.botao

    # configura o texto no seu estado deselecionado (branco)
    def setup_texto_botao_selecionado(self, texto, tamanho_fonte):
        self.texto = self.w_text(texto, c.WHITE,
                                      pg.font.Font(setup.FONTS[c.FONT_BOTOES], tamanho_fonte))
        return self.texto

    #prepara o fundo de cada tela do Menu e o Titulo
    def setup_background(self):
        self.background = setup.GFX['Menu']
        self.imagem = pg.Surface((c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem.set_alpha(130)
        self.imagem.fill(c.GRAY)

        self.text_game_over = self.w_text(c.TEXT_GAME_OVER, c.BLACK,
                                        pg.font.Font(setup.FONTS[c.FONT_BOTOES], 80))
        self.text_deseja = self.w_text(c.TEXT_DESEJA, c.BLACK,
                                          pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))


    # define a posição default do cursor e qual tela aparece primeiro
    def setup_cursor(self):
        self.cursor = c.BOTAO0

    def mover_cursor(self):
        setup.SFX['menu_select'].play()
        pg.time.wait(200)

    # atualiza qual botao deve estar selecionado na tela Ajuda e Creditos
    def update_cursor_tela_game_over(self, keys):
        if self.cursor == c.BOTAO0:
            if keys[pg.K_DOWN]:
                self.mover_cursor()
                self.cursor = c.BOTAO_SIM
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_sim = self.setup_botao_selecionado()

                self.text_sim = self.setup_texto_botao_selecionado(c.TEXT_SIM, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_SIM:
            if keys[pg.K_UP]:
                self.mover_cursor()
                self.cursor = c.BOTAO0
                self.botao_sim = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_sim = self.setup_texto_botao(c.TEXT_SIM, c.FONT_BOTOES_TAMANHO)
            elif keys[pg.K_RIGHT]:
                self.mover_cursor()
                self.cursor = c.BOTAO_NAO
                self.botao_sim = self.setup_botao()
                self.botao_nao = self.setup_botao_selecionado()

                self.text_sim = self.setup_texto_botao(c.TEXT_SIM, c.FONT_BOTOES_TAMANHO)
                self.text_nao = self.setup_texto_botao_selecionado(c.TEXT_NAO, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_NAO:
            if keys[pg.K_UP]:
                self.mover_cursor()
                self.cursor = c.BOTAO0
                self.botao_nao = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_nao = self.setup_texto_botao(c.TEXT_NAO, c.FONT_BOTOES_TAMANHO)
            elif keys[pg.K_LEFT]:
                self.botao_nao = self.setup_botao()
                self.botao_sim = self.setup_botao_selecionado()

                self.text_nao = self.setup_texto_botao(c.TEXT_NAO, c.FONT_BOTOES_TAMANHO)
                self.text_sim = self.setup_texto_botao_selecionado(c.TEXT_SIM, c.FONT_BOTOES_TAMANHO)

    # Apresenta as imagens e textos da tela Ajuda
    def blit_tela(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, [0, 0])
        surface.blit(self.botao_sim, c.POS_BOTAO_SIM)
        surface.blit(self.botao_nao, c.POS_BOTAO_NAO)
        surface.blit(self.botao_perm2, c.POS_BOTAO_PERM2)
        surface.blit(self.text_game_over, c.POS_TEXT_GAME_OVER)
        surface.blit(self.text_deseja, c.POS_TEXT_DESEJA)
        surface.blit(self.text_sim, c.POS_TEXT_SIM)
        surface.blit(self.text_nao, c.POS_TEXT_NAO)

    # Controla a tela Menu
    def tela(self, surface, keys):
        input_list = [pg.K_RETURN]
        self.update_cursor_tela_game_over(keys)
        self.blit_tela(surface)
         # se o cursor estiver em uma posição diferente do botao auxiliar (redondo) e for
        # pressionada a tecla enter troca de tela
        if self.cursor != c.BOTAO0:
            for input in input_list:
                if keys[input]:
                    if self.cursor == c.BOTAO_SIM:
                        self.next = c.LEVEL1
                        self.done = True
                    elif self.cursor == c.BOTAO_NAO:
                        self.next = c.MAIN_MENU
                        self.done = True
                    self.cursor = c.BOTAO0



    #atualiza as informações
    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.tela(surface, keys)










