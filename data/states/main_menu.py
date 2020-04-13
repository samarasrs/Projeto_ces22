
import pygame as pg
from .. import setup, tools
from .. import constants as c


class Menu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        persist = {}
        self.startup(0.0, persist)
        self.keys = None

    def startup(self, current_time, persist):
        self.persist = persist
        self.setup_background()
        self.setup_botoes_default()
        self.setup_cursor()

    def w_text(self, msg, color, font):
        self.font = font
        self.text = font.render(msg, True, color)
        return self.text

    def setup_botoes_default(self):
        self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)
        self.botao_jogar = self.setup_botao()
        self.botao_ajuda = self.setup_botao()
        self.botao_creditos = self.setup_botao()
        self.botao_voltar = self.setup_botao()

        #self.text_perm1 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
        #self.text_perm2 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)
        self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)
        self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)
        self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
        self.text_voltar = self.setup_texto_botao(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)


    def setup_botao(self):
        self.botao = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        return self.botao

    def setup_texto_botao(self, texto, tamanho_fonte):
        self.texto = self.w_text(texto, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_BOTOES], tamanho_fonte))
        return self.texto

    def setup_botao_selecionado(self):
        self.botao = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        return self.botao

    def setup_texto_botao_selecionado(self, texto, tamanho_fonte):
        self.texto = self.w_text(texto, c.WHITE,
                                      pg.font.Font(setup.FONTS[c.FONT_BOTOES], tamanho_fonte))
        return self.texto

    def setup_background(self):
        # tela 1
        self.background= pg.transform.scale(setup.GFX['Menu'],(c.TELA_LARGURA,c.TELA_ALTURA))

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
        # Titulo tela 3
        self.text_tela3 = self.w_text(c.TEXT_TELA3, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))

    def setup_cursor(self):
        self.cursor = c.BOTAO0
        self.tela = c.TELA1

    def update_cursor_tela1(self, keys):
        if self.cursor == c.BOTAO0:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO_AJUDA
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_ajuda = self.setup_botao_selecionado()

                self.text_perm1 = self.setup_texto_botao(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)
                self.text_ajuda = self.setup_texto_botao_selecionado(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)

            if keys[pg.K_RIGHT]:
                self.cursor = c.BOTAO_JOGAR
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_jogar = self.setup_botao_selecionado()

                self.text_perm1 = self.setup_texto_botao(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)
                self.text_jogar = self.setup_texto_botao_selecionado(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_JOGAR:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO_CREDITOS
                self.botao_jogar = self.setup_botao()
                self.botao_creditos = self.setup_botao_selecionado()

                self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)
                self.text_creditos = self.setup_texto_botao_selecionado(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)

            elif keys[pg.K_LEFT]:
                self.cursor = c.BOTAO0
                self.botao_jogar = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_jogar = self.setup_texto_botao(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)
                self.text_perm1 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)

        elif self.cursor == c.BOTAO_CREDITOS:
            if keys[pg.K_UP]:
                self.cursor = c.BOTAO_JOGAR
                self.botao_creditos = self.setup_botao()
                self.botao_jogar = self.setup_botao_selecionado()

                self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
                self.text_jogar = self.setup_texto_botao_selecionado(c.TEXT_JOGAR, c.FONT_BOTOES_TAMANHO)

            elif keys[pg.K_LEFT]:
                self.cursor = c.BOTAO_AJUDA
                self.botao_creditos = self.setup_botao()
                self.botao_ajuda = self.setup_botao_selecionado()

                self.text_creditos = self.setup_texto_botao(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)
                self.text_ajuda = self.setup_texto_botao_selecionado(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_AJUDA:
            if keys[pg.K_UP]:
                self.cursor = c.BOTAO0
                self.botao_ajuda = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)
                self.text_perm1 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)

            elif keys[pg.K_RIGHT]:
                self.cursor = c.BOTAO_CREDITOS
                self.botao_ajuda= self.setup_botao()
                self.botao_creditos = self.setup_botao_selecionado()

                self.text_ajuda = self.setup_texto_botao(c.TEXT_AJUDA, c.FONT_BOTOES_TAMANHO)
                self.text_creditos = self.setup_texto_botao_selecionado(c.TEXT_CREDITO, c.FONT_BOTOES_TAMANHO)


    def update_cursor_tela23(self, keys):
        if self.cursor == c.BOTAO0:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO_VOLTA
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_amarelo'], c.BOTAO_PERM_TAMANHO)
                self.botao_voltar = self.setup_botao_selecionado()

                self.text_perm1 = self.setup_texto_botao(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)
                self.text_voltar = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)

        elif self.cursor == c.BOTAO_VOLTA:
            if keys[pg.K_UP]:
                self.cursor = c.BOTAO0
                self.botao_voltar = self.setup_botao()
                self.botao_perm = self.botao = pg.transform.scale(setup.GFX['circulo_azul'], c.BOTAO_PERM_TAMANHO)

                self.text_voltar = self.setup_texto_botao(c.TEXT_BOTAO_VOLTAR, c.FONT_BOTOES_TAMANHO)
                self.text_perm1 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM1, c.FONT_BOTAO_PERM)
                self.text_perm2 = self.setup_texto_botao_selecionado(c.TEXT_BOTAO_PERM2, c.FONT_BOTAO_PERM)

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
        #surface.blit(self.text_perm1, c.POS_TEXT_BOTAO_PERM1_TELA1)
        #surface.blit(self.text_perm2, c.POS_TEXT_BOTAO_PERM2_TELA1)

    def blit_tela2(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, c.POS_BACKGROUND)
        surface.blit(self.botao_voltar, c.POS_BOTAO_VOLTAR)
        surface.blit(self.botao_perm, c.POS_BOTAO_PERM)
        surface.blit(self.text_tela2, c.POS_TEXT_TIT_TELA2)
        surface.blit(self.text_voltar, c.POS_TEXT_VOLTAR)


    def blit_tela3(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, c.POS_BACKGROUND)
        surface.blit(self.botao_voltar, c.POS_BOTAO_VOLTAR)
        surface.blit(self.botao_perm, c.POS_BOTAO_PERM)
        surface.blit(self.text_tela3, c.POS_TEXT_TIT_TELA3)
        surface.blit(self.text_voltar, c.POS_TEXT_VOLTAR)


    def tela1(self, surface, keys):
        input_list = [pg.K_RETURN]
        if self.tela == c.TELA1:
            self.update_cursor_tela1(keys)
            self.blit_menu(surface)
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        if self.cursor == c.BOTAO_AJUDA:
                            self.tela = c.TELA2
                            self.setup_botoes_default()
                        elif self.cursor == c.BOTAO_CREDITOS:
                            self.tela = c.TELA3
                            self.setup_botoes_default()
                        self.cursor = c.BOTAO0

    def tela2(self, surface, keys):
        input_list = [pg.K_RETURN]
        if self.tela == c.TELA2:
            self.update_cursor_tela23(keys)
            self.blit_tela2(surface)
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        if self.cursor == c.BOTAO_VOLTA:
                            self.tela = c.TELA1
                            self.setup_botoes_default()
                        self.cursor = c.BOTAO0

    def tela3(self, surface, keys):
        input_list = [pg.K_RETURN]
        if self.tela == c.TELA3:
            self.update_cursor_tela23(keys)
            self.blit_tela3(surface)
            if self.cursor != c.BOTAO0:
                for input in input_list:
                    if keys[input]:
                        if self.cursor == c.BOTAO_VOLTA:
                            self.tela = c.TELA1
                            self.setup_botoes_default()
                        self.cursor = c.BOTAO0

    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.tela1(surface, keys)
        self.tela2(surface, keys)
        self.tela3(surface, keys)









