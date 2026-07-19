import pygame



class Enemigo:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.color = (0,0,255)
        self.speed = 3
    def move(self):
        self.position.x += self.speed
    def update(self):
    # Rebote en los bordes izquierdo o derecho
        if self.position.x >= 730 or self.position.x <= 50:
            self.speed *= -1  # Se devuelve horizontalmente
    
    def draw(self, screen):
         pygame.draw.circle(screen,self.color, self.position, 10)

    
