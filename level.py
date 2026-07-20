import pygame

conf_game = {
    1:{
        "zona_inicio" : (100, 100, 30, 30),
        "meta_final" : (605, 445, 60, 60),
        "zona_spawn" : (105,105)
    },
    2:{
        "zona_inicio" : (400, 400, 30, 30),
        "meta_final" : (100, 100, 60, 60),
        "zona_spawn" : (405,405)
    }

}

class Nivel:
    def __init__(self, numero_nivel):
        datos = conf_game[numero_nivel]
        self.inicio_rect = pygame.Rect(datos["zona_inicio"])
        self.final_rect = pygame.Rect(datos["meta_final"])
        self.spawn = datos["zona_spawn"]
    def draw(self, Screen):

        #ventana principal para cada nivel
        pygame.draw.line(Screen, (0,0,0), (40,40), (740,40), 5)
        pygame.draw.line(Screen, (0,0,0), (40,540), (40,38), 5)
        pygame.draw.line(Screen, (0,0,0), (38,540), (740,540), 5)
        pygame.draw.line(Screen, (0,0,0), (740,542), (740,38), 5)
        
        #punto de partida y punto final.
        pygame.draw.rect(Screen, (0,255,0), self.inicio_rect)
        pygame.draw.rect(Screen, (0,255,0), self.final_rect)


