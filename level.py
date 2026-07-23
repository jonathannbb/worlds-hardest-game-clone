import pygame
from enemys import Enemigo

conf_game = {
    1:{
        "zona_inicio" : (69, 134, 125, 300),
        "meta_final" : (580, 134, 125, 300),
        "zona_spawn" : (122,275),
        "paredes" : [(65, 130, 125, 4),   # Pared superior
            (65, 430, 185, 4),   # Pared inferior
            (65, 130, 4, 300), #pared izquierda
            (190, 130, 4, 270), # pared derecha
            (250, 400, 4, 34),
            (250, 400, 300, 4),
            (546, 170, 4, 230),
            (546,170, 34, 4),
            (576, 170, 4, 260),
            (576, 430, 130, 4),
            (705, 134,4, 300),
            (515, 130, 194, 4),
            (515, 130, 4, 44),
            (220,170, 295, 4),
            (220, 170, 4, 230),
            (190,400, 34, 4)], 
        "enemigos" :[(235,375, 5), (532,335, 5), (235,295, 5), (532,255, 5), (235,215, 5), (532,185, 5)],
        "modo_movimiento" : (1)
    },
    2:{
        "zona_inicio" : (400, 400, 30, 30),
        "meta_final" : (100, 100, 60, 60),
        "zona_spawn" : (405,405),
        "paredes" : [(150, 200, 500, 20),   # Pared superior
        (150, 380, 500, 20),   # Pared inferior
        (150, 220, 20, 160),],
        "enemigos" : [(500,400, 5)],
        "modo_movimiento" : (2)
    }

}

class Nivel:
    def __init__(self, numero_nivel):
        datos = conf_game[numero_nivel]
        self.inicio_rect = pygame.Rect(datos["zona_inicio"])
        self.final_rect = pygame.Rect(datos["meta_final"])
        self.spawn = datos["zona_spawn"]
        self.paredes = []
        for p in datos["paredes"]:
            self.paredes.append(pygame.Rect(p))

        self.enemigos = [] #Enemigo (100,100), Enemigo(200,200)
        for pos in datos["enemigos"]:
            nuevo_enemigo = Enemigo(*pos)
            self.enemigos.append(nuevo_enemigo)

        self.movimiento = datos["modo_movimiento"]

    def draw(self, Screen):

        #ventana principal para cada nivel
        pygame.draw.line(Screen, (0,0,0), (40,40), (740,40), 5)
        pygame.draw.line(Screen, (0,0,0), (40,540), (40,38), 5)
        pygame.draw.line(Screen, (0,0,0), (38,540), (740,540), 5)
        pygame.draw.line(Screen, (0,0,0), (740,542), (740,38), 5)
        
        #punto de partida y punto final.
        pygame.draw.rect(Screen, (0,255,0), self.inicio_rect)
        pygame.draw.rect(Screen, (0,255,0), self.final_rect)
        #paredes
        for pared in self.paredes:
            pygame.draw.rect(Screen, (0,0,0), pared)
        #enemigos
        for enemigo in self.enemigos:
            enemigo.draw(Screen)




        



