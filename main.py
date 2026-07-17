import pygame
from player import Jugador
from level import Nivel

# 1. Iniciar Pygame
pygame.init()


# 2. Configurar el tamaño de la ventana (ancho, alto en píxeles y color de pantalla)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
blanco = (255,255,255)
player = Jugador(100,100)
limitScreen = screen.get_rect()


obstacle = Nivel(1)




# 3. Ponerle un título a la ventana
pygame.display.set_caption("Mi Ventana Principal")

# 4. Bucle principal para que la ventana no se cierre sola
jugando = True
while jugando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_ESCAPE:
                jugando = False
    
    
    player.Move()
    player.rect.clamp_ip(limitScreen)
    screen.fill(blanco)
    obstacle.draw(screen)
    player.Draw(screen)
    



    
    
    pygame.display.flip()
    clock.tick(60)

# 5. Salir de Pygame de forma segura
pygame.quit()