import pygame

class Jugador:
    def __init__ (self, x, y):
        #self.velocidad = 
        
        self.rect = pygame.Rect(x, y, 20,20)
        self.color = (255,0,0)
        self.speed = 2
    def Move(self):
        self.direction_x = 0
        self.direction_y = 0

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.direction_x = -self.speed
        if teclas[pygame.K_RIGHT]:
            self.direction_x = self.speed   
        if teclas[pygame.K_UP]:
            self.direction_y = -self.speed
        if teclas[pygame.K_DOWN]:
            self.direction_y = self.speed
    def update(self, paredes):

        #movimiento y colision eje x
        self.rect.x += self.direction_x
        for pared in paredes:
            if self.rect.colliderect(pared):
                if self.direction_x > 0:  # Moviéndose a la derecha
                    self.rect.right = pared.left
                    
                elif self.direction_x < 0:  # Moviéndose a la izquierda
                    self.rect.left = pared.right
                
        
        #movimiento y colision eje y
        self.rect.y += self.direction_y
        for pared in paredes:
            if self.rect.colliderect(pared):
                if (self.direction_y > 0):  # Moviéndose a la derecha
                    self.rect.bottom = pared.top
                    
                elif self.direction_y < 0:  # Moviéndose a la izquierda
                    self.rect.top = pared.bottom
                
                

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
