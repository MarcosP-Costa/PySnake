import pygame
import random

pygame.init() #Inicia o PyGame
pygame.display.set_caption("PySnake")#Nome do Programa
largura, altura = 1200, 800#Tamanho da Janela
tela = pygame.display.set_mode((largura, altura))#Abrir Programa
relogio = pygame.time.Clock()


#cores RGB
preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)
verde = (0, 255, 0)
azul = (0, 0, 255)

#parametros da cobrinha
tamanho_quadrado = 20


#poderes
poderes = [
    {
        "nome": "lentidão",
        "buff": -5,
        "cor": verde
    },
    {
        "nome": "Eu sou a VELOCIDADE(catchau)",
        "buff": 10,
        "cor": vermelho
    }
]



def gerar_comida():
    comida_x = round(random.randrange(0, largura-tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    comida_y = round(random.randrange(0, round(altura/3)) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return comida_x, comida_y

def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, azul, [comida_x, comida_y, tamanho, tamanho])
    
def gerar_poder():
    poder_x = round(random.randrange(0, largura-tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    poder_y = round(random.randrange(0, altura-tamanho_quadrado) / float(tamanho_quadrado)) * float(tamanho_quadrado)
    return poder_x, poder_y

def desenhar_poder(tamanho, poder_x, poder_y, cor):
    pygame.draw.rect(tela, cor, [poder_x, poder_y, tamanho, tamanho])
    
def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, branco, [pixel[0], pixel[1], tamanho, tamanho])

def desenhar_pontuacao(pontuacao, velocidade):
    fonte = pygame.font.SysFont("Helvatica", 35)
    texto_pontuacao = fonte.render(f"Pontos: {pontuacao}", False, azul)
    texto_velocidade = fonte.render(f"Velocidade: {velocidade}", True, verde)
    tela.blit(texto_pontuacao, [1, 1])
    tela.blit(texto_velocidade, [1, 25])
    
def recadoInicial():
    fonte1 = pygame.font.SysFont("Comic Sans", 40)
    fonte2 = pygame.font.SysFont("Comic Sans", 25)
    textoInicial = fonte1.render("Para Jogar, é só clicar em uma das setas", True, branco)
    textoComplementar = fonte2.render("O Quadrado Azul te da pontos, o quadrado verde diminui sua velocidade, e o vermelho aumenta!", True, branco)
    tela.blit(textoInicial, [largura/6, altura/2])
    tela.blit(textoComplementar, [90, altura/3])


def selecionar_velocidade(tecla, x, y):
    if tecla == pygame.K_DOWN and y != -tamanho_quadrado:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
        print("Baixo")
    elif tecla == pygame.K_UP and y != tamanho_quadrado:
        velocidade_x = 0
        velocidade_y = -tamanho_quadrado
        print("Cima")
    elif tecla == pygame.K_RIGHT and x != -tamanho_quadrado:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
        print("Direita")
    elif tecla == pygame.K_LEFT and x != tamanho_quadrado:
        velocidade_x = -tamanho_quadrado
        velocidade_y = 0   
        print("Esquerda")
    else:
        
        velocidade_x = x
        velocidade_y = y    
    return velocidade_x, velocidade_y



def rodar_jogo():
    

    fim_jogo = False
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_jogo = 1
    pixels = []
    
    velocidade_jogo = 20
    
    comida_x, comida_y = gerar_comida()
    poder_x, poder_y = gerar_poder()
    poder = random.randrange(0, len(poderes))
    
    while not fim_jogo:
        tela.fill(preto)
        
        if(tamanho_jogo == 1):
            recadoInicial()
        
        
        for evento in pygame.event.get():  #Todo evento do usuario é registrado aqui, seja clicar, mover seta, etc
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key, velocidade_x, velocidade_y)


        #desenhar_comida
        desenhar_poder(tamanho_quadrado, poder_x, poder_y, poderes[poder]["cor"] )
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
       
        #desenhando Poder
        
       
        #atualizar a posicao da cobra
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        x += velocidade_x
        y += velocidade_y
        #desenhar_cobra
        pixels.append([x, y])
        if len(pixels) > tamanho_jogo:
            del pixels[0]
            
        for pixel in pixels[:-1]:
            if pixel == [x, y]:#pixels é o corpo da cobrinha, aqui checamos se a cabeça dela esta no mesmo lugar que o corpo
                fim_jogo = True
        desenhar_cobra(tamanho_quadrado, pixels)
        desenhar_pontuacao(tamanho_jogo - 1, velocidade_jogo)
        
        
                
        # atualização de tela
        pygame.display.update()
        
        if x == comida_x and y == comida_y:
            tamanho_jogo  += 1
            velocidade_jogo += 1
            comida_x, comida_y = gerar_comida()
            
            
        if x == poder_x and y == poder_y:
            if(velocidade_jogo <= 5 and poderes[poder]["buff"] <= 0):
                velocidade_jogo = 1
            else:
                velocidade_jogo += poderes[poder]["buff"]
            poder = random.randrange(0, len(poderes))
            poder_x, poder_y = gerar_poder()
        
        
        relogio.tick(velocidade_jogo)
#criar um loop infinito

#desenhar os objetos do jogo na tela
#pontuação
#cobrinha
#comida



rodar_jogo()