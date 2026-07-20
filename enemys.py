import pygame


class Enemigo:
    def __init__(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.radio = 10
        self.rect = pygame.Rect(x - self.radio, y - self.radio,
                                self.radio * 2, self.radio * 2)
        self.color = (0,0,255)
        self.speed = 3

    def move(self):
        self.position.x += self.speed
        self.rect.center = self.position

    def update(self, paredes):
        # Rebote en los bordes izquierdo o derecho
        if self.position.x >= 730 or self.position.x <= 50:
            self.speed *= -1
        for pared in paredes:
            if not self.rect.colliderect(pared):
                continue

            # El enemigo sólo se mueve en el eje X, por lo que el rebote se
            # resuelve contra el lado horizontal de la pared que acaba de tocar.
            if self.speed > 0:
                self.rect.right = pared.left
            else:
                self.rect.left = pared.right

            self.position.x = self.rect.centerx
            self.speed *= -1
            break
    def draw(self, screen):
         pygame.draw.circle(screen, self.color, self.position, self.radio)

    
