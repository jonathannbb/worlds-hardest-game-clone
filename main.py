import pygame
from player import Jugador
from level import Nivel
from enemys import Enemigo

#Iniciar Pygame
pygame.init()


#Configurar el tamaño de la ventana y color
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
blanco = (255,255,255)

#posicion inicial del jugador, enemigo y que ambos no sobrepasen el limite de la ventana
SPAWNS_POR_NIVEL = {
    1: (105, 105),
    2: (125, 125),
    3: (400, 300),
    4: (50, 500)
}
nivel_actual = 1
spawn_x, spawn_y = SPAWNS_POR_NIVEL[nivel_actual]
player = Jugador(spawn_x, spawn_y)
enemigo = Enemigo(375, 265)

#limite aplicado a cada nivel.
zona_permitida = pygame.Rect(43, 43, 695, 495)

#objeto que instacia el nivel (escenario)
level = Nivel(nivel_actual)

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
    
    #movimientos del jugador y enemigos
    player.Move()
    enemigo.move()
    
    #color a la pantalla
    screen.fill(blanco)

    #aplicando limite para el cuadrado rojo
    player.rect.clamp_ip(zona_permitida)
    
    #dibujar en pantalla
    level.draw(screen)
    player.Draw(screen)
    enemigo.draw(screen)

    #aplicando colision al enemigo
    enemigo.update()

    pygame.display.flip()
    clock.tick(60)

#Salir de Pygame de forma segura
pygame.quit()