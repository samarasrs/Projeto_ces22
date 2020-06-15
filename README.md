# Projeto CES22

 Versão do Python : 3.8.0
 Versão do Pygame: 1.9.6
 
 # Equipe

![dragon](https://user-images.githubusercontent.com/63266677/84607056-682cc480-ae81-11ea-8f2c-1129180b2c30.png)

# Componentes

![Captura de tela de 2020-06-14 20-58-08](https://user-images.githubusercontent.com/63266677/84607115-cfe30f80-ae81-11ea-960b-dfe337d492e4.png)

# Descrição do Jogo

![Captura de tela de 2020-06-14 21-10-45](https://user-images.githubusercontent.com/63266677/84607426-90b5be00-ae83-11ea-8e5e-780fede5cc73.png)

# Menu Principal

![Captura de tela de 2020-06-14 21-04-42](https://user-images.githubusercontent.com/63266677/84607288-d45bf800-ae82-11ea-94ca-144992f884d2.png)


![Captura de tela de 2020-06-14 21-05-19](https://user-images.githubusercontent.com/63266677/84607315-f9506b00-ae82-11ea-9f38-1d8599245054.png)


![Captura de tela de 2020-06-14 21-05-38](https://user-images.githubusercontent.com/63266677/84607353-2ef55400-ae83-11ea-952b-86c9a7d3e23e.png)

# Level 1

O level 1 é composto por duas partes, a primeira dentro do castelo e a segunda na floresta. Na figura a seguir é possível observar essa mudança e também visualizar os dois inimigos existentes no jogo.

![Captura de tela de 2020-06-14 21-15-49](https://user-images.githubusercontent.com/63266677/84607581-73352400-ae84-11ea-8fd4-5e8b5f345714.png)

Para maiores informações sobre a dinâmica do jogo assista o vídeo de apresentação do jogo: https://youtu.be/-N34N35UX6I

# Organização do Código

## Arquivo Dragon_Prince_level1

É o arquivo que inicializa o jogo.

## Pasta Data

Possui os arquivos das classes que compõe o jogo.

### Constants

Arquivo das constantes do jogo, como as cores, nomes de variáveis e posição de objetos.

#### game_sound

Possui a classe Sound que controla a execução de música durante a partida.

#### main

A função principal do jogo, onde é definido o dicionário de estados.

#### setup

Arquivo com as configurações de tela e lista de fontes, músicas, sons e figuras.

#### tools

Possui as classes State e Control. A classe State é a classe do estado do jogo e a classe Control é responsável pelas trocas de estados e looping do jogo. Este arquivo possui também as funções que carregam as fontes, músicas, sons e figuras.

#### components

É a pasta que possui os arquivos das classes dos elementos que compoe o jogo como, callum2 (personagem), egg, obstaculos (define os retângulos para colisão), powercallum e witch.

#### states

É a pasta dos estados possivéis do jogo, esqueceu (a tela de game over quando o player esquece de pegar o ovov), game_over (tela de game over quando acabam as vidas ou o player cai na água ou espinhos), level (classe onde é definida toda a dinâmica do level), main_menu (a tela de menu, ajuda e créditos) e vc_venceu (a tela de vitória).

## Pasta Resources

Contém todos as fontes, músicas, sons e figuras separadas por subpastas.
