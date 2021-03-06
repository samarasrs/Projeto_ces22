
import pygame as pg
from .. import setup, tools
from .. import constants as c
from .. import game_sound as gs


class Menu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        # o persist vai definir as variaveis iniciais do jogo
        persist = {c.SCORE: 0,
                   c.VIDAS: 3,
                   c.CURRENT_TIME: 0.0,
                   c.LEVEL_STATE: None,
                   c.CAMERA_INICIAL_X: 0,
                   c.DEAD: False,
                   c.EGG: False}
        self.startup(0.0, persist)
        self.keys = None
        self.som = gs.Sound(c.MAIN_MENU)
        self.som.update()


    def startup(self, current_time, persist):
        self.next = c.LEVEL1
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
        self.botao_perm  = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)
        self.botao_jogar = self.setup_botao()
        self.botao_ajuda = self.setup_botao()
        self.botao_creditos = self.setup_botao()
        self.botao_voltar = self.setup_botao()

        self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)
        self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)
        self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
        self.text_voltar = self.setup_texto_botao(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)

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
        # tela 1
        self.background= setup.GFX['Menu']

        #tela 2 e 3
        self.imagem = pg.Surface((c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem.set_alpha(130)
        self.imagem.fill(c.GRAY)

        # Titulo tela 1
        self.text_TITULO = self.w_text(c.TITULO, c.BLACK,
                                        pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))
        # Titulo tela 2
        self.text_tela2 = self.w_text(c.TEXT_TELA2, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))

        self.up = pg.transform.scale(setup.GFX['up'], (50, 50))
        self.right = pg.transform.scale(setup.GFX['right'], (50, 50))
        self.left = pg.transform.scale(setup.GFX['left'], (50, 50))
        self.teclaS = pg.transform.scale(setup.GFX['S'], (50, 50))
        self.text_tela2_1 = self.w_text("- Objetivo: ", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_2 = self.w_text("Leve o Ovo do Principe Dragão até um lugar seguro.", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_3 = self.w_text("- Teclas utilizadas", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_4 = self.w_text("andar para esquerda", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_5 = self.w_text("andar para direita", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_6 = self.w_text("pular", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela2_7 = self.w_text("atacar", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))

        # Titulo tela 3

        self.text_tela3 = self.w_text(c.TEXT_TELA3, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))
        self.text_tela3_1 = self.w_text("- Sprite sheets: ", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 25))
        self.text_tela3_2 = self.w_text("https://bakudas.itch.io ", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela3_3 = self.w_text("https://opengameart.org", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela3_4 = self.w_text("Obs: Mapa montado pela equipe.", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela3_5 = self.w_text("- Músicas e efeitos sonoros: ", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 25))
        self.text_tela3_6 = self.w_text("https://opengameart.org", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))
        self.text_tela3_7 = self.w_text("- Criadores: ", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 25))
        self.text_tela3_8 = self.w_text("Carlos Figueiredo, Matheus Martins e Samara Ribeiro", c.BLACK, pg.font.Font(setup.FONTS['JMH_Typewriter'], 22))




    # define a posição default do cursor e qual tela aparece primeiro
    def setup_cursor(self):
        self.cursor = c.BOTAO0
        self.tela = c.TELA1

    def mover_cursor(self):
        setup.SFX['menu_select'].play()
        pg.time.wait(200)

    def update_cursor_tela1(self, keys):
        if self.cursor == c.BOTAO0:
            if keys[pg.K_DOWN]:
                self.mover_cursor()
                self.cursor = c.BOTAO_AJUDA
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_ajuda = self.setup_botao_selecionado()

                self.text_ajuda = self.setup_texto_botao_selecionado(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)

            if keys[pg.K_RIGHT]:
                self.mover_cursor()
                self.cursor = c.BOTAO_JOGAR
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_jogar = self.setup_botao_selecionado()

                self.text_jogar = self.setup_texto_botao_selecionado(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_JOGAR:
            if keys[pg.K_DOWN]:
                self.mover_cursor()
                self.cursor = c.BOTAO_CREDITOS
                self.botao_jogar = self.setup_botao()
                self.botao_creditos = self.setup_botao_selecionado()

                self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)
                self.text_creditos = self.setup_texto_botao_selecionado(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)

            elif keys[pg.K_LEFT]:
                self.mover_cursor()
                self.cursor = c.BOTAO0
                self.botao_jogar = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_CREDITOS:
            if keys[pg.K_UP]:
                self.mover_cursor()
                self.cursor = c.BOTAO_JOGAR
                self.botao_creditos = self.setup_botao()
                self.botao_jogar = self.setup_botao_selecionado()

                self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
                self.text_jogar = self.setup_texto_botao_selecionado(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)

            elif keys[pg.K_LEFT]:
                self.mover_cursor()
                self.cursor = c.BOTAO_AJUDA
                self.botao_creditos = self.setup_botao()
                self.botao_ajuda = self.setup_botao_selecionado()

                self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
                self.text_ajuda = self.setup_texto_botao_selecionado(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_AJUDA:
            if keys[pg.K_UP]:
                self.mover_cursor()
                self.cursor = c.BOTAO0
                self.botao_ajuda = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)

            elif keys[pg.K_RIGHT]:
                self.mover_cursor()
                self.cursor = c.BOTAO_CREDITOS
                self.botao_ajuda= self.setup_botao()
                self.botao_creditos = self.setup_botao_selecionado()

                self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)
                self.text_creditos = self.setup_texto_botao_selecionado(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)

    # atualiza qual botao deve estar selecionado na tela Ajuda e Creditos
    def update_cursor_tela23(self, keys):
        if self.cursor == c.BOTAO0:
            if keys[pg.K_DOWN]:
                self.mover_cursor()
                self.cursor = c.BOTAO_VOLTA
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_voltar = self.setup_botao_selecionado()

                self.text_voltar = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_VOLTA:
            if keys[pg.K_UP]:
                self.mover_cursor()
                self.cursor = c.BOTAO0
                self.botao_voltar = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_voltar = self.setup_texto_botao(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)

    # Apresenta as imagens e textos da tela Menu
    def blit_menu(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.botao_jogar, c.POS_BOTAO_JOGAR)
        surface.blit(self.botao_ajuda, c.POS_BOTAO_AJUDA)
        surface.blit(self.botao_creditos, c.POS_BOTAO_CREDITO)
        surface.blit(self.botao_perm, c.POS_BOTAO_PERM_TELA1)
        surface.blit(self.text_TITULO, c.POS_TITULO)
        surface.blit(self.text_jogar, c.POS_TEXT_JOGAR)
        surface.blit(self.text_ajuda, c.POS_TEXT_AJUDA)
        surface.blit(self.text_creditos, c.POS_TEXT_CREDITO)

    # Apresenta as imagens e textos da tela Ajuda
    def blit_tela2(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, [0, 0])
        surface.blit(self.botao_voltar, c.POS_BOTAO_VOLTAR)
        surface.blit(self.botao_perm, c.POS_BOTAO_PERM)
        surface.blit(self.text_tela2, c.POS_TEXT_TIT_TELA2)
        surface.blit(self.text_voltar, c.POS_TEXT_VOLTAR)
        surface.blit(self.text_tela2_1, [30, 130])
        surface.blit(self.text_tela2_2, [90, 160])
        surface.blit(self.text_tela2_3, [30, 200])
        surface.blit(self.text_tela2_4, [150, 240])
        surface.blit(self.text_tela2_5, [460, 240])
        surface.blit(self.text_tela2_6, [150, 300])
        surface.blit(self.text_tela2_7, [460, 300])
        surface.blit(self.left, [90, 230])
        surface.blit(self.right, [400, 230])
        surface.blit(self.up, [90, 290])
        surface.blit(self.teclaS, [400, 290])


    # Apresenta as imagens e textos da tela Creditos
    def blit_tela3(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, [0, 0])
        surface.blit(self.botao_voltar, c.POS_BOTAO_VOLTAR)
        surface.blit(self.botao_perm, c.POS_BOTAO_PERM)
        surface.blit(self.text_tela3, c.POS_TEXT_TIT_TELA3)
        surface.blit(self.text_voltar, c.POS_TEXT_VOLTAR)
        surface.blit(self.text_tela3_1, [30, 240])
        surface.blit(self.text_tela3_2, [90, 270])
        surface.blit(self.text_tela3_3, [90, 300])
        surface.blit(self.text_tela3_4, [90, 330])
        surface.blit(self.text_tela3_5, [30, 390])
        surface.blit(self.text_tela3_6, [90, 420])
        surface.blit(self.text_tela3_7, [30, 150])
        surface.blit(self.text_tela3_8, [90, 180])




    # Controla a tela Menu
    def tela1(self, surface, keys):
        input_list = [pg.K_RETURN]
        # se a tela for a 1 apresenta as informações da tela Menu
        if self.tela == c.TELA1:
            self.update_cursor_tela1(keys)
            self.blit_menu(surface)
            # se o cursor estiver em uma posição diferente do botao auxiliar (redondo) e for
            # pressionada a tecla enter troca de tela
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        setup.SFX['menu_entrar'].play()
                        pg.time.wait(500)
                        if self.cursor == c.BOTAO_AJUDA:
                            self.tela = c.TELA2
                            self.setup_botoes_default()
                        elif self.cursor == c.BOTAO_CREDITOS:
                            self.tela = c.TELA3
                            self.setup_botoes_default()
                        elif self.cursor == c.BOTAO_JOGAR:
                            self.done = True
                        self.cursor = c.BOTAO0

    # Controla a tela Ajuda
    def tela2(self, surface, keys):
        input_list = [pg.K_RETURN]
        # se a tela for a 2 apresenta as informações da tela Ajuda
        if self.tela == c.TELA2:
            self.update_cursor_tela23(keys)
            self.blit_tela2(surface)
            # se o cursor estiver em uma posição diferente do botao auxiliar (redondo) e for
            # pressionada a tecla enter troca de tela
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        setup.SFX['menu_entrar'].play()
                        pg.time.wait(500)
                        if self.cursor == c.BOTAO_VOLTA:
                            self.tela = c.TELA1
                            self.setup_botoes_default()
                        self.cursor = c.BOTAO0

    # Controla a tela Creditos
    def tela3(self, surface, keys):
        input_list = [pg.K_RETURN]
        # se a tela for a 3 apresenta as informações da tela Creditos
        if self.tela == c.TELA3:
            self.update_cursor_tela23(keys)
            self.blit_tela3(surface)
            # se o cursor estiver em uma posição diferente do botao auxiliar (redondo) e for
            # pressionada a tecla enter troca de tela
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        setup.SFX['menu_entrar'].play()
                        pg.time.wait(500)
                        if self.cursor == c.BOTAO_VOLTA:
                            self.tela = c.TELA1
                            self.setup_botoes_default()
                        self.cursor = c.BOTAO0

    #atualiza as informações
    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.tela1(surface, keys)
        self.tela2(surface, keys)
        self.tela3(surface, keys)









