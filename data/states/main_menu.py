
import pygame as pg
from .. import setup, tools
from .. import constants as c


class Menu(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        persist = {}
        self.startup(0.0, persist)
        self.font = None

    def w_text(self, msg, color, font):
        self.font = font
        self.text = font.render(msg, True, color)
        return self.text

    def setup_background(self):
        self.background= pg.transform.scale(setup.GFX['Menu'],(c.TELA_LARGURA,c.TELA_ALTURA))
        self.botao1 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
        self.botao2 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        self.botao3 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        self.texto_TITULO = self.w_text(c.TITULO, c.BLACK, pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))
        self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.WHITE,  pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.BLACK, pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        self.texto_botao3 = self.w_text(c.TEXT_BOTAO3, c.BLACK, pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

    def setup_tela2(self):
        self.background = pg.transform.scale(setup.GFX['Menu'], (c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem = pg.Surface((c.TELA_LARGURA,c.TELA_ALTURA))
        self.imagem.set_alpha(30)
        self.imagem.fill(c.GRAY)
        self.botao_voltar = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        self.texto_voltar = self.w_text(c.TEXT_BOTAO_VOLTAR, c.BLACK,
                                         pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        self.text_tela2 = self.w_text(c.POS_TEXT_TIT_TELA2, c.BLACK, pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))

    def setup_tela3(self):
        self.background = pg.transform.scale(setup.GFX['Menu'], (c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem = pg.Surface((c.TELA_LARGURA,c.TELA_ALTURA))
        self.imagem.set_alpha(30)
        self.imagem.fill(c.GRAY)
        self.botao_voltar = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
        self.texto_voltar = self.w_text(c.TEXT_BOTAO_VOLTAR, c.BLACK,
                                         pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        self.text_tela3 = self.w_text(c.POS_TEXT_TIT_TELA3, c.BLACK, pg.font.Font(setup.FONTS[c.FONT_TITULO], c.FONT_TITULO_TAMANHO))

    def setup_cursor(self):
        self.cursor = c.BOTAO1

    def update_cursor (self, keys):
        if self.cursor == c.BOTAO1:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO2
                self.botao1 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao2 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
            elif keys[pg.K_UP]:
                self.cursor = c.BOTAO3
                self.botao1 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao3 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        elif self.cursor == c.BOTAO2:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO3
                self.botao2 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao3 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
            elif keys[pg.K_UP]:
                self.cursor = c.BOTAO1
                self.botao2 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao1 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
        elif self.cursor == c.BOTAO3:
            if keys[pg.K_DOWN]:
                self.cursor = c.BOTAO1
                self.botao3 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao1 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao1 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
            elif keys[pg.K_UP]:
                self.cursor = c.BOTAO2
                self.botao3 = pg.transform.scale(setup.GFX['button_amarelo2'], c.BOTOES_TAMANHO)
                self.botao2 = pg.transform.scale(setup.GFX['button_azul'], c.BOTOES_TAMANHO)
                self.texto_botao3 = self.w_text(c.TEXT_BOTAO1, c.BLACK,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))
                self.texto_botao2 = self.w_text(c.TEXT_BOTAO2, c.WHITE,
                                                 pg.font.Font(setup.FONTS[c.FONT_BOTOES], c.FONT_BOTOES_TAMANHO))

    def uptade(self, surface, keys):
        self.update_cursor(keys)
        surface.blit(self.texto_TITULO, c.POS_TITULO)
        surface.blit(self.texto_botao1, c.POS_TEXT_BOTAO1)
        surface.blit(self.texto_botao2, c.POS_TEXT_BOTAO2)
        surface.blit(self.texto_botao3, c.POS_TEXT_BOTAO3)
        surface.blit(self.texto_botao3, c.POS_TEXT_BOTAO3)
        surface.blit(self.background, c.POS_BACKGROUND)
        surface.blit(self.botao1, c.POS_BOTAO1)
        surface.blit(self.botao2, c.POS_BOTAO2)
        surface.blit(self.botao3, c.POS_BOTAO3)
