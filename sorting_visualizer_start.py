import pygame
import random
import time
from sorting_algorithms import SortingAlgorithms
import tracemalloc

WIDTH, HEIGHT = 800, 600
BAR_WIDTH = 5
BAR_COLOR = (0, 102, 204)
BG_COLOR = (255, 255, 255)
SELECTED_COLOR = (255, 0, 0)
BUTTON_COLOR = (200, 200, 200)
BUTTON_HOVER_COLOR = (150, 150, 150)
TEXT_COLOR = (0, 0, 0)

class SortVisualizer:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Tri Visuel")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 20)
        self.large_font = pygame.font.SysFont("Arial", 36)
        self.background_image = pygame.image.load("C:/Users/ndiay/Desktop/lptf/projets/sorting-algorithms/images/ALGO.jpeg")
        self.background_image = pygame.transform.scale(self.background_image, (WIDTH, HEIGHT))

        self.algorithms = [
            SortingAlgorithms.selection_sort,
            SortingAlgorithms.bubble_sort,
            SortingAlgorithms.insertion_sort,
            SortingAlgorithms.merge_sort,
            SortingAlgorithms.quick_sort,
            SortingAlgorithms.heap_sort,
            SortingAlgorithms.comb_sort,
        ]
        self.algorithm_names = [
            "Selection Sort",
            "Bubble Sort",
            "Insertion Sort",
            "Merge Sort",
            "Quick Sort",
            "Heap Sort",
            "Comb Sort"
        ]
        self.buttons = []
        self.return_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT - 60, 200, 40)
        self.numbers = []
        self.generate_numbers()
        self.create_buttons()

        # Nouveaux boutons du menu d'accueil
        self.start_buttons = [
            (pygame.Rect(WIDTH//2 - 150, 250, 300, 40), "Tester les algorithmes"),
            (pygame.Rect(WIDTH//2 - 150, 310, 300, 40), "Trier un cercle de couleurs"),
            (pygame.Rect(WIDTH//2 - 150, 370, 300, 40), "Afficher la complexité")
        ]

        self.comparisons = 0
        self.swaps = 0
        self.execution_time = 0
        self.start_ticks = 0
        self.is_sorting = False
        self.memory_used_kb = 0
        self.current_screen = "start"  # start, menu, circle_sort, complexity

    def generate_numbers(self):
        self.numbers = [random.randint(1, HEIGHT) for _ in range(WIDTH // BAR_WIDTH)]

    def create_buttons(self):
        self.buttons = []
        for i, name in enumerate(self.algorithm_names):
            rect = pygame.Rect(100, 70 + 40 * i, 200, 30)
            self.buttons.append((rect, name))

    def draw_bars(self, highlighted_indices=None):
        self.screen.fill(BG_COLOR)
        highlighted_indices = highlighted_indices or []
        for i, value in enumerate(self.numbers):
            x = i * BAR_WIDTH
            color = SELECTED_COLOR if i in highlighted_indices else BAR_COLOR
            pygame.draw.rect(self.screen, color, (x, HEIGHT - value, BAR_WIDTH, value))

        stats_text = self.font.render(f"Comparaisons: {self.comparisons} | Échanges: {self.swaps}", True, TEXT_COLOR)
        time_text = self.font.render(f"Temps: {self.execution_time:.6f}s", True, TEXT_COLOR)
        memory_text = self.font.render(f"Mémoire: {self.memory_used_kb:.2f} Ko", True, TEXT_COLOR)

        self.screen.blit(stats_text, (10, 10))
        self.screen.blit(time_text, (10, 40))
        self.screen.blit(memory_text, (10, 70))
        pygame.display.flip()

    def draw_menu(self):
        self.screen.fill(BG_COLOR)
        title = self.font.render("Cliquez sur un tri:", True, TEXT_COLOR)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
        mouse_pos = pygame.mouse.get_pos()

        for i, (rect, _) in enumerate(self.buttons):
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(self.screen, color, rect)
            text = self.font.render(self.algorithm_names[i], True, TEXT_COLOR)
            self.screen.blit(text, (rect.x + 10, rect.y + 5))

        # Dessine le bouton retour ici directement
        color = BUTTON_HOVER_COLOR if self.return_button.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, self.return_button)
        text = self.font.render("Retour au menu", True, TEXT_COLOR)
        self.screen.blit(text, (self.return_button.x + 25, self.return_button.y + 10))

        pygame.display.flip()


    def draw_return_button(self):
        mouse_pos = pygame.mouse.get_pos()
        color = BUTTON_HOVER_COLOR if self.return_button.collidepoint(mouse_pos) else BUTTON_COLOR
        pygame.draw.rect(self.screen, color, self.return_button)
        text = self.font.render("Retour au menu", True, TEXT_COLOR)
        self.screen.blit(text, (self.return_button.x + 25, self.return_button.y + 10))
        pygame.display.flip()

    def draw_swap(self, arr, i, j):
        self.comparisons += 1
        arr[i], arr[j] = arr[j], arr[i]
        self.swaps += 1
        self.execution_time = (pygame.time.get_ticks() - self.start_ticks) / 1000.0
        current, peak = tracemalloc.get_traced_memory()
        self.memory_used_kb = peak / 1024
        self.draw_bars([i, j])

    def measure_performance(self, sorting_function):
        self.comparisons = 0
        self.swaps = 0
        self.execution_time = 0
        self.memory_used_kb = 0

        tracemalloc.start()
        self.start_ticks = pygame.time.get_ticks()

        sorting_function(self.numbers, self.draw_swap)

        self.execution_time = (pygame.time.get_ticks() - self.start_ticks) / 1000.0
        tracemalloc.stop()
        self.draw_bars()
        return self.execution_time, self.memory_used_kb

    def draw_start_screen(self):
        self.screen.blit(self.background_image, (0, 0))
        title = self.large_font.render("Sorting Algorithms", True, TEXT_COLOR)
        self.screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 100))

        mouse_pos = pygame.mouse.get_pos()
        for rect, label in self.start_buttons:
            color = BUTTON_HOVER_COLOR if rect.collidepoint(mouse_pos) else BUTTON_COLOR
            pygame.draw.rect(self.screen, color, rect)
            text = self.font.render(label, True, TEXT_COLOR)
            self.screen.blit(text, (rect.x + 10, rect.y + 10))

        pygame.display.flip()

    def run(self):
        running = True
        while running:
            if self.current_screen == "start":
                self.draw_start_screen()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        for i, (rect, label) in enumerate(self.start_buttons):
                            if rect.collidepoint(event.pos):
                                if i == 0:
                                    self.current_screen = "menu"
                                elif i == 1:
                                    print("TODO: Trier un cercle de couleurs")
                                elif i == 2:
                                    print("TODO: Afficher complexité")

            elif self.current_screen == "menu":
                self.draw_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if self.return_button.collidepoint(event.pos):
                            self.current_screen = "start"
                        else:
                            for i, (rect, _) in enumerate(self.buttons):
                                if rect.collidepoint(event.pos):
                                    self.generate_numbers()
                                    self.draw_bars()
                                    self.execution_time = 0
                                    execution_time, memory_used = self.measure_performance(self.algorithms[i])
                                    print(f"{self.algorithm_names[i]} - Temps: {execution_time:.6f}s | Mémoire: {memory_used:.2f} Ko")
                                    self.current_screen = "menu"
                self.draw_return_button()
            self.clock.tick(60)
        pygame.quit()
