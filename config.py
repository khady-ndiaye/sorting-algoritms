import pygame
pygame.init()
# Paramètres de l'écran
WIDTH, HEIGHT = 600, 600
FPS = 60

# Couleurs
WHITE = (255, 255, 255)
BACKGROUND_COLOR = (30, 30, 30)
BUTTON_COLOR = (100, 100, 250)
BUTTON_HOVER_COLOR = (150, 150, 255)
TEXT_COLOR = (255, 255, 255)
TEXT_BG_COLOR = (0, 0, 0)

# Police pour les boutons
font = pygame.font.SysFont("Arial", 24)
large_font = pygame.font.SysFont("Arial", 36)