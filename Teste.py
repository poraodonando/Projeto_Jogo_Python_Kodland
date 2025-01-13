# Escreva o seu código aqui :-)

import pgzrun
import random
from pgzhelper import *

# Dimensões da Janela (em pixels)

WIDTH = 800
HEIGHT = 600

#Cores
black = (0,0,0)
brown = (71,34,18)
red = (255,0,0)
white = (255,255,255)

#Lua

lua = Actor('lua')
lua.x = 700 # posicao x da lua
lua.y = 80
#lua.scale = 0.5 # diminui o tamanho da lua

#casa fantasma

casa_fantasma = Actor('casa_fantasma_4_')
casa_fantasma.x = 400
casa_fantasma.y = 300

#morcego
morcego = Actor('bat-frames/bat-1')
morcego.scale = 1.3
morcego.x = 900
morcego.y = 100
morcego.images = ['bat-frames/bat-1','bat-frames/bat-2', 'bat-frames/bat-3',
                'bat-frames/bat-4', 'bat-frames/bat-5']
morcego.fps = 10


# ZUMBI
zumbi = Actor('zumbis-frames/walk_1')

zumbi.x = 100
zumbi.y = 470
zumbi.fps = 15
zumbi.images = ['zumbis-frames/walk_1','zumbis-frames/walk_2', 'zumbis-frames/walk_3',
'zumbis-frames/walk_4','zumbis-frames/walk_5', 'zumbis-frames/walk_6','zumbis-frames/walk_7',
'zumbis-frames/walk_8','zumbis-frames/walk_9','zumbis-frames/walk_10']

# outra forma de colocar as imagens:
    #zumbi.images = []
    #for i in range(1,11):
    #    zumbi.images.append(f'zumbis-frames/walk_{i}')

zumbi.scale = 0.2

velocidade = 0 # velocidade que o zumbi se move quando nas direções cima/baixo
gravidade = 1 # A gravidade vai mudar a velocidade


#Criação dos fantasmas

fantasma = Actor('fantasma/fantasma_1')
fantasma.x = random.randint(900,5000)
fantasma.y = random.randint(250,350)
fantasma.scale = 0.2
fantasma.flip_x = True
fantasma.fps = 5
fantasma.images = ['fantasma/fantasma_1', 'fantasma/fantasma_2','fantasma/fantasma_3',
                    'fantasma/fantasma_4','fantasma/fantasma_5','fantasma/fantasma_6',
                    'fantasma/fantasma_7']


#OBSTÁCULOS



# Criação de variaveis de JOgos

score = 0

####################
####################
####################
####################


def update():
    global velocidade, score

    #ANIMAÇÃO DO MORCEGO

    morcego.animate()
    morcego.x -= 5
    if morcego.x <  -50:
        morcego.x = random.randint(1000, 15000)
        morcego.y = random.randint(100,250)

    morcego.flip_x = True #coloca o morcego do lado certo


#ANIMAÇÃO DO ZUMBI
    zumbi.scale = 0.2 # deixa  o scale na função update,o zumbi fica na escala menor
    zumbi.animate()
    #zumbi.next_image() # deixa ele correndo

# PULAR QUANDO A SETA PARA CIMA FOR PRESSIONADA
    if keyboard.up and zumbi.y == 470: # verifica se a tecla foi pressionada e se o zumbi estpa no chao
        velocidade = -18
    zumbi.y += velocidade

    velocidade += gravidade;

# para o zumbi no chão
    if zumbi.y > 470:
        velocidade = 0
        zumbi.y = 470



#coloca fantasma na cena

    fantasma.animate()
    fantasma.x -=5 # move o fantasma pela cena
    fantasma.scale = 0.2
    if fantasma.x < -50: #quando chega no final da tela volta para uma posição aleatoria
        fantasma.x =  random.randint(900,5000)
        fantasma.y = random.randint(200,350)


## Quando o zumbi colide com o fantasma

    if zumbi.colliderect(fantasma):
        sounds.splat.play() # som.nome_arquido_ação()
        #reseta a posição do fantasma
        fantasma.x =  random.randint(900,5000)
        fantasma.y = random.randint(200,350)
        score += 5

    #ESPINHOS
    # cada timeout de frames serão atualizados no jogo adicionando 1 no contador


    # move o espinho pela cena

def draw():
    screen.draw.filled_rect(Rect(0, 0, 800, 500),(black)) #céu
    screen.draw.filled_rect(Rect(0, 500, 800, 600), (brown)) #Solo

    lua.draw()
    casa_fantasma.draw() #desenha as casas na tela
    morcego.draw() #desenha o  morcego na tela
    zumbi.draw() #desenha o  zumbi na tela
    fantasma.draw()

    screen.draw.text('Score: ' + str(score),(20,20),color = (red),fontname='creepster',
            fontsize = 30)
    # Se tiver nenhum espinho atualmente no cenario, desenhe-os



