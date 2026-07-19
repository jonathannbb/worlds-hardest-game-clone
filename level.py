import pygame

conf_game = {
    1:{
        "zona_inicio" : (100, 100, 30, 30),
        "meta_final" : (500, 500, 30, 30),
    }
}

class Nivel:
    def __init__(self, numero_nivel):
        datos = conf_game[numero_nivel]
        self.inicio_rect = pygame.Rect(datos["zona_inicio"])
        self.final_rect = pygame.Rect(datos["meta_final"])
    def draw(self, Screen):
        pygame.draw.rect(Screen, (0,255,0), self.inicio_rect)
        pygame.draw.rect(Screen, (0,255,0), self.final_rect)


