import pygame
from player import Jugador
from level import Nivel

#Iniciar Pygame
pygame.init()

#Configurar el tamaño de la ventana y color
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
blanco = (255,255,255)

#variable para aplicar el cambio de nivel
nivel_actual = 1
#objeto que instacia el nivel(escenario)
level = Nivel(nivel_actual)

#posicion inicial del jugador
spawn_x, spawn_y = level.spawn
player = Jugador(spawn_x, spawn_y)

#limite aplicado a cada nivel.
zona_permitida = pygame.Rect(43, 43, 695, 495)

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
                player.rect.topleft = level.spawn

    #Coordenadas del jugador, por ahora con el objetivo de saber donde esta ubicado el jugador
    #y asi plantear los niveles con mayor facilidad
    pygame.display.set_caption(f"Posición Jugador -> X: {player.rect.x} | Y: {player.rect.y}")

    #movimientos del jugador
    player.Move()
    
    #color a la pantalla
    screen.fill(blanco)
    
    # Si el jugador toca la hitbox del enemigo, vuelve al spawn del nivel actual.
    for enemigo in level.enemigos:
        if player.rect.colliderect(enemigo.rect):
            player.rect.topleft = level.spawn
            break
        
    #verificar si el jugador paso de nivel
    if player.rect.colliderect(level.final_rect):
        nivel_actual += 1
        level = Nivel(nivel_actual)
        spawn_x, spawn_y = level.spawn
        player.rect.x = spawn_x
        player.rect.y = spawn_y

    # Actualizar todos los enemigos del nivel actual.
    for enemigo in level.enemigos:
        enemigo.update(level.paredes)
    
    #aplicando colision al jugador
    player.update(level.paredes)

    #aplicando limite para el cuadrado rojo
    player.rect.clamp_ip(zona_permitida)

    #dibujar en pantalla 
    level.draw(screen)
    player.Draw(screen)

    pygame.display.flip()
    clock.tick(60)

#Salir de Pygame de forma segura
pygame.quit()
