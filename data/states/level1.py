import pygame as pg
from .. import setup, tools
from .. import constants as c
from ..components import obstaculo
from ..components import callum

from os import path


class Level1(tools._State):
    def __init__(self):
        tools._State.__init__(self)
        self.all_sprites = pg.sprite.Group()
        self.testepycharm = pg.sprite.Group()


    def startup(self, current_time, persist):
        self.game_info = persist
        self.setup_background()
        self.setup_ground()
        self.setup_teto()
        self.setup_agua()
        self.setup_gaiola()
        self.setup_espinhos()
        self.setup_espinhos()
        self.setup_plataformas()
        self.setup_pedras()



        self.new()
        #self.events()


    def new(self):

        self.player = callum.Player(self)
        self.all_sprites.add(self.player)
        #self.platforms = pg.sprite.Group()


    """def run(self):
        # Game Loop
        
        self.playing = True
        while not self.done:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()"""




    """def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        #self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        self.spritesheet_player = Spritesheet(path.join("resources", "fonts", "callum.png"))
        #self.spritesheet_heart = Spritesheet(path.join(img_dir, HEART))
        #self.spritesheet_witch = Spritesheet(path.join(img_dir, WITCH))"""

    def setup_background(self):
        self.background = setup.GFX['Map_jogo_teste']
        self.back_rect = self.background.get_rect()
        largura = self.back_rect.width
        altura = self.back_rect.height
        self.level = pg.Surface((largura, altura)).convert()
        self.level_rect = self.level.get_rect()
        self.camera = setup.TELA.get_rect(bottom=self.level_rect.bottom)
        self.camera.x = self.game_info[c.CAMERA_INICIAL_X]

    def setup_ground(self):
        ground_rect1 = obstaculo.Obstaculo(0, 493, 175, 107)
        self.ground_rect1 = ground_rect1
        #ground_rect1 = obstaculo.Obstaculo(0, 600, 175, 107)
        #ground_rect1.rect.fill(c.RED)
        ground_rect2 = obstaculo.Obstaculo(172.4, 388, 178, 212)
        ground_rect3 = obstaculo.Obstaculo(591, 378, 104, 222)
        ground_rect4 = obstaculo.Obstaculo(596, 274, 180, 326)
        ground_rect5 = obstaculo.Obstaculo(913, 238, 214, 362)
        ground_rect6 = obstaculo.Obstaculo(1055, 143, 706, 32)
        ground_rect8 = obstaculo.Obstaculo(6937, 324, 2088, 276)
        ground_rect7 = obstaculo.Obstaculo(1055, 143, 33, 90)
        ground_rect9 = obstaculo.Obstaculo(1127, 529, 422, 71)
        ground_rect10 = obstaculo.Obstaculo(1301, 496, 106, 104)
        ground_rect11 = obstaculo.Obstaculo(1897, 495, 109, 105)
        ground_rect12 = obstaculo.Obstaculo(2005, 528, 821, 72)
        ground_rect13 = obstaculo.Obstaculo(3434, 496, 107, 104)
        ground_rect14 = obstaculo.Obstaculo(3541, 530, 817, 70)
        ground_rect15 = obstaculo.Obstaculo(4160, 498, 36, 36)
        ground_rect16 = obstaculo.Obstaculo(4194, 462, 36, 36)
        ground_rect17 = obstaculo.Obstaculo(4225, 429, 36, 36)
        ground_rect18 = obstaculo.Obstaculo(4259, 393, 36, 36)
        ground_rect19 = obstaculo.Obstaculo(4291, 361, 36, 36)
        ground_rect20 = obstaculo.Obstaculo(4325, 327, 36, 36)
        ground_rect21 = obstaculo.Obstaculo(4356, 319, 497, 281)
        ground_rect22 = obstaculo.Obstaculo(4844, 395, 43, 205)
        ground_rect23 = obstaculo.Obstaculo(4887, 413, 147, 187)
        ground_rect24 = obstaculo.Obstaculo(5173, 420, 184, 180)
        ground_rect25 = obstaculo.Obstaculo(5586, 416, 186, 184)
        ground_rect26 = obstaculo.Obstaculo(5591, 398, 47, 202)
        ground_rect27 = obstaculo.Obstaculo(6241, 397, 692, 203)

        self.group_ground = pg.sprite.Group(ground_rect1, ground_rect2, ground_rect3, ground_rect4,
                                            ground_rect5, ground_rect6, ground_rect7, ground_rect9,
                                            ground_rect10, ground_rect11, ground_rect12, ground_rect13,
                                            ground_rect14, ground_rect15, ground_rect16, ground_rect17,
                                            ground_rect18, ground_rect19, ground_rect20, ground_rect21,
                                            ground_rect22, ground_rect23, ground_rect24, ground_rect25,
                                            ground_rect26, ground_rect27, ground_rect8)
        for sprite in self.group_ground:
            self.all_sprites.add(sprite)

    def setup_teto(self):
        teto_rect1 = obstaculo.Obstaculo(0, 0, 173, 246)
        teto_rect2 = obstaculo.Obstaculo(173, 0, 776, 103)
        teto_rect3 = obstaculo.Obstaculo(949, 0, 988, 67)
        teto_rect4 = obstaculo.Obstaculo(1688, 172, 37, 41)
        teto_rect5 = obstaculo.Obstaculo(1650, 197, 39, 52)
        teto_rect6 = obstaculo.Obstaculo(1513, 197, 141, 85)
        teto_rect7 = obstaculo.Obstaculo(1404, 197, 107, 123)
        teto_rect8 = obstaculo.Obstaculo(1196, 197, 106, 156)
        teto_rect9 = obstaculo.Obstaculo(1935, 0, 771, 319)
        teto_rect10 = obstaculo.Obstaculo(1971, 0, 701, 353)
        teto_rect11 = obstaculo.Obstaculo(2077, 334, 209, 53)
        teto_rect12 = obstaculo.Obstaculo(2144, 358, 40, 66)
        teto_rect13 = obstaculo.Obstaculo(2352, 301, 209, 86)
        teto_rect14 = obstaculo.Obstaculo(2704, 0, 1657, 66)

        self.group_teto = pg.sprite.Group(teto_rect1, teto_rect2, teto_rect3, teto_rect4,
                                          teto_rect5, teto_rect6, teto_rect7, teto_rect8,
                                          teto_rect9, teto_rect10, teto_rect11, teto_rect12,
                                          teto_rect13, teto_rect14)





        for sprite in self.group_teto:
            self.all_sprites.add(sprite)

    def setup_agua(self):
        agua_rect1 = obstaculo.Obstaculo(1547, 566, 354, 34)
        agua_rect2 = obstaculo.Obstaculo(2824, 563, 611, 37)
        agua_rect3 = obstaculo.Obstaculo(5034, 544, 123, 56)
        agua_rect4 = obstaculo.Obstaculo(5356, 544, 250, 56)

        self.group_agua = pg.sprite.Group(agua_rect1, agua_rect2, agua_rect3, agua_rect4)




        for sprite in self.group_agua:
            self.all_sprites.add(sprite)

    def setup_gaiola(self):
        gaiola_rect1 = obstaculo.Obstaculo(1434, 334, 51, 86)

        self.group_gaiola = pg.sprite.Group(gaiola_rect1)




        for sprite in self.group_gaiola:
            self.all_sprites.add(sprite)

    def setup_espinhos(self):
        espinho_rect1 = obstaculo.Obstaculo(350, 387, 141, 213)
        espinho_rect2 = obstaculo.Obstaculo(775, 532, 139, 68)
        espinho_rect3 = obstaculo.Obstaculo(1123, 317, 73, 28)
        espinho_rect4 = obstaculo.Obstaculo(1334, 283, 76, 26)

        self.group_espinho = pg.sprite.Group(espinho_rect1, espinho_rect2, espinho_rect3, espinho_rect4)



        for sprite in self.group_espinho:
            self.all_sprites.add(sprite)

    def setup_plataformas(self):
        plataforma_rect1 = obstaculo.Obstaculo(1654, 389, 110, 37)
        plataforma_rect2= obstaculo.Obstaculo(2905, 381, 110, 37)
        plataforma_rect3 = obstaculo.Obstaculo(3076, 274, 110, 37)
        plataforma_rect4 = obstaculo.Obstaculo(3258, 486, 110, 37)
        plataforma_rect5 = obstaculo.Obstaculo(5443, 222, 185, 69)
        plataforma_rect6 = obstaculo.Obstaculo(5713, 102, 181, 71)
        plataforma_rect7 = obstaculo.Obstaculo(5943, 265, 186, 75)

        self.group_plataforma = pg.sprite.Group(plataforma_rect1, plataforma_rect2, plataforma_rect3, plataforma_rect4,
                                                plataforma_rect5, plataforma_rect6, plataforma_rect7)


        for sprite in self.group_plataforma:
            self.all_sprites.add(sprite)


    def setup_pedras(self):
        pedra_rect1 = obstaculo.Obstaculo(5800, 28, 94, 95)
        pedra_rect2 = obstaculo.Obstaculo(7686, 228, 155, 372)
        pedra_rect3 = obstaculo.Obstaculo(7755, 192, 87, 408)
        pedra_rect4 = obstaculo.Obstaculo(6478, 339, 195, 261)
        pedra_rect5 = obstaculo.Obstaculo(6532, 314, 56, 286)
        pedra_rect6 = obstaculo.Obstaculo(6605, 322, 47, 278)
        pedra_rect7 = obstaculo.Obstaculo(6426, 370, 41, 230)
        pedra_rect8 = obstaculo.Obstaculo(6664, 373, 34, 227)

        self.group_pedra = pg.sprite.Group(pedra_rect1, pedra_rect2, pedra_rect3, pedra_rect4,
                                           pedra_rect5, pedra_rect6, pedra_rect7, pedra_rect8)


        for sprite in self.group_pedra:
            self.all_sprites.add(sprite)

    def check_callum_y_colide(self):
        ground_plataforma = pg.sprite.spritecollideany(self.player,self.group_ground)

        if ground_plataforma:
            self.ajustar_callum_y(ground_plataforma)

    def ajustar_callum_y(self,collider):
        print("ground ")
        print( collider.rect.top)
        print("player ")
        print(self.player.rect.bottom)
        if collider.rect.top < (self.player.pos.y+1000):
            print("colidiu")
            self.player.vel.y = 0
            self.player.pos.y = collider.rect.top-55
            print("groundcolisao ")
            print( collider.rect.top)
            print("playercolisao ")
            print(self.player.rect.bottom)

    def blit_tela(self, surface):
        surface.blit(self.level, (0, 0), self.camera)
        self.level.blit(self.background, self.camera, self.camera)
        setup.TELA.blit(self.player.image, (self.player.pos.x, self.player.pos.y))



    def update(self, surface, keys, current_time):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        
        self.check_callum_y_colide()
        self.blit_tela(surface)
        #pg.draw.rect(surface,c.RED,self.ground_rect1.rect)
        self.player.update(self.current_time)
        self.events()

        # check if callum hits a platform if falling
        '''if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                print("hitou")
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                        self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.bottom:
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False'''




    def update_camera(self):
        pass


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                self.done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    print("indo cima dnv")
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.jump_cut()

            """if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.player.Crouch()

            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self.player.crouch_cut()"""

    '''def draw(self):
        # Game Loop - draw

        #setup.TELA.fill(c.BGCOLOR)
        self.all_sprites.draw(setup.TELA)
        setup.TELA.blit(self.player.image, self.player.rect)

        #self.player.show_heart()
        # self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 20)
        # *after* drawing everything, flip the display
        pg.display.flip()'''


















