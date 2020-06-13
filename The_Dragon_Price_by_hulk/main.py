import pygame as pg
import random
from settings import *
from Sprites import *
from os import path

class Game:
    def __init__(self):
        # initialize game window, etc
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = FONT_NAME
        self.load_data()

        ## SOUNDS
        self.snd_dir = path.join(self.dir, 'snd')





    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'img')
        with open(path.join(self.dir, HS_FILE), 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        self.spritesheet_player = Spritesheet(path.join(img_dir, CALLUM))
        self.spritesheet_heart = Spritesheet(path.join(img_dir, HEART))
        self.spritesheet_egg = Spritesheet(path.join(img_dir, HEART))




    def new(self):
        # start a new game
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self)
        self.all_sprites.add(self.player)

        self.platform_base = Platform_base(0, HEIGHT - 40, 10000, 50)
        #self.all_sprites.add(self.platform_base)

        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        #pg.mixer.music.load(path.join(self.snd_dir, 'happytune.wav'))
        self.run()

    def run(self):
        # Game Loop
        #pg.mixer.music.play(loops=-1)#loop infinito
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        #pg.mixer.music.fadeout(500)
    def update(self):
        # Game Loop - Update

        self.all_sprites.update()

        #Score

        # check if player hits a platform - only if falling
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                lowest = hits[0]
                for hit in hits:
                    if hit.rect.bottom > lowest.rect.bottom:
                        lowest = hit
                if self.player.pos.x < lowest.rect.right + 10 and \
                    self.player.pos.x > lowest.rect.left - 10:
                    if self.player.pos.y < lowest.rect.bottom:
                        self.player.pos.y = hits[0].rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False


        #if self.player.vel.y < 0:
            #hits2 = pg.sprite.spritecollide(self.player, self.platforms, False)
            #if hits2:
              #  self.player.pos.y = hits2[0].rect.bottom + self.player.rect.height
               # self.player.vel.y = 0
        #Scrolling the screen
        if self.player.pos.x >= WIDTH / 4:
            self.player.pos.x -= max(abs(self.player.vel.x), 2)
            for plat in self.platforms:
                plat.rect.x -= int(abs(self.player.vel.x))
                if plat.rect.x + plat.rect.width < 0:
                    plat.kill()
                    #self.score += 1

        #Game over
        if self.player.rect.bottom > HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y -= max(self.player.vel.y, 10)
                if sprite.rect.bottom < 0:
                    sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False


        # Criar plataformas aleatoriamente:
        while len(self.platforms) < 7:
            width = random.randrange(50, 100)
            p = Platform(self, WIDTH,
            random.randrange(HEIGHT / 4, HEIGHT))
            self.platforms.add(p)
            self.all_sprites.add(p)


    def events(self):
        # Game Loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()

            if event.type == pg.KEYUP:
                if event.key == pg.K_UP:
                    self.player.jump_cut()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DOWN:
                    self.player.Crouch()

            if event.type == pg.KEYUP:
                if event.key == pg.K_DOWN:
                    self.player.crouch_cut()

    def draw(self):
        # Game Loop - draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.screen.blit(self.player.image, self.player.rect)
        self.player.show_heart()
        #self.draw_text(str(self.score), 22, WHITE, WIDTH / 2, 20)
        # *after* drawing everything, flip the display
        pg.display.flip()


    def show_start_screen(self):
        # game splash/start screen
        #pg.mixer.music.load(path.join(self.snd_dir, 'yippee.wav'))
        #pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE, 48, WHITE,WIDTH / 2, HEIGHT / 4)
        self.draw_text("Setas pra mover", 22, WHITE, WIDTH / 2, HEIGHT /2)
        self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT*3/4)
        #self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)

        pg.display.flip()
        self.wait_for_key()
        #pg.mixer.music.fadeout(500)

    def show_go_screen(self):
        # game over/continue
        #pg.mixer.music.load(path.join(self.snd_dir, 'yippee.wav'))
        #pg.mixer.music.play(loops=-1)
        if not self.running:
            return
        self.screen.fill(BGCOLOR)
        self.draw_text("Game Over", 48, WHITE, WIDTH / 2, HEIGHT / 4)
        """self.draw_text("Score: " + str(self.score), 22, WHITE, WIDTH / 2, HEIGHT / 2)
        self.draw_text("Press any key to play again", 22, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("New Highscore !!!", 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)
            with open(path.join(self.dir, HS_FILE), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("High Score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 + 40)"""
        pg.display.flip()
        self.wait_for_key()
        #pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x, y):
        pg.font.init()
        font = pg.font.SysFont(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (int(x), int(y))
        self.screen.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()