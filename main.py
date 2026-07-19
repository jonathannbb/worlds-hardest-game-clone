import pygame
from player import Jugador
from level import Nivel

#Iniciar Pygame
pygame.init()


#Configurar el tamaño de la ventana y color
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
blanco = (255,255,255)

#posicion inicial del jugador, y que el objeto no sobrepase el limite de la ventana
poscision_inicial_jugador = [Jugador(105,105), Jugador(125,125)]
player = poscision_inicial_jugador[0]
limitScreen = screen.get_rect()

#objeto que instacia el nivel (escenario)
obstacle = Nivel(1)

#Bucle principal para que la ventana no se cierre sola con los diversos elementos del juego
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jugando = False
    
    #Coordenadas del jugador, por ahora con el objetivo de saber donde esta ubicado el jugador
    #y asi plantear los niveles con mayor facilidad
    pygame.display.set_caption(f"Posición Jugador -> X: {player.rect.x} | Y: {player.rect.y}")

    player.Move()
    player.rect.clamp_ip(limitScreen)
    screen.fill(blanco)
    obstacle.draw(screen)
    player.Draw(screen)
    
    pygame.display.flip()
    clock.tick(60)

# 5. Salir de Pygame de forma segura
pygame.quit()