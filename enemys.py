import pygame


class Enemigo:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.radio = 10
        self.rect = pygame.Rect(x - self.radio, y - self.radio,
                                self.radio * 2, self.radio * 2)
        self.color = (0,0,255)
        self.speed = 3
        self.direction_x = self.speed
        self.direction_y = self.speed

    def update(self, paredes):
        self.position.x += self.direction_x
        self.rect.centerx = round(self.position.x)
        # Rebote en los bordes izquierdo o derecho
        if self.position.x >= 730 or self.position.x <= 50:
            self.direction_x *= -1
        for pared in paredes:
            if self.rect.colliderect(pared):
                if self.direction_x > 0:  # Choca contra la izquierda de la pared
                    self.rect.right = pared.left
                elif self.direction_x < 0:  # Choca contra la derecha de la pared
                    self.rect.left = pared.right
                
                #rebote: Invertimos solo el eje x
                self.position.x = self.rect.centerx
                self.direction_x *= -1

    def draw(self, screen):
         pygame.draw.circle(screen, self.color, self.position, self.radio)

    
