#definindo a altura e largura da tela
TELA_ALTURA= 600
TELA_LARGURA = 800

TELA_TAMANHO = (TELA_LARGURA, TELA_ALTURA)

# definindo titulo
TITULO = "The Dragon Prince "

# definir as cores em RGB
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GRAY = (100, 100, 100)
NAVYBLUE     = ( 60,  60, 100)
GREEN        = (  0, 255,   0)
FOREST_GREEN = ( 31, 162,  35)
BLUE         = (  0,   0, 255)
SKY_BLUE     = ( 39, 145, 251)
YELLOW       = (255, 255,   0)
ORANGE       = (255, 128,   0)
PURPLE       = (255,   0, 255)
CYAN         = (  0, 255, 255)
BLACK        = (  0,   0,   0)
NEAR_BLACK    = ( 19,  15,  48)
COMBLUE      = (233, 232, 255)
GOLD         = (255, 215,   0)

# Callum
SIZE_MULTIPLIER = 3

# POWER

SIZE_MULTIPLIER_POWER = 0.5
POWER1 = 'poder1'
POWER2 = 'poder2'
FLYING = 'voando'
EXPLODING = 'explodindo'



#looking

RIGHT = 'right'
LEFT = 'left'

#estados Callum
STAND = 'standing'
WALK = 'walk'
JUMP = 'jump'
FALL = 'fall'
DEAD = 'dead'
LIFES = 3


# Fisica
# Player properties
WALK_ACCEL = .15
RUN_ACCEL = 20
SMALL_TURNAROUND = .35

GRAVITY = 1.01
JUMP_GRAVITY = .31
JUMP_VEL = -10
FAST_JUMP_VEL = -12.5
MAX_Y_VEL = 11

MAX_RUN_SPEED = 800
MAX_WALK_SPEED = 6


# MENU
# posição das imagens e textos no Menu
POS_TITULO = [85,10]
POS_BOTAO_PERM_TELA1 = [280,220]
POS_BOTAO_JOGAR = [410, 230]
POS_BOTAO_AJUDA = [230, 310]
POS_BOTAO_CREDITO = [410,310]
POS_BOTAO_VOLTAR = [10, 530]
POS_BOTAO_PERM = [50, 440]
POS_BOTAO_SIM = [230, 400]
POS_BOTAO_NAO = [410, 400]
POS_BOTAO_PERM2 = [365, 310]
POS_BACKGROUND = [-110,0]
POS_TEXT_JOGAR = [445, 235]
POS_TEXT_AJUDA = [260, 315]
POS_TEXT_CREDITO = [425, 315]
POS_TEXT_VOLTAR = [42, 535]
POS_TEXT_TIT_TELA2 = [305,10]
POS_TEXT_TIT_TELA3 = [250,10]
POS_TEXT_BOTAO_PERM1 = [42, 305]
POS_TEXT_BOTAO_PERM2 = [42, 318]
POS_TEXT_BOTAO_PERM1_TELA1 = [247, 175]
POS_TEXT_BOTAO_PERM2_TELA1 = [247, 188]
POS_TEXT_GAME_OVER = [190, 150]
POS_TEXT_DESEJA = [220, 250]
POS_TEXT_SIM = [285, 405]
POS_TEXT_NAO = [465, 405]

# tamanho dos Botoes
BOTOES_TAMANHO = (160, 50)
BOTAO_PERM_TAMANHO = (70, 70) #botao redondo

# textos Menu
TEXT_JOGAR = 'Jogar'
TEXT_AJUDA = 'Ajuda'
TEXT_TELA2 = 'Ajuda'
TEXT_TELA3 = 'Créditos'
TEXT_CREDITO = 'Créditos'
TEXT_BOTAO_VOLTAR = 'Voltar'
TEXT_BOTAO_PERM1 = 'Permanecer'
TEXT_BOTAO_PERM2 = 'nesta tela'
TEXT_GAME_OVER = 'GAME OVER'
TEXT_DESEJA = 'Deseja jogar novamente?'
TEXT_SIM = 'SIM'
TEXT_NAO = 'NÃO'

# fonts Menu
FONT_TITULO='DragonForcE'
FONT_BOTOES= 'JMH_Typewriter'

# tamanho da Fonte
FONT_TITULO_TAMANHO = 110
FONT_BOTOES_TAMANHO = 30
FONT_BOTAO_PERM = 12

# estados do cursor
BOTAO0= 'bot 0'
BOTAO_JOGAR= 'bot 1'
BOTAO_AJUDA= 'bot 2'
BOTAO_CREDITOS= 'bot 3'
BOTAO_VOLTA= 'bot 4'
BOTAO_SIM = 'bot 1'
BOTAO_NAO = 'bot 2'


# Estados do jogo (state_dict)
MAIN_MENU = 'main menu'
LOAD_SCREEN = 'load screen'
TIME_OUT = 'time out'
GAME_OVER = 'game over'
LEVEL1 = 'level1'
FOREST = 'floresta'
CASTLE = 'castelo'

# telas do Menu
TELA1 = 'Menu'
TELA2 = 'Ajuda'
TELA3 = 'Creditos'

# Informação Level1


SCORE = 'score'
VIDAS = 'lives'
CURRENT_TIME = 'current time'
LEVEL_STATE = 'level state'
CAMERA_INICIAL_X = 'camera start x'
CALLUM_DEAD = 'dead'
PODER_1 = 'poder 1'
PODER_2 = 'poder 2'
EGG = 'egg'
