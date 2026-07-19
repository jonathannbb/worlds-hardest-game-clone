import pygame

class Jugador:
    def __init__ (self, x, y):
        self.rect = pygame.Rect(x, y, 20,20)
        self.color = (255,0,0)
        self.speed = 5
    def Move(self):
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]: 
            self.rect.x -= self.speed
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if teclas[pygame.K_UP]:
            self.rect.y -= self.speed
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.speed

    def Draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
