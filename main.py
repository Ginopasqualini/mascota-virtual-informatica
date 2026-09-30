import math
import random
import subprocess
import sys
from pathlib import Path
from enum import Enum

import pygame

# Configuración del juego
WIDTH, HEIGHT = 1200, 800
FPS = 60
BASE_DIR = Path(__file__).resolve().parent
ASSET_DIR = BASE_DIR / "assets"
SOUNDS_DIR = ASSET_DIR / "sounds"
IMAGES_DIR = ASSET_DIR / "images"

# Colores
BORDO = (110, 20, 30)
AMARILLO = (255, 205, 50)
ROJO = (185, 35, 35)
BLANCO = (245, 245, 245)
AZUL_MARINO = (18, 40, 80)
AZUL_OSCURO = (9, 18, 40)
GRIS = (220, 220, 220)
NEGRO = (15, 15, 15)
NARANJA = (255, 135, 40)
VERDE = (36, 170, 100)
CELESTE = (88, 168, 255)
MARRON = (139, 69, 19)
MARRON_CLARO = (184, 115, 51)

# Estados
class GameState(Enum):
    MAIN = 1
    SHOP = 2
    MINIGAME = 3

class PetMood(Enum):
    FELIZ = 1
    TRANQUILO = 2
    TRISTE = 3
    CANSADO = 4
    LLORANDO = 5
    BRAZOS_ARRIBA = 6
    BOSTEZANDO = 7

# Stats iniciales
INITIAL_STATS = {
    "energia": 82,
    "hambre": 72,
    "higiene": 76,
    "felicidad": 78,
    "programacion": 80,
}

SOUND_FILES = {
    "alimentar": SOUNDS_DIR / "eat.wav",
    "bañar": SOUNDS_DIR / "bath.wav",
    "jugar": SOUNDS_DIR / "play.wav",
    "programar": SOUNDS_DIR / "code.wav",
    "dormir": SOUNDS_DIR / "sleep.wav",
    "feliz": SOUNDS_DIR / "happy.wav",
    "triste": SOUNDS_DIR / "sad.wav",
}

SHOP_ITEMS = {
    "sombrero_rojo": {"precio": 50, "nombre": "Sombrero Rojo", "color": ROJO},
    "sombrero_amarillo": {"precio": 50, "nombre": "Sombrero Amarillo", "color": AMARILLO},
    "lentes": {"precio": 75, "nombre": "Lentes", "color": NEGRO},
    "corona": {"precio": 150, "nombre": "Corona", "color": AMARILLO},
    "pañuelo_bordo": {"precio": 40, "nombre": "Pañuelo Bordó", "color": BORDO},
}

def ensure_assets():
    generator = ASSET_DIR / "generate_assets.py"
    if not generator.exists():
        return
    try:
        subprocess.run([sys.executable, str(generator)], check=True)
    except Exception:
        pass

class SoundManager:
    def __init__(self):
        self.enabled = True
        self.sounds = {}
        for name, path in SOUND_FILES.items():
            if path.exists():
                try:
                    self.sounds[name] = pygame.mixer.Sound(str(path))
                except Exception:
                    self.sounds[name] = None

    def play(self, name):
        if not self.enabled:
            return
        sound = self.sounds.get(name)
        if sound is not None:
            sound.play()

    def toggle(self):
        self.enabled = not self.enabled

class Mascota:
    def __init__(self):
        self.stats = INITIAL_STATS.copy()
        self.mood = PetMood.TRANQUILO
        self.anim_timer = 0.0
        self.puntos = 0
        self.dinero = 200
        self.items_comprados = set()

    def update(self, dt):
        self.anim_timer += dt
        self.stats["energia"] = max(0, self.stats["energia"] - dt * 0.7)
        self.stats["hambre"] = max(0, self.stats["hambre"] - dt * 0.8)
        self.stats["higiene"] = max(0, self.stats["higiene"] - dt * 0.6)
        self.stats["felicidad"] = max(0, self.stats["felicidad"] - dt * 0.5)
        self.stats["programacion"] = max(0, self.stats["programacion"] - dt * 0.45)

        avg = sum(self.stats.values()) / len(self.stats)
        
        if self.stats["hambre"] < 30:
            self.mood = PetMood.LLORANDO
        elif self.stats["energia"] < 25:
            self.mood = PetMood.BOSTEZANDO
        elif self.stats["felicidad"] > 75 and avg > 70:
            self.mood = PetMood.BRAZOS_ARRIBA
        elif avg > 75:
            self.mood = PetMood.FELIZ
        elif avg > 45:
            self.mood = PetMood.TRANQUILO
        elif avg > 25:
            self.mood = PetMood.TRISTE
        else:
            self.mood = PetMood.CANSADO

    def action(self, accion):
        if accion == "alimentar":
            self.stats["hambre"] = min(100, self.stats["hambre"] + 20)
            self.stats["energia"] = min(100, self.stats["energia"] + 10)
            self.stats["felicidad"] = min(100, self.stats["felicidad"] + 8)
        elif accion == "bañar":
            self.stats["higiene"] = min(100, self.stats["higiene"] + 24)
            self.stats["felicidad"] = min(100, self.stats["felicidad"] + 6)
        elif accion == "jugar":
            self.stats["felicidad"] = min(100, self.stats["felicidad"] + 22)
            self.stats["energia"] = max(0, self.stats["energia"] - 8)
            self.stats["programacion"] = max(0, self.stats["programacion"] - 5)
        elif accion == "programar":
            self.stats["programacion"] = min(100, self.stats["programacion"] + 22)
            self.stats["felicidad"] = min(100, self.stats["felicidad"] + 7)
            self.stats["energia"] = max(0, self.stats["energia"] - 6)
        elif accion == "dormir":
            self.stats["energia"] = min(100, self.stats["energia"] + 26)
            self.stats["felicidad"] = min(100, self.stats["felicidad"] + 5)
        elif accion == "reiniciar":
            self.stats = INITIAL_STATS.copy()
            self.mood = PetMood.TRANQUILO

    def ganar_puntos(self, cantidad):
        self.puntos += cantidad
        self.dinero += cantidad // 10

    def comprar_item(self, item_id):
        if item_id not in SHOP_ITEMS:
            return False
        item = SHOP_ITEMS[item_id]
        if self.dinero >= item["precio"]:
            self.dinero -= item["precio"]
            self.items_comprados.add(item_id)
            return True
        return False

class Button:
    def __init__(self, x, y, w, h, text, color, text_color=BLANCO):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text
        self.color = color
        self.text_color = text_color
        self.hover = False

    def draw(self, screen):
        color = tuple(min(c + 30, 255) for c in self.color) if self.hover else self.color
        pygame.draw.rect(screen, color, self.rect, border_radius=16)
        pygame.draw.rect(screen, BLANCO, self.rect, 2, border_radius=16)
        font = pygame.font.SysFont("arial", 16, bold=True)
        label = font.render(self.text, True, self.text_color)
        screen.blit(label, (self.rect.centerx - label.get_width() / 2, self.rect.centery - label.get_height() / 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

    def update_hover(self, pos):
        self.hover = self.rect.collidepoint(pos)

class SpaceInvadersGame:
    def __init__(self):
        self.name = "Space Invaders"
        self.score = 0
        self.active = True
        self.timer = 0
        self.duration = 30
        self.player_pos = WIDTH // 2
        self.enemies = []
        self.bullets = []
        self.spawn_timer = 0
        for _ in range(3):
            self.enemies.append({"x": random.randint(50, WIDTH - 50), "y": random.randint(50, 150), "vy": random.uniform(1, 3)})

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.duration:
            self.active = False
        self.spawn_timer += dt
        if self.spawn_timer > 0.5:
            self.enemies.append({"x": random.randint(50, WIDTH - 50), "y": 30, "vy": random.uniform(1, 3)})
            self.spawn_timer = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos = max(30, self.player_pos - 300 * dt)
        if keys[pygame.K_RIGHT]:
            self.player_pos = min(WIDTH - 30, self.player_pos + 300 * dt)
        if keys[pygame.K_SPACE]:
            self.bullets.append({"x": self.player_pos, "y": HEIGHT - 100})
        for enemy in self.enemies[:]:
            enemy["y"] += enemy["vy"] * 100 * dt
            if enemy["y"] > HEIGHT:
                self.enemies.remove(enemy)
        for bullet in self.bullets[:]:
            bullet["y"] -= 300 * dt
            if bullet["y"] < 0:
                self.bullets.remove(bullet)
            for enemy in self.enemies[:]:
                if abs(bullet["x"] - enemy["x"]) < 20 and abs(bullet["y"] - enemy["y"]) < 20:
                    self.score += 10
                    if bullet in self.bullets:
                        self.bullets.remove(bullet)
                    if enemy in self.enemies:
                        self.enemies.remove(enemy)
                    break
        return self.timer >= self.duration

    def draw(self, screen):
        screen.fill(AZUL_OSCURO)
        pygame.draw.rect(screen, VERDE, (self.player_pos - 15, HEIGHT - 100, 30, 30))
        for enemy in self.enemies:
            pygame.draw.rect(screen, ROJO, (enemy["x"] - 15, enemy["y"] - 15, 30, 30))
        for bullet in self.bullets:
            pygame.draw.rect(screen, AMARILLO, (bullet["x"] - 3, bullet["y"], 6, 15))
        font = pygame.font.SysFont("arial", 36, bold=True)
        score_text = font.render(f"Score: {self.score}", True, BLANCO)
        screen.blit(score_text, (20, 20))
        timer_text = font.render(f"Tiempo: {int(self.duration - self.timer)}", True, BLANCO)
        screen.blit(timer_text, (WIDTH - 300, 20))

    def get_score(self):
        return self.score

class VoleyGame:
    def __init__(self):
        self.name = "Voley"
        self.score = 0
        self.active = True
        self.timer = 0
        self.duration = 30
        self.player_pos = WIDTH // 2
        self.ball_x = WIDTH // 2
        self.ball_y = HEIGHT // 2
        self.ball_vx = random.uniform(-3, 3)
        self.ball_vy = random.uniform(-3, -1)
        self.combo = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.duration:
            self.active = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_pos = max(30, self.player_pos - 300 * dt)
        if keys[pygame.K_RIGHT]:
            self.player_pos = min(WIDTH - 30, self.player_pos + 300 * dt)
        self.ball_x += self.ball_vx * 200 * dt
        self.ball_y += self.ball_vy * 200 * dt
        self.ball_vy += 300 * dt
        if self.ball_x < 10 or self.ball_x > WIDTH - 10:
            self.ball_vx *= -1
        if abs(self.ball_x - self.player_pos) < 40 and abs(self.ball_y - (HEIGHT - 50)) < 30:
            self.ball_vy = -5
            self.ball_vx += random.uniform(-2, 2)
            self.score += 10
            self.combo += 1
        if self.ball_y > HEIGHT:
            self.ball_x = WIDTH // 2
            self.ball_y = HEIGHT // 2
            self.ball_vx = random.uniform(-3, 3)
            self.ball_vy = random.uniform(-3, -1)
            self.combo = 0
        return self.timer >= self.duration

    def draw(self, screen):
        screen.fill(VERDE)
        pygame.draw.line(screen, BLANCO, (0, HEIGHT // 2), (WIDTH, HEIGHT // 2), 3)
        pygame.draw.rect(screen, AMARILLO, (self.player_pos - 30, HEIGHT - 50, 60, 30))
        pygame.draw.circle(screen, BLANCO, (int(self.ball_x), int(self.ball_y)), 8)
        font = pygame.font.SysFont("arial", 36, bold=True)
        score_text = font.render(f"Score: {self.score} | Combo: {self.combo}", True, NEGRO)
        screen.blit(score_text, (20, 20))

    def get_score(self):
        return self.score

class CarGame:
    def __init__(self):
        self.name = "Autos"
        self.score = 0
        self.active = True
        self.timer = 0
        self.duration = 30
        self.player_x = WIDTH // 2
        self.obstacles = []
        self.spawn_timer = 0

    def update(self, dt):
        self.timer += dt
        if self.timer >= self.duration:
            self.active = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_x = max(20, self.player_x - 300 * dt)
        if keys[pygame.K_RIGHT]:
            self.player_x = min(WIDTH - 20, self.player_x + 300 * dt)
        self.spawn_timer += dt
        if self.spawn_timer > 0.3:
            lane = random.choice([WIDTH // 3, WIDTH // 2, 2 * WIDTH // 3])
            self.obstacles.append({"x": lane, "y": -30})
            self.spawn_timer = 0
        for obs in self.obstacles[:]:
            obs["y"] += 400 * dt
            if obs["y"] > HEIGHT:
                self.obstacles.remove(obs)
                self.score += 5
        for obs in self.obstacles:
            if abs(obs["x"] - self.player_x) < 30 and abs(obs["y"] - (HEIGHT - 50)) < 30:
                self.obstacles.remove(obs)
                self.score = max(0, self.score - 10)
                break
        return self.timer >= self.duration

    def draw(self, screen):
        screen.fill(GRIS)
        pygame.draw.rect(screen, (50, 50, 50), (WIDTH // 3 - 20, 0, 40, HEIGHT))
        pygame.draw.rect(screen, (50, 50, 50), (WIDTH // 2 - 20, 0, 40, HEIGHT))
        pygame.draw.rect(screen, (50, 50, 50), (2 * WIDTH // 3 - 20, 0, 40, HEIGHT))
        pygame.draw.rect(screen, VERDE, (self.player_x - 20, HEIGHT - 60, 40, 40))
        for obs in self.obstacles:
            pygame.draw.rect(screen, ROJO, (obs["x"] - 20, obs["y"], 40, 40))
        font = pygame.font.SysFont("arial", 36, bold=True)
        score_text = font.render(f"Score: {self.score}", True, BLANCO)
        screen.blit(score_text, (20, 20))

    def get_score(self):
        return self.score

def draw_shield(screen, x, y, scale=1.0):
    s = scale
    shield = pygame.Surface((140 * s, 150 * s), pygame.SRCALPHA)
    pygame.draw.polygon(shield, BORDO, [(70 * s, 0), (140 * s, 20 * s), (130 * s, 150 * s), (10 * s, 150 * s), (0, 20 * s)])
    pygame.draw.polygon(shield, AMARILLO, [(70 * s, 18 * s), (122 * s, 32 * s), (112 * s, 128 * s), (28 * s, 128 * s), (18 * s, 32 * s)])
    pygame.draw.circle(shield, BLANCO, (70 * s, 70 * s), 34 * s)
    pygame.draw.circle(shield, BORDO, (70 * s, 70 * s), 18 * s)
    pygame.draw.line(shield, BORDO, (70 * s, 18 * s), (70 * s, 120 * s), 4)
    pygame.draw.line(shield, BORDO, (18 * s, 70 * s), (120 * s, 70 * s), 4)
    screen.blit(shield, (x, y))

def draw_hedgehog(screen, pet, x, y):
    bob = math.sin(pet.anim_timer * 3) * 5
    body_x, body_y = x, y + bob
    pygame.draw.ellipse(screen, (60, 30, 10), (body_x - 100, body_y + 130, 200, 35))
    pygame.draw.ellipse(screen, MARRON, (body_x - 80, body_y, 160, 110))
    pygame.draw.ellipse(screen, MARRON_CLARO, (body_x - 60, body_y + 20, 120, 70))
    espinas = [(body_x - 50, body_y - 20), (body_x - 20, body_y - 25), (body_x + 20, body_y - 25), (body_x + 50, body_y - 20), (body_x + 70, body_y + 10)]
    for espina in espinas:
        pygame.draw.polygon(screen, MARRON, [espina, (espina[0] - 5, espina[1] - 15), (espina[0] + 5, espina[1] - 15)])
    pygame.draw.circle(screen, MARRON, (body_x, body_y - 30), 35)
    pygame.draw.circle(screen, MARRON_CLARO, (body_x, body_y - 25), 25)
    eye_y = body_y - 40
    if pet.mood in (PetMood.FELIZ, PetMood.BRAZOS_ARRIBA):
        eye_y = body_y - 35
    elif pet.mood == PetMood.TRISTE:
        eye_y = body_y - 20
    elif pet.mood == PetMood.BOSTEZANDO:
        eye_y = body_y - 30
    pygame.draw.ellipse(screen, NEGRO, (body_x - 20, eye_y, 12, 12))
    pygame.draw.ellipse(screen, NEGRO, (body_x + 8, eye_y, 12, 12))
    pygame.draw.ellipse(screen, BLANCO, (body_x - 16, eye_y + 2, 4, 4))
    pygame.draw.ellipse(screen, BLANCO, (body_x + 12, eye_y + 2, 4, 4))
    pygame.draw.circle(screen, NARANJA, (body_x, body_y - 10), 6)
    pygame.draw.ellipse(screen, MARRON, (body_x - 40, body_y + 100, 20, 25))
    pygame.draw.ellipse(screen, MARRON, (body_x + 20, body_y + 100, 20, 25))
    if pet.mood == PetMood.LLORANDO:
        pygame.draw.circle(screen, CELESTE, (body_x - 16, body_y - 20), 3)
        pygame.draw.circle(screen, CELESTE, (body_x + 12, body_y - 20), 3)
        pygame.draw.arc(screen, NEGRO, (body_x - 15, body_y + 5, 30, 20), 3.3, 6.2, 3)
    elif pet.mood == PetMood.BRAZOS_ARRIBA:
        pygame.draw.line(screen, MARRON, (body_x - 60, body_y + 20), (body_x - 80, body_y - 30), 8)
        pygame.draw.line(screen, MARRON, (body_x + 60, body_y + 20), (body_x + 80, body_y - 30), 8)
        pygame.draw.arc(screen, NEGRO, (body_x - 15, body_y + 5, 30, 25), 0.2, 3.1, 3)
    elif pet.mood == PetMood.BOSTEZANDO:
        pygame.draw.ellipse(screen, NEGRO, (body_x - 8, body_y + 8, 16, 20))
    elif pet.mood == PetMood.FELIZ:
        pygame.draw.arc(screen, NEGRO, (body_x - 15, body_y + 5, 30, 20), 0.2, 3.1, 3)
    elif pet.mood == PetMood.TRANQUILO:
        pygame.draw.line(screen, NEGRO, (body_x - 15, body_y + 10), (body_x + 15, body_y + 10), 2)
    elif pet.mood == PetMood.TRISTE:
        pygame.draw.arc(screen, NEGRO, (body_x - 15, body_y - 5, 30, 20), 3.3, 6.2, 3)
    elif pet.mood == PetMood.CANSADO:
        pygame.draw.line(screen, NEGRO, (body_x - 20, body_y - 35), (body_x - 12, body_y - 35), 3)
        pygame.draw.line(screen, NEGRO, (body_x + 8, body_y - 35), (body_x + 16, body_y - 35), 3)
    if "sombrero_rojo" in pet.items_comprados:
        pygame.draw.polygon(screen, ROJO, [(body_x - 20, body_y - 60), (body_x + 20, body_y - 60), (body_x + 25, body_y - 45), (body_x - 25, body_y - 45)])
    if "corona" in pet.items_comprados:
        for i in range(5):
            pygame.draw.circle(screen, AMARILLO, (body_x - 20 + i * 10, body_y - 70), 5)

def draw_bar(screen, x, y, w, h, value, color, label):
    pygame.draw.rect(screen, (80, 80, 80), (x, y, w, h), border_radius=12)
    pygame.draw.rect(screen, color, (x, y, w * (value / 100), h), border_radius=12)
    font = pygame.font.SysFont("arial", 14, bold=True)
    text = font.render(f"{label}: {int(value)}%", True, BLANCO)
    screen.blit(text, (x, y - 20))

def draw_shop(screen, pet):
    screen.fill(BORDO)
    font_title = pygame.font.SysFont("arial", 40, bold=True)
    title = font_title.render("TIENDA", True, AMARILLO)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 20))
    font_money = pygame.font.SysFont("arial", 24, bold=True)
    money_text = font_money.render(f"Dinero: ${pet.dinero}", True, AMARILLO)
    screen.blit(money_text, (20, 80))
    y_pos = 150
    for i, (item_id, item_info) in enumerate(SHOP_ITEMS.items()):
        comprado = item_id in pet.items_comprados
        color = GRIS if comprado else BLANCO
        rect = pygame.Rect(50, y_pos, 400, 50)
        pygame.draw.rect(screen, item_info["color"], rect, border_radius=10)
        pygame.draw.rect(screen, color, rect, 2, border_radius=10)
        text = f"{item_info['nombre']} - ${item_info['precio']}" + (" (COMPRADO)" if comprado else "")
        font_item = pygame.font.SysFont("arial", 16, bold=True)
        item_text = font_item.render(text, True, color)
        screen.blit(item_text, (60, y_pos + 12))
        key_text = pygame.font.SysFont("arial", 14, bold=True).render(f"Presiona {i+1}", True, BLANCO)
        screen.blit(key_text, (500, y_pos + 12))
        y_pos += 70
    font_back = pygame.font.SysFont("arial", 20, bold=True)
    back_text = font_back.render("VOLVER (ESC)", True, BLANCO)
    screen.blit(back_text, (WIDTH - 250, HEIGHT - 50))

def draw_minigame_selector(screen):
    screen.fill(AZUL_OSCURO)
    font_title = pygame.font.SysFont("arial", 40, bold=True)
    title = font_title.render("ELIGE UN MINIJUEGO", True, AMARILLO)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 50))
    games = [("1 - Space Invaders", 150), ("2 - Voley", 300), ("3 - Autos", 450)]
    font_game = pygame.font.SysFont("arial", 28, bold=True)
    for text, y in games:
        game_text = font_game.render(text, True, BLANCO)
        screen.blit(game_text, (WIDTH // 2 - game_text.get_width() // 2, y))

def draw_minigame_end(screen, score):
    overlay = pygame.Surface((WIDTH, HEIGHT))
    overlay.set_alpha(200)
    overlay.fill(NEGRO)
    screen.blit(overlay, (0, 0))
    font_end = pygame.font.SysFont("arial", 50, bold=True)
    end_text = font_end.render("¡JUEGO TERMINADO!", True, AMARILLO)
    screen.blit(end_text, (WIDTH // 2 - end_text.get_width() // 2, HEIGHT // 2 - 100))
    font_score = pygame.font.SysFont("arial", 40, bold=True)
    score_text = font_score.render(f"Puntos: {score}", True, VERDE)
    screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
    font_continue = pygame.font.SysFont("arial", 24, bold=True)
    continue_text = font_continue.render("Presiona ESPACIO para volver", True, BLANCO)
    screen.blit(continue_text, (WIDTH // 2 - continue_text.get_width() // 2, HEIGHT // 2 + 100))

def main():
    ensure_assets()
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Erizo Virtual de Informática - IPET 249")
    clock = pygame.time.Clock()
    pet = Mascota()
    sound_manager = SoundManager()
    game_state = GameState.MAIN
    current_minigame = None
    minigame_finished = False
    minigame_score = 0
    buttons = [
        Button(40, 680, 140, 50, "1. Alimentar", BORDO),
        Button(190, 680, 140, 50, "2. Bañar", AZUL_MARINO),
        Button(340, 680, 140, 50, "3. Jugar", ROJO),
        Button(490, 680, 140, 50, "4. Programar", VERDE),
        Button(640, 680, 140, 50, "5. Dormir", AZUL_OSCURO),
        Button(790, 680, 140, 50, "T. Tienda", AMARILLO),
    ]
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == GameState.MAIN:
                    if event.key == pygame.K_1:
                        pet.action("alimentar")
                        sound_manager.play("alimentar")
                    elif event.key == pygame.K_2:
                        pet.action("bañar")
                        sound_manager.play("bañar")
                    elif event.key == pygame.K_3:
                        game_state = GameState.MINIGAME
                        sound_manager.play("jugar")
                    elif event.key == pygame.K_4:
                        pet.action("programar")
                        sound_manager.play("programar")
                    elif event.key == pygame.K_5:
                        pet.action("dormir")
                        sound_manager.play("dormir")
                    elif event.key == pygame.K_t:
                        game_state = GameState.SHOP
                    elif event.key == pygame.K_m:
                        sound_manager.toggle()
                    elif event.key == pygame.K_r:
                        pet.action("reiniciar")
                elif game_state == GameState.MINIGAME:
                    if event.key == pygame.K_1 and current_minigame is None:
                        current_minigame = SpaceInvadersGame()
                    elif event.key == pygame.K_2 and current_minigame is None:
                        current_minigame = VoleyGame()
                    elif event.key == pygame.K_3 and current_minigame is None:
                        current_minigame = CarGame()
                    elif event.key == pygame.K_SPACE and minigame_finished:
                        pet.ganar_puntos(minigame_score)
                        game_state = GameState.MAIN
                        current_minigame = None
                        minigame_finished = False
                        minigame_score = 0
                elif game_state == GameState.SHOP:
                    if event.key == pygame.K_ESCAPE:
                        game_state = GameState.MAIN
                    elif event.key == pygame.K_1:
                        pet.comprar_item("sombrero_rojo")
                    elif event.key == pygame.K_2:
                        pet.comprar_item("sombrero_amarillo")
                    elif event.key == pygame.K_3:
                        pet.comprar_item("lentes")
                    elif event.key == pygame.K_4:
                        pet.comprar_item("corona")
                    elif event.key == pygame.K_5:
                        pet.comprar_item("pañuelo_bordo")
            elif event.type == pygame.MOUSEBUTTONDOWN and game_state == GameState.MAIN:
                pos = event.pos
                for button in buttons:
                    if button.is_clicked(pos):
                        if "Alimentar" in button.text:
                            pet.action("alimentar")
                            sound_manager.play("alimentar")
                        elif "Bañar" in button.text:
                            pet.action("bañar")
                            sound_manager.play("bañar")
                        elif "Jugar" in button.text:
                            game_state = GameState.MINIGAME
                            sound_manager.play("jugar")
                        elif "Programar" in button.text:
                            pet.action("programar")
                            sound_manager.play("programar")
                        elif "Dormir" in button.text:
                            pet.action("dormir")
                            sound_manager.play("dormir")
                        elif "Tienda" in button.text:
                            game_state = GameState.SHOP
        if game_state == GameState.MAIN:
            pet.update(dt)
            for button in buttons:
                button.update_hover(mouse_pos)
            screen.fill((245, 242, 236))
            pygame.draw.rect(screen, BORDO, (0, 0, WIDTH, 120))
            pygame.draw.rect(screen, AMARILLO, (0, 120, WIDTH, 20))
            pygame.draw.rect(screen, (13, 15, 18), (0, 140, WIDTH, HEIGHT - 140))
            draw_shield(screen, 20, 15, 0.7)
            font = pygame.font.SysFont("arial", 28, bold=True)
            title = font.render("IPET 249 | Especialidad en Informática", True, BLANCO)
            screen.blit(title, (130, 35))
            pygame.draw.rect(screen, (30, 35, 52), (20, 160, 280, 500), border_radius=18)
            pygame.draw.rect(screen, AMARILLO, (20, 160, 280, 500), 3, border_radius=18)
            draw_bar(screen, 40, 190, 240, 14, pet.stats["energia"], (33, 191, 115), "Energía")
            draw_bar(screen, 40, 235, 240, 14, pet.stats["hambre"], (255, 153, 0), "Hambre")
            draw_bar(screen, 40, 280, 240, 14, pet.stats["higiene"], (92, 170, 255), "Higiene")
            draw_bar(screen, 40, 325, 240, 14, pet.stats["felicidad"], (230, 80, 70), "Felicidad")
            draw_bar(screen, 40, 370, 240, 14, pet.stats["programacion"], (220, 202, 58), "Código")
            font_points = pygame.font.SysFont("arial", 16, bold=True)
            points_text = font_points.render(f"Puntos: {pet.puntos}", True, AMARILLO)
            money_text = font_points.render(f"Dinero: ${pet.dinero}", True, AMARILLO)
            screen.blit(points_text, (40, 415))
            screen.blit(money_text, (40, 445))
            draw_hedgehog(screen, pet, 650, 380)
            mood_font = pygame.font.SysFont("arial", 24, bold=True)
            mood_text = mood_font.render(f"Estado: {pet.mood.name}", True, BLANCO)
            screen.blit(mood_text, (350, 180))
            for button in buttons:
                button.draw(screen)
        elif game_state == GameState.MINIGAME:
            if current_minigame is None:
                draw_minigame_selector(screen)
            else:
                game_finished = current_minigame.update(dt)
                current_minigame.draw(screen)
                if game_finished:
                    minigame_finished = True
                    minigame_score = current_minigame.get_score()
                    draw_minigame_end(screen, minigame_score)
        elif game_state == GameState.SHOP:
            draw_shop(screen, pet)
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
