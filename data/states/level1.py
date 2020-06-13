import pygame as pg
import os
from .. import setup, tools
from .. import constants as c
from ..components import obstaculo, callum2, witch, egg



class Level1(tools._State):
    # classe do level 1
    def __init__(self):
        # classe filha de State
        tools._State.__init__(self)


    def startup(self, current_time, persist):
        # metodo que insere os dados iniciais no level
        self.game_info = persist
        self.game_info[c.CURRENT_TIME] = current_time
        self.game_info[c.CALLUM_DEAD] = False
        self.setup_background()
        self.setup_ground()
        self.setup_teto()
        self.setup_agua()
        self.setup_gaiola()
        self.setup_espinhos()
        self.setup_espinhos()
        self.setup_plataformas()
        self.setup_pedras()
        self.setup_callum()
        self.setup_witch()

        self.setup_egg()



        self.setup_spritegroups()
        self.setup_barraca()

# SETUPS


    def setup_egg(self):
        self.egg1 = egg.Egg(True)
        self.egg1.rect.midbottom = (50,50)


    def setup_witch(self):
        # criando os objetos inimigos e atribuindo uma posição para eles
        self.witch1 = witch.Witch(True)
        self.witch1.rect.midbottom = (742, 283)
        self.witch2 = witch.Witch(True)
        self.witch2.rect.midbottom = (334, 388)
        self.witch3 = witch.Witch(True)
        self.witch3.rect.midbottom = (1525, 143)
        self.witch4 = witch.Witch(True)
        self.witch4.rect.midbottom = (1375, 496)
        self.witch5 = witch.Witch(True)
        self.witch5.rect.midbottom = (2596, 528)
        self.witch6 = witch.Witch(True)
        self.witch6.rect.midbottom = (4654, 319)
        self.witch7 = witch.Witch(True)
        self.witch7.rect.midbottom = (8540, 324)
        self.morcego1 = witch.Witch(False)
        self.morcego1.rect.midbottom = (3970, 500)
        self.morcego2 = witch.Witch(False)
        self.morcego2.rect.midbottom = (5310, 400)
        self.morcego3 = witch.Witch(False)
        self.morcego3.rect.midbottom = (6880, 380)
        self.morcego4 = witch.Witch(False)
        self.morcego4.rect.midbottom = (7300, 300)

    def setup_callum(self):
        # criando o heroi e posicionando ele na tela
        self.callum = callum2.Callum()
        self.callum.rect.x = self.camera.x + 30
        self.callum.rect.bottom = 493

    def setup_background(self):
        # inserindo o background do cenario
        # definindo o local onde esta o background
        self.background = setup.GFX['Map_jogo_teste']
        # criando um retangulo para o background
        self.back_rect = self.background.get_rect()
        largura = self.back_rect.width
        altura = self.back_rect.height
        self.level = pg.Surface((largura, altura)).convert()
        self.level_rect = self.level.get_rect()
        # fazendo configurações iniciais da camera
        self.camera = setup.TELA.get_rect(bottom=self.level_rect.bottom)
        self.camera.x = 0

    def setup_ground(self):
        # definindo o que será chão
        ground_rect1 = obstaculo.Obstaculo(0, 493, 175, 107)
        ground_rect2 = obstaculo.Obstaculo(172.4, 388, 178, 212)
        ground_rect3 = obstaculo.Obstaculo(172.4, 388, 178, 212)
        ground_rect4 = obstaculo.Obstaculo(491, 385, 104, 222)
        ground_rect5 = obstaculo.Obstaculo(596, 283, 180, 319)
        ground_rect6 = obstaculo.Obstaculo(913, 238, 214, 362)
        ground_rect7 = obstaculo.Obstaculo(1055, 143, 706, 32)
        ground_rect8 = obstaculo.Obstaculo(1055, 143, 33, 90)
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
        ground_rect28 = obstaculo.Obstaculo(6937, 324, 2088, 276)

        # atribuindo todos os objetos num único grupo
        self.group_ground = pg.sprite.Group(ground_rect1, ground_rect2, ground_rect3, ground_rect4,
                                            ground_rect5, ground_rect6, ground_rect7, ground_rect8,
                                            ground_rect9,
                                            ground_rect10, ground_rect11, ground_rect12, ground_rect13,
                                            ground_rect14, ground_rect15, ground_rect16, ground_rect17,
                                            ground_rect18, ground_rect19, ground_rect20, ground_rect21,
                                            ground_rect22, ground_rect23, ground_rect24, ground_rect25,
                                            ground_rect26, ground_rect27, ground_rect28)

    def setup_teto(self):
        # definindo os objetos tetos e onde estão posicionados
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

        # atribuindo os objetos no mesmo grupo
        self.group_teto = pg.sprite.Group(teto_rect1, teto_rect2, teto_rect3, teto_rect4,
                                          teto_rect5, teto_rect6, teto_rect7, teto_rect8,
                                          teto_rect9, teto_rect10, teto_rect11, teto_rect12,
                                          teto_rect13, teto_rect14)

    def setup_agua(self):
        # definindo os objetos água e seu posicionamento
        agua_rect1 = obstaculo.Obstaculo(1547, 566, 354, 34)
        agua_rect2 = obstaculo.Obstaculo(2824, 563, 611, 37)
        agua_rect3 = obstaculo.Obstaculo(5034, 544, 123, 56)
        agua_rect4 = obstaculo.Obstaculo(5356, 544, 250, 56)

        # atribuindo os objetos no mesmo grupo
        self.group_agua = pg.sprite.Group(agua_rect1, agua_rect2, agua_rect3, agua_rect4)

    #### estamos utilizando a gaiola????
    def setup_gaiola(self):
        #
        gaiola_rect1 = obstaculo.Obstaculo(1434, 334, 51, 86)

        self.group_gaiola = pg.sprite.Group(gaiola_rect1)

    def setup_espinhos(self):
        # definindo os objetos espinhos e onde estão posicionados
        espinho_rect1 = obstaculo.Obstaculo(350, 421, 144, 179)
        espinho_rect2 = obstaculo.Obstaculo(771, 565, 140, 35)
        espinho_rect3 = obstaculo.Obstaculo(1123, 317, 73, 28)
        espinho_rect4 = obstaculo.Obstaculo(1334, 283, 76, 26)

        # atribuindo os objetos no mesmo grupo
        self.group_espinho = pg.sprite.Group(espinho_rect1, espinho_rect2, espinho_rect3, espinho_rect4)

    def setup_plataformas(self):
        # definindo os objetos plataforma e onde estão posicionados
        plataforma_rect1 = obstaculo.Obstaculo(1654, 389, 110, 37)
        plataforma_rect2= obstaculo.Obstaculo(2905, 381, 110, 37)
        plataforma_rect3 = obstaculo.Obstaculo(3076, 274, 110, 37)
        plataforma_rect4 = obstaculo.Obstaculo(3258, 486, 110, 37)
        plataforma_rect5 = obstaculo.Obstaculo(5443, 222, 185, 69)
        plataforma_rect6 = obstaculo.Obstaculo(5713, 102, 181, 71)
        plataforma_rect7 = obstaculo.Obstaculo(5943, 265, 186, 75)

        #atribuindo os objetos no mesmo grupo
        self.group_plataforma = pg.sprite.Group(plataforma_rect1, plataforma_rect2, plataforma_rect3, plataforma_rect4,
                                                plataforma_rect5, plataforma_rect6, plataforma_rect7)

    def setup_pedras(self):
        # definindo os objetos pedras e onde estão localizados
        pedra_rect1 = obstaculo.Obstaculo(5800, 28, 94, 95)
        pedra_rect2 = obstaculo.Obstaculo(7686, 228, 155, 372)
        pedra_rect3 = obstaculo.Obstaculo(7755, 192, 87, 408)
        pedra_rect4 = obstaculo.Obstaculo(6478, 339, 195, 261)
        pedra_rect5 = obstaculo.Obstaculo(6532, 314, 56, 286)
        pedra_rect6 = obstaculo.Obstaculo(6605, 322, 47, 278)
        pedra_rect7 = obstaculo.Obstaculo(6426, 370, 41, 230)
        pedra_rect8 = obstaculo.Obstaculo(6664, 373, 34, 227)

        # atribuindo os objetos no mesmo grupo
        self.group_pedra = pg.sprite.Group(pedra_rect1, pedra_rect2, pedra_rect3, pedra_rect4,
                                           pedra_rect5, pedra_rect6, pedra_rect7, pedra_rect8)

    def setup_barraca(self):
        # definindo o objeto barraca e onde está posicionada
        barraca_rect = obstaculo.Obstaculo(8863, 0, 147, 600)

        # criando um grupo para ela
        self.group_barraca = pg.sprite.Group(barraca_rect)

    '''def tela_fim_do_level(self):
        self.imagem = pg.Surface((c.TELA_LARGURA, c.TELA_ALTURA))
        self.imagem.set_alpha(130)
        self.imagem.fill(c.GRAY)'''

# CHECKS

    ### todos os checks dos inimigos são bem parecidos, não daria para criar uma única função?
    def check_witch1_limits(self):
        if self.witch1.rect.left <= 590:
            self.witch1.vel.x = self.witch1.vel.x * (-1)
        if self.witch1.rect.right >= 790:
            self.witch1.vel.x = self.witch1.vel.x * (-1)

        self.adjust_witch1_position()

    def check_witch2_limits(self):
        if self.witch2.rect.left <= 150:
            self.witch2.vel.x = self.witch2.vel.x * (-1)
        if self.witch2.rect.right >= 380:
            self.witch2.vel.x = self.witch2.vel.x * (-1)

        self.adjust_witch2_position()

    def check_witch3_limits(self):
        if self.witch3.rect.left <= 1200:
            self.witch3.vel.x = self.witch3.vel.x * (-1)
        if self.witch3.rect.right >= 1600:
            self.witch3.vel.x = self.witch3.vel.x * (-1)

        self.adjust_witch3_position()
    
    def check_witch4_limits(self):
        if self.witch4.rect.left <= 1280:
            self.witch4.vel.x = self.witch4.vel.x * (-1)
        if self.witch4.rect.right >= 1450:
            self.witch4.vel.x = self.witch4.vel.x * (-1)

        self.adjust_witch4_position()
    
    def check_witch5_limits(self):
        if self.witch5.rect.left <= 2250:
            self.witch5.vel.x = self.witch5.vel.x * (-1)
        if self.witch5.rect.right >= 2695:
            self.witch5.vel.x = self.witch5.vel.x * (-1)

        self.adjust_witch5_position()
    
    def check_witch6_limits(self):
        if self.witch6.rect.left <= 4440:
            self.witch6.vel.x = self.witch6.vel.x * (-1)
        if self.witch6.rect.right >= 4750:
            self.witch6.vel.x = self.witch6.vel.x * (-1)

        self.adjust_witch6_position()
    
    def check_witch7_limits(self):
        if self.witch7.rect.left <= 8100:
            self.witch7.vel.x = self.witch7.vel.x * (-1)
        if self.witch7.rect.right >= 8590:
            self.witch7.vel.x = self.witch7.vel.x * (-1)

        self.adjust_witch7_position()
   
    def check_morcego1_limits(self):
        if self.morcego1.rect.left <= 3700:
            self.morcego1.vel.x = self.morcego1.vel.x * (-1)
        if self.morcego1.rect.right >= 4050:
            self.morcego1.vel.x = self.morcego1.vel.x * (-1)

        self.adjust_morcego1_position()
    
    def check_morcego2_limits(self):
        if self.morcego2.rect.left <= 5200:
            self.morcego2.vel.x = self.morcego2.vel.x * (-1)
        if self.morcego2.rect.right >= 5340:
            self.morcego2.vel.x = self.morcego2.vel.x * (-1)

        self.adjust_morcego2_position()

    def check_morcego3_limits(self):
        if self.morcego3.rect.left <= 6800:
            self.morcego3.vel.x = self.morcego3.vel.x * (-1)
        if self.morcego1.rect.right >= 6930:
            self.morcego3.vel.x = self.morcego3.vel.x * (-1)

        self.adjust_morcego3_position()

    def check_morcego4_limits(self):
        if self.morcego4.rect.left <= 7110:
            self.morcego4.vel.x = self.morcego4.vel.x * (-1)
        if self.morcego4.rect.right >= 7350:
            self.morcego4.vel.x = self.morcego4.vel.x * (-1)

        self.adjust_morcego4_position()
    
    def check_callum_x_collisions(self):
        # checando as colisões do heroi no eixo x
        # fazendo a verificação se o heroi colide com algum dos objetos abaixo
        collider = pg.sprite.spritecollideany(self.callum, self.group_ground)
        teto = pg.sprite.spritecollideany(self.callum, self.group_teto)
        pedras = pg.sprite.spritecollideany(self.callum, self.group_pedra)
        barraca = pg.sprite.spritecollideany(self.callum, self.group_barraca)

        # se houver colisão, deve-se chamar a função para ajustar a posição
        if collider:
            self.adjust_callum_position_for_x_collision(collider)
        elif pedras:
            self.adjust_callum_position_for_x_collision(pedras)
        elif teto:
            self.adjust_callum_position_for_x_collision(teto)
        elif barraca:
            self.adjust_callum_position_for_x_collision(barraca)
            self.callum.vel.x = 0

    def check_callum_y_collisions(self):
        # checando as colisões do heroi no eixo y
        # fazendo a verificação se o heroi colide com algum dos objetos abaixo
        ground = pg.sprite.spritecollideany(self.callum, self.group_ground)
        plataforma = pg.sprite.spritecollideany(self.callum, self.group_plataforma)
        teto = pg.sprite.spritecollideany(self.callum, self.group_teto)
        agua = pg.sprite.spritecollideany(self.callum, self.group_agua)
        espinho = pg.sprite.spritecollideany(self.callum, self.group_espinho)
        pedra = pg.sprite.spritecollideany(self.callum, self.group_pedra)

        # se houver colisão com objetos que não matam, chama a função para ajustar posição
        # caso o objeto "mate" o heroi, chama a função "star_death"
        if ground:
            self.adjust_callum_position_for_y_collision_ground(ground)
        elif plataforma:
            self.adjust_callum_position_for_y_collision_plataforma(plataforma)
        elif teto:
            self.adjust_callum_position_for_y_collision_teto(teto)
        elif pedra:
            self.adjust_callum_position_for_y_collision_ground(pedra)
        elif agua:
            if agua.rect.bottom > self.callum.rect.bottom:
                self.callum.vel.y = 0
                self.callum.rect.bottom = agua.rect.top
                self.callum.star_death(self.game_info)
                #self.callum.number_of_lifes -= 1
        elif espinho:
            if espinho.rect.bottom > self.callum.rect.bottom:
                self.callum.vel.y = 0
                self.callum.rect.bottom = espinho.rect.top
                if self.callum.die_timer == 0:
                    self.callum_damage_sound()
                self.callum.star_death(self.game_info)
                #self.callum.number_of_lifes -= 1
        if ground == None and plataforma == None and pedra == None:
            if self.callum.state != c.JUMP and self.callum.state != c.DEAD :
                self.callum.state = c.FALL

    def check_callum_dead(self):
        # verifica se o heroi está morto
        # estando morto, muda o estado do jogo para c.CALLUM_DEAD, dando fim ao jogo
        if self.callum.number_of_lifes == 0:
            self.game_info[c.CALLUM_DEAD] = True
        if self.callum.rect.y > c.TELA_ALTURA:
            self.game_info[c.CALLUM_DEAD] = True
            self.callum.state = c.DEAD
        if self.game_info[c.CALLUM_DEAD]:
            self.callum.star_death(self.game_info)
            self.end_game()

    #### essa função nao poderia ser mesclada com check_callum_x_collisions?? talvez conserte o bug do game over
    def check_witch_damage(self):
        # verificando se o heroi toma dano dos herois
        hits = pg.sprite.spritecollide(self.callum, self.witch_group, False)

        for hit in hits:
            if hit:
                self.callum.number_of_lifes -= 1
                if self.callum.vel.x >= 0:
                    self.callum.rect.right -= 25
                    self.callum.vel.x = - 5
                    hit.dead = True
                else:
                    self.callum.rect.left += 40
                    self.callum.vel.x = + 5
                self.callum_damage_sound()

    def callum_damage_sound(self):
        # definindo um som para a dano no heroi
        self.pain = pg.mixer.Sound(os.path.join('resources', 'music', 'pain.wav'))
        self.pain.play()

    def check_witch_life(self):
        # verificando se a bruxa ainda está vida, se não, chama a função star_death
        for witch in self.witch_group:
            if witch.dead == True:
                witch.star_death()

    def setup_spritegroups(self):
        # definindo os grupos dos inimigos
        self.witch_group = pg.sprite.Group()
        self.witch_group.add(self.witch1)
        self.witch_group.add(self.witch2)
        self.witch_group.add(self.witch3)
        self.witch_group.add(self.witch4)
        self.witch_group.add(self.witch5)
        self.witch_group.add(self.witch6)
        self.witch_group.add(self.witch7)
        self.witch_group.add(self.morcego1)
        self.witch_group.add(self.morcego2)
        self.witch_group.add(self.morcego3)
        self.witch_group.add(self.morcego4)

        # criando um grupo para todos os personagens
        self.callum_and_enemy_group = pg.sprite.Group(self.callum, self.witch_group)

        # criando um grupo para os poderes
        self.power1_group = pg.sprite.Group()

        # Grupo para o sprite do ovo

        self.egg_group = pg.sprite.Group()

# AJUSTES

    def adjust_sprites_positions(self):
        # chama as funções para ajustar cada sprite na tela
        self.adjust_callum_position()
        self.check_witch_damage()
        self.check_witch_life()
        self.check_witch1_limits()
        self.check_witch2_limits()
        self.check_witch3_limits()
        self.check_witch4_limits()
        self.check_witch5_limits()
        self.check_witch6_limits()
        self.check_witch7_limits()
        self.check_morcego1_limits()
        self.check_morcego2_limits()
        self.check_morcego3_limits()
        self.check_morcego4_limits()
        for power in self.power1_group:
            self.adjust_power1_position(power)

    ### poderia ser feito uma função para ajustar todos os inimigos
    def adjust_witch1_position(self):
        self.last_x_position = self.witch1.rect.right
        self.witch1.rect.x += round(self.witch1.vel.x)
        self.witch1.rect.y += round(self.witch1.vel.y)

    def adjust_witch2_position(self):
        self.last_x_position = self.witch2.rect.right
        self.witch2.rect.x += round(self.witch2.vel.x)
        self.witch2.rect.y += round(self.witch2.vel.y)

    def adjust_witch3_position(self):
        self.last_x_position = self.witch3.rect.right
        self.witch3.rect.x += round(self.witch3.vel.x)
        self.witch3.rect.y += round(self.witch3.vel.y)

    def adjust_witch4_position(self):
        self.last_x_position = self.witch4.rect.right
        self.witch4.rect.x += round(self.witch4.vel.x)
        self.witch4.rect.y += round(self.witch4.vel.y)

    def adjust_witch5_position(self):
        self.last_x_position = self.witch5.rect.right
        self.witch5.rect.x += round(self.witch5.vel.x)
        self.witch5.rect.y += round(self.witch5.vel.y)

    def adjust_witch6_position(self):
        self.last_x_position = self.witch6.rect.right
        self.witch6.rect.x += round(self.witch6.vel.x)
        self.witch6.rect.y += round(self.witch6.vel.y)

    def adjust_witch7_position(self):
        self.last_x_position = self.witch7.rect.right
        self.witch7.rect.x += round(self.witch7.vel.x)
        self.witch7.rect.y += round(self.witch7.vel.y)

    def adjust_morcego1_position(self):
        self.last_x_position = self.morcego1.rect.right
        self.morcego1.rect.x += round(self.morcego1.vel.x)

    def adjust_morcego2_position(self):
        self.last_x_position = self.morcego2.rect.right
        self.morcego2.rect.x += round(self.morcego2.vel.x)

    def adjust_morcego3_position(self):
        self.last_x_position = self.morcego3.rect.right
        self.morcego3.rect.x += round(self.morcego3.vel.x)

    def adjust_morcego4_position(self):
        self.last_x_position = self.morcego4.rect.right
        self.morcego4.rect.x += round(self.morcego4.vel.x)

    def adjust_callum_position(self):
        # ajusta o sprite do callum na tela no eixo X e Y
        self.last_x_position = self.callum.rect.right
        self.callum.rect.x += round(self.callum.vel.x)
        self.check_callum_x_collisions()
        self.callum.rect.y += round(self.callum.vel.y)
        self.check_callum_y_collisions()
        if self.callum.rect.left < 5:
            self.callum.rect.left = 5
        if self.callum.rect.x < (self.camera.x + 5):
            self.callum.rect.x = (self.camera.x + 5)

    def adjust_callum_position_for_x_collision(self, collider):
        # ajusta a posição do heroi no eixo x
        if self.callum.rect.x < collider.rect.x:
            self.callum.rect.right = collider.rect.left
        else:
            self.callum.rect.left = collider.rect.right
            self.callum.vel.x = 0

    def adjust_callum_position_for_y_collision_teto(self, collider):
        # ajusta a posição do heroi no eixo y em relação ao teto
        if self.callum.rect.y > collider.rect.y:
            self.callum.rect.top = collider.rect.bottom
            self.callum.vel.y = 7
            self.callum.state = c.FALL

    def adjust_callum_position_for_y_collision_ground(self, collider):
        # ajusta a posição do heroi no eixo y em relação ao chão
        if collider.rect.bottom > self.callum.rect.bottom:
            self.callum.vel.y = 0
            self.callum.rect.bottom = collider.rect.top
            self.callum.state = c.WALK
        elif collider.rect.top < self.callum.rect.top:
            self.callum.vel.y = 7
            self.callum.rect.top = collider.rect.bottom
            self.callum.state = c.FALL

    def adjust_callum_position_for_y_collision_plataforma(self, collider):
        # ajusta a posição do heroi no eixo y em relação à plataforma
        if collider.rect.y >= self.callum.rect.y:
            self.callum.vel.y = 0
            self.callum.rect.bottom = collider.rect.top
            self.callum.state = c.WALK

    def adjust_power1_position(self,power1):
        # ajustando a posição do poder 1(raio) do heroi(esse poder acompanha o heroi)
        if power1.state == c.FLYING:
            if power1.looking ==c.RIGHT:
                power1.rect.centery = self.callum.rect.centery+13
                power1.rect.x = self.callum.rect.right-2
            else:
                power1.rect.centery = self.callum.rect.centery+15
                power1.rect.right = (self.callum.rect.left+3)

# BLIT

    def blit_tela(self, surface):
        # desenhando na janela apenas a area definida pela camera
        self.level.blit(self.background, self.camera, self.camera)
        # desenhando o heroi e os inimigos na tela
        self.callum_and_enemy_group.draw(self.level)
        # desenhando o poder na tela
        self.power1_group.draw(self.level)
        #### ???????????
        surface.blit(self.level, (0, 0), self.camera)
        # desenhando os "corações" do heroi
        self.show_heart()
        self.show_egg()
        self.show_power1()

    def get_power1_image(self, x, y, width, height):
        # definindo a image do coração
        self.spritesheet_power1 = setup.GFX['poder1']
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.spritesheet_power1, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width / 1.2),
                                    int(rect.height / 1.2)))
        return image

    def show_power1(self):
        # apresentando na tela quantos "poderes 1" o heroi possui
        self.power1_image = self.get_power1_image(383, 211, 55, 32)
        self.power1_image.set_colorkey(c.BLACK)
        self.power1_rect = self.power1_image.get_rect()
        self.power1_rect.x = 0
        self.power1_rect.y = 105
        setup.TELA.blit(self.power1_image, self.power1_rect)

        if self.callum.power1_count > 1:

            self.power1_image2 = self.get_power1_image(383, 211, 55, 32)
            self.power1_image2.set_colorkey(c.BLACK)
            self.power1_rect2 = self.heart_image2.get_rect()
            self.power1_rect2.x = 49
            self.power1_rect2.y = 105
            setup.TELA.blit(self.power1_image2, self.power1_rect2)
        if self.callum.power1_count > 2:
            self.power1_image3 = self.get_power1_image(383, 211, 55, 32)
            self.power1_image3.set_colorkey(c.BLACK)
            self.power1_rect3 = self.power1_image3.get_rect()
            self.power1_rect3.x = 98
            self.power1_rect3.y = 105
            setup.TELA.blit(self.power1_image3, self.power1_rect3)


    def get_heart_image(self, x, y, width, height):
        # definindo a image do coração
        self.spritesheet_heart = setup.GFX['heart']
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.spritesheet_heart, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width * c.SIZE_MULTIPLIER),
                                    int(rect.height * c.SIZE_MULTIPLIER)))
        return image

    def show_heart(self):
        # apresentando na tela quantos "corações" o heroi possui
        self.heart_image = self.get_heart_image(0, 0, 16, 16)
        self.heart_image.set_colorkey(c.BLACK)
        self.heart_rect = self.heart_image.get_rect()
        self.heart_rect.x = 0
        self.heart_rect.y = 0
        setup.TELA.blit(self.heart_image, self.heart_rect)

        if self.callum.number_of_lifes > 1:

            self.heart_image2 = self.get_heart_image(0, 0, 16, 16)
            self.heart_image2.set_colorkey(c.BLACK)
            self.heart_rect2 = self.heart_image2.get_rect()
            self.heart_rect2.x = 49
            self.heart_rect2.y = 0
            setup.TELA.blit(self.heart_image2, self.heart_rect2)
        if self.callum.number_of_lifes > 2:
            self.heart_image3 = self.get_heart_image(0, 0, 16, 16)
            self.heart_image3.set_colorkey(c.BLACK)
            self.heart_rect3 = self.heart_image3.get_rect()
            self.heart_rect3.x = 98
            self.heart_rect3.y = 0
            setup.TELA.blit(self.heart_image3, self.heart_rect3)


    def get_egg_image(self, x, y, width, height):
        # definindo a image do coração
        self.spritesheet_egg = setup.GFX['egg']
        image = pg.Surface((width, height))
        rect = image.get_rect()

        image.blit(self.spritesheet_egg, (0, 0), (x, y, width, height))
        image = pg.transform.scale(image,
                                   (int(rect.width // 3),
                                    int(rect.height // 3)))
        return image
    def show_egg(self):
        # apresentando na tela quantos "corações" o heroi possui

        self.egg_image = self.get_egg_image(68, 52, 120, 165)
        self.egg_image.set_colorkey(c.BLACK)
        self.egg_rect = self.egg_image.get_rect()
        if self.callum.number_of_eggs > 0:
            self.egg_rect.x = 0
            self.egg_rect.y = 50
        else:
            self.egg_rect.midbottom = (300, 388)


        setup.TELA.blit(self.egg_image, self.egg_rect)

# UPDATES

    def update(self, surface, keys, current_time):
        self.game_info[c.CURRENT_TIME] = self.current_time = current_time
        self.update_all_sprites(keys)
        self.blit_tela(surface)

    def update_camera(self):
        third = self.camera.x + self.camera.w // 3
        callum_center = self.callum.rect.centerx
        callum_right = self.callum.rect.right
        #print(self.callum.rect.midbottom)
        if self.callum.vel.x > 0 and callum_center >= third:
            mult = 0.5 if callum_right < self.camera.centerx else 1
            new = self.camera.x + mult * self.callum.vel.x
            highest = self.level_rect.w - self.camera.w
            self.camera.x = min(highest, new)

        if self.callum.vel.x < 0 and self.callum.rect.left < third and self.camera.x > self.camera.w // 3:
            mult = 1
            new = self.camera.x + mult * self.callum.vel.x
            self.camera.x = new

    def update_all_sprites(self, keys):
        self.callum.update(keys, self.game_info, self.power1_group)
        self.witch1.update(self.game_info)
        self.witch2.update(self.game_info)
        self.witch3.update(self.game_info)
        self.witch4.update(self.game_info)
        self.witch5.update(self.game_info)
        self.witch6.update(self.game_info)
        self.witch7.update(self.game_info)
        self.morcego1.update(self.game_info)
        self.morcego2.update(self.game_info)
        self.morcego3.update(self.game_info)
        self.morcego4.update(self.game_info)

        self.egg1.update(self.game_info)

        self.update_number_of_eggs()
        self.show_egg()

        self.adjust_sprites_positions()
        self.check_callum_dead()
        self.update_camera()
    def update_number_of_eggs(self):
        if self.callum.rect.x > 240:
            self.callum.number_of_eggs = 1
    def end_game(self):
        self.next = c.GAME_OVER
        if self.callum.die_timer == 150:
            self.done = True

























