
import pygame as pg
from .. import setup, tools
from .. import constants as c


class Menu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        persist = {}
        self.startup(0.0, persist)

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
        # botoes tela 1
        self.botao1 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        self.botao2 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)

        self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.WHITE,
                                        pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.BLACK,
                                        pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        # botoes tela 2
        self.botao_voltar = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        self.botao_creditos = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        self.texto_voltar = self.w_text(c.TEXT_BOTAO_VOLTAR, c.WHITE,
                                        pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

        self.text_creditos = self.w_text(c.TEXT_BOTAO3, c.BLACK,
                                         pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

        # botoes tela 3
        self.botao_voltar_tela3 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        self.texto_voltar_tela3 = self.w_text(c.TEXT_BOTAO_VOLTAR, c.WHITE,
                                              pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

    def setup_background(self):
        # tela 1
        self.background= pg.transform.scale(setup.GFX['Menu'],(c.TELA_LARGURA,c.TELA_ALTURA))

        #tela 2 e 3
        self.imagem = pg.Surface((c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem.set_alpha(130)
        self.imagem.fill(c.GRAY)

        # Titulo tela 1
        self.texto_TITULO = self.w_text(c.TITULO, c.BLACK,
                                        pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))
        # Titulo tela 2
        self.text_tela2 = self.w_text(c.TEXT_TELA2, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))
        # Titulo tela 3
        self.text_tela3 = self.w_text(c.TEXT_TELA3, c.BLACK,
                                      pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))

    def setup_cursor(self):
        self.cursor = c.BOTAO1
        self.tela = c.TELA1

    def update_cursor_tela1(self, keys):
        if self.cursor == c.BOTAO1:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO2
                self.botao1 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao2 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

        elif self.cursor == c.BOTAO2:
            if keys[pg.K_UP]:
                self.cursor = c.BOTAO1
                self.botao2 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao1 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

    def update_cursor_tela2(self, keys):
        if self.cursor == c.BOTAO1:
            if keys[pg.K_RIGHT]:
                self.cursor = c.BOTAO2
                self.botao_voltar = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao_creditos = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_voltar = self.w_text(c.TEXT_BOTAO_VOLTAR, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO3, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

        elif self.cursor == c.BOTAO2:
            if keys[pg.K_LEFT]:
                self.cursor = c.BOTAO1
                self.botao_creditos = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao_voltar = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO3, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_voltar = self.w_text(c.TEXT_BOTAO_VOLTAR, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

    def blit_menu(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.botao1, c.POS_BOTAO1)
        surface.blit(self.botao2, c.POS_BOTAO2)
        surface.blit(self.texto_TITULO, c.POS_TITULO)
        surface.blit(self.texto_botao1, c.POS_TEXT_BOTAO1)
        surface.blit(self.texto_botao2, c.POS_TEXT_BOTAO2)

    def blit_tela2(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, c.POS_BACKGROUND)
        surface.blit(self.botao_voltar, c.POS_BOTAO_VOLTAR)
        surface.blit(self.botao_creditos, c.POS_BOTAO3)
        surface.blit(self.text_tela2, c.POS_TEXT_TIT_TELA2)
        surface.blit(self.texto_voltar, c.POS_TEXT_BOTAO_VOLTAR)
        surface.blit(self.text_creditos, c.POS_TEXT_BOTAO3)

    def blit_tela3(self, surface):
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.imagem, c.POS_BACKGROUND)
        surface.blit(self.botao_voltar_tela3, c.POS_BOTAO_VOLTAR)
        surface.blit(self.text_tela3, c.POS_TEXT_TIT_TELA3)
        surface.blit(self.texto_voltar_tela3, c.POS_TEXT_BOTAO_VOLTAR)

    def tela1(self, surface, keys):
        input_list = [pg.K_RETURN, pg.K_BACKSPACE]
        if self.tela == c.TELA1:
            self.update_cursor_tela1(keys)
            self.blit_menu(surface)
            for input in input_list:
                if keys[input]:
                    if self.cursor == c.BOTAO2:
                        self.tela = c.TELA2
                        self.trocou = True
                        self.setup_botoes_default()
                    self.cursor = c.BOTAO0

    def tela2(self, surface, keys):
        input_list = [pg.K_RETURN, pg.K_BACKSPACE]
        if self.tela == c.TELA2:
            self.update_cursor_tela2(keys)
            self.blit_tela2(surface)
            for input in input_list:
                if keys[input]:
                    if self.cursor == c.BOTAO1:
                        self.tela = c.TELA1
                        self.trocou = True
                        self.setup_botoes_default()
                    else:
                        self.tela = c.TELA3
                        self.trocou = True
                    self.cursor = c.BOTAO0

    def tela3(self, surface, keys):
        input_list = [pg.K_RETURN, pg.K_BACKSPACE]
        if self.tela == c.TELA3:
            self.blit_tela3(surface)
            for input in input_list:
                if keys[input]:
                    self.tela = c.TELA1


    def update(self, surface, keys, current_time):
        self.current_time = current_time
        self.tela1(surface, keys)
        self.tela2(surface, keys)
        self.tela3(surface, keys)








