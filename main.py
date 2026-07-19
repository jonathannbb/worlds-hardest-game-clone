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
SPAWNS_POR_NIVEL = {
    1: (105, 105),
    2: (125, 125),
    3: (400, 300),
    4: (50, 500)
}
nivel_actual = 1
spawn_x, spawn_y = SPAWNS_POR_NIVEL[nivel_actual]
player = Jugador(spawn_x, spawn_y)

#limite aplicado a cada nivel.
limitScreen = screen.get_rect()

zona_permitida = pygame.Rect(40, 40, 700, 500)



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
                
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_r:
                player.rect.topleft = SPAWNS_POR_NIVEL[nivel_actual]



    #Coordenadas del jugador, por ahora con el objetivo de saber donde esta ubicado el jugador
    #y asi plantear los niveles con mayor facilidad
    pygame.display.set_caption(f"Posición Jugador -> X: {player.rect.x} | Y: {player.rect.y}")
    
    player.Move()
    player.rect.clamp_ip(limitScreen)
    screen.fill(blanco)


    
    pygame.draw.line(screen, (0,0,0), (40,40), (740,40), 5)
    pygame.draw.line(screen, (0,0,0), (40,540), (40,38), 5)
    pygame.draw.line(screen, (0,0,0), (38,540), (740,540), 5)
    pygame.draw.line(screen, (0,0,0), (740,542), (740,38), 5)
    player.rect.clamp_ip(zona_permitida)
    

    obstacle.draw(screen)
    player.Draw(screen)

    pygame.display.flip()
    clock.tick(60)

# 5. Salir de Pygame de forma segura
pygame.quit()