# -*- coding: utf-8 -*-
"""
Flappy Bird  –  ASCII Edition
Rendered with pygame (all visuals are ASCII characters).
Start / Game-Over menus are displayed with tkinter.
"""

import pygame
import sys
import random
import math
import tkinter as tk
from tkinter import ttk, font as tkfont

# ══════════════════════════════════════════════════════════════════════
#  SETTINGS
# ══════════════════════════════════════════════════════════════════════
WIN_W, WIN_H   = 900, 600
FPS            = 60
GRAVITY        = 0.45
FLAP_FORCE     = -8.5
PIPE_SPEED     = 3.0
PIPE_GAP       = 190        # vertical gap between top / bottom pipe
GROUND_H       = 56
SPAWN_EVERY    = 90         # frames between new pipe pairs
CHAR_W         = 10         # pixel width  of one monospace character
CHAR_H         = 18         # pixel height of one monospace character
PIPE_COLS      = 7          # how many chars wide each pipe section is

# ── Palette ──────────────────────────────────────────────────────────
SKY       = ( 10,  18,  42)
STAR_C    = (200, 210, 255)
CLOUD_C   = (160, 180, 220)
PIPE_C    = (  0, 200,  70)
PIPE_S    = (  0, 130,  45)   # shadow side
PIPE_CAP  = (  0, 230,  90)
GROUND_C  = ( 90,  58,  22)
GROUND_L  = (120,  80,  35)
BIRD_Y    = (255, 215,   0)   # yellow
BIRD_W    = (255, 255, 255)   # white (eye / wing)
BIRD_B    = ( 20,  20,  20)   # dark (pupil / outline)
WHITE     = (255, 255, 255)
SCORE_C   = (255, 235,  80)
DANGER_C  = (255,  70,  70)
CYAN      = (  0, 220, 240)
DIM       = (100, 120, 160)


# ══════════════════════════════════════════════════════════════════════
#  TKINTER  SCREENS
# ══════════════════════════════════════════════════════════════════════

def _apply_dark_style(root: tk.Tk):
    """Apply a dark, retro-terminal style to a tkinter window."""
    root.configure(bg="#0a1228")
    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure("TFrame",  background="#0a1228")
    style.configure("TLabel",  background="#0a1228", foreground="#ffe050",
                    font=("Courier New", 12))
    style.configure("Big.TLabel", background="#0a1228", foreground="#00e8ff",
                    font=("Courier New", 28, "bold"))
    style.configure("Sub.TLabel", background="#0a1228", foreground="#a0b4d8",
                    font=("Courier New", 11))
    style.configure("Score.TLabel", background="#0a1228", foreground="#ff6060",
                    font=("Courier New", 18, "bold"))
    style.configure("Play.TButton",
                    background="#00c846", foreground="#0a1228",
                    font=("Courier New", 14, "bold"),
                    relief="flat", padding=(20, 8))
    style.map("Play.TButton",
              background=[("active", "#00ff60")],
              foreground=[("active", "#000000")])
    style.configure("Quit.TButton",
                    background="#2a1a1a", foreground="#ff6060",
                    font=("Courier New", 12),
                    relief="flat", padding=(14, 6))
    style.map("Quit.TButton",
              background=[("active", "#ff3030")],
              foreground=[("active", "#ffffff")])


TITLE_ART = r"""
  _____ _                             ____  _         _
 |  ___| | __ _ _ __  _ __  _   _   | __ )(_)_ __ __| |
 | |_  | |/ _` | '_ \| '_ \| | | |  |  _ \| | '__/ _` |
 |  _| | | (_| | |_) | |_) | |_| |  | |_) | | | | (_| |
 |_|   |_|\__,_| .__/| .__/ \__, |  |____/|_|_|  \__,_|
                |_|   |_|   |___/
""".strip("\n")


def show_start_screen() -> bool:
    """
    Display the tkinter start screen.
    Returns True  → user wants to play.
    Returns False → user wants to quit.
    """
    result = {"play": False}

    root = tk.Tk()
    root.title("Flappy Bird  –  ASCII Edition")
    root.resizable(False, False)
    _apply_dark_style(root)

    # Centre on screen
    w, h = 680, 440
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    frame = ttk.Frame(root, padding=20)
    frame.pack(fill="both", expand=True)

    # ASCII title art
    art_lbl = tk.Label(
        frame, text=TITLE_ART,
        bg="#0a1228", fg="#00e8ff",
        font=("Courier New", 9, "bold"), justify="left"
    )
    art_lbl.pack(pady=(10, 4))

    ttk.Label(frame,
              text="─── ASCII  EDITION ───",
              style="Sub.TLabel").pack(pady=2)

    instructions = (
        "  [SPACE] or [UP]  →  Flap wings\n"
        "  Dodge the pipes and survive!\n"
        "  Every pipe you pass = +1 point"
    )
    ttk.Label(frame, text=instructions,
              style="Sub.TLabel", justify="left").pack(pady=12)

    ttk.Label(frame,
              text="  Bird  :  (>)  flapping  (^) / (v)",
              style="Sub.TLabel").pack()
    ttk.Label(frame,
              text="  Pipes :  blocks of  #  characters",
              style="Sub.TLabel").pack(pady=(0, 16))

    def on_play():
        result["play"] = True
        root.destroy()

    def on_quit():
        result["play"] = False
        root.destroy()

    btn_frame = ttk.Frame(frame)
    btn_frame.pack()
    ttk.Button(btn_frame, text="▶  PLAY",  style="Play.TButton",
               command=on_play).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="✕  QUIT",  style="Quit.TButton",
               command=on_quit).grid(row=0, column=1, padx=10)

    root.bind("<Return>", lambda e: on_play())
    root.bind("<Escape>", lambda e: on_quit())
    root.protocol("WM_DELETE_WINDOW", on_quit)
    root.mainloop()
    return result["play"]


def show_gameover_screen(score: int, best: int) -> str:
    """
    Display the tkinter game-over screen.
    Returns 'play'  → restart.
    Returns 'quit'  → exit.
    """
    result = {"action": "quit"}

    root = tk.Tk()
    root.title("Game Over")
    root.resizable(False, False)
    _apply_dark_style(root)

    w, h = 480, 380
    sw, sh = root.winfo_screenwidth(), root.winfo_screenheight()
    root.geometry(f"{w}x{h}+{(sw-w)//2}+{(sh-h)//2}")

    frame = ttk.Frame(root, padding=30)
    frame.pack(fill="both", expand=True)

    tk.Label(frame,
             text=r"""
  ____                         ___
 / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
| |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
| |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
 \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
""".strip("\n"),
             bg="#0a1228", fg="#ff5050",
             font=("Courier New", 8, "bold"), justify="left"
             ).pack(pady=(0, 12))

    ttk.Label(frame,
              text=f"  Score  :  {score}",
              style="Score.TLabel").pack(anchor="w", padx=40)
    ttk.Label(frame,
              text=f"  Best   :  {best}",
              style="Score.TLabel").pack(anchor="w", padx=40, pady=(0, 20))

    def on_play():
        result["action"] = "play"
        root.destroy()

    def on_quit():
        result["action"] = "quit"
        root.destroy()

    btn_frame = ttk.Frame(frame)
    btn_frame.pack()
    ttk.Button(btn_frame, text="↺  PLAY AGAIN", style="Play.TButton",
               command=on_play).grid(row=0, column=0, padx=10)
    ttk.Button(btn_frame, text="✕  QUIT",       style="Quit.TButton",
               command=on_quit).grid(row=0, column=1, padx=10)

    root.bind("<Return>", lambda e: on_play())
    root.bind("<Escape>", lambda e: on_quit())
    root.protocol("WM_DELETE_WINDOW", on_quit)
    root.mainloop()
    return result["action"]


# ══════════════════════════════════════════════════════════════════════
#  GAME OBJECTS
# ══════════════════════════════════════════════════════════════════════

class Bird:
    FRAMES = ["(>)", "(^)", "(v)"]   # neutral / flap-up / flap-down

    def __init__(self):
        self.x   = WIN_W // 4
        self.y   = float(WIN_H // 2)
        self.vel = 0.0
        self.frame_idx   = 0          # animation frame index
        self.frame_timer = 0
        self.alive = True
        self.angle = 0.0              # visual tilt (degrees)

    # ── Physics ──────────────────────────────────────────────────────
    def flap(self):
        self.vel = FLAP_FORCE
        self.frame_idx   = 1          # force flap-up frame
        self.frame_timer = 8

    def update(self):
        self.vel += GRAVITY
        self.y   += self.vel

        # Tilt proportional to velocity
        self.angle = max(-30, min(70, self.vel * 4.5))

        # Animate frame
        if self.frame_timer > 0:
            self.frame_timer -= 1
        else:
            if self.vel > 1.5:
                self.frame_idx = 2    # falling
            else:
                self.frame_idx = 0   # neutral

    # ── Collision rect ───────────────────────────────────────────────
    @property
    def rect(self) -> pygame.Rect:
        w = CHAR_W * len(self.FRAMES[0])
        h = CHAR_H
        return pygame.Rect(self.x - w // 2, int(self.y) - h // 2, w, h)

    # ── Draw ─────────────────────────────────────────────────────────
    def draw(self, surface, font):
        char = self.FRAMES[self.frame_idx]
        cx, cy = self.x, int(self.y)

        # Shadow
        sh = font.render(char, True, (0, 0, 0))
        surface.blit(sh, (cx - sh.get_width() // 2 + 2,
                          cy - sh.get_height() // 2 + 2))

        # Main body (yellow)
        body = font.render(char, True, BIRD_Y)
        surface.blit(body, (cx - body.get_width() // 2,
                             cy - body.get_height() // 2))

        # Eyes  –  a small white dot over the `>` beak part
        eye_surf = font.render(".", True, BIRD_W)
        ex = cx - body.get_width() // 2 + CHAR_W + 1
        ey = cy - body.get_height() // 2 + 2
        surface.blit(eye_surf, (ex, ey))


class Pipe:
    BODY_CHAR = "#"
    CAP_CHAR  = "="

    def __init__(self, x: float):
        self.x = x
        # Random gap centre, keeping away from very top / bottom
        gap_centre = random.randint(
            GROUND_H + PIPE_GAP // 2 + 30,
            WIN_H - GROUND_H - PIPE_GAP // 2 - 30
        )
        self.top_y    = gap_centre - PIPE_GAP // 2   # y where top pipe ends
        self.bottom_y = gap_centre + PIPE_GAP // 2   # y where bottom pipe starts
        self.scored   = False                         # score claimed?

    # ── Pixel rects for collision ─────────────────────────────────────
    @property
    def top_rect(self) -> pygame.Rect:
        w = PIPE_COLS * CHAR_W
        return pygame.Rect(int(self.x), 0, w, self.top_y)

    @property
    def bottom_rect(self) -> pygame.Rect:
        w = PIPE_COLS * CHAR_W
        return pygame.Rect(int(self.x), self.bottom_y,
                           w, WIN_H - self.bottom_y)

    def update(self):
        self.x -= PIPE_SPEED

    def offscreen(self) -> bool:
        return self.x + PIPE_COLS * CHAR_W < 0

    # ── Draw ─────────────────────────────────────────────────────────
    def _draw_block(self, surface, font, px, py, height, is_top):
        """Draw a solid ASCII block (pipe section)."""
        rows = max(1, height // CHAR_H)
        cap  = (self.CAP_CHAR * PIPE_COLS)[:PIPE_COLS]
        body = (self.BODY_CHAR * PIPE_COLS)[:PIPE_COLS]

        for r in range(rows):
            y = py + r * CHAR_H
            if is_top and r == rows - 1:
                txt, col = cap, PIPE_CAP
            elif (not is_top) and r == 0:
                txt, col = cap, PIPE_CAP
            else:
                # Alternate cols for depth effect
                col = PIPE_C if r % 2 == 0 else PIPE_S
                txt = body
            surf = font.render(txt, True, col)
            surface.blit(surf, (int(self.x), y))

    def draw(self, surface, font):
        # Top pipe
        self._draw_block(surface, font,
                         int(self.x), 0, self.top_y, is_top=True)
        # Bottom pipe
        self._draw_block(surface, font,
                         int(self.x), self.bottom_y,
                         WIN_H - self.bottom_y - GROUND_H, is_top=False)


class Background:
    """Pre-generated static star / cloud layer (scrolls slowly)."""

    def __init__(self):
        self._stars  = self._gen_stars(120)
        self._clouds = self._gen_clouds(8)
        self._scroll = 0.0

    @staticmethod
    def _gen_stars(n):
        chars = [".", "*", "·", "+", "✦"]
        pchars = [".",".",".","*","·"]   # simpler fallback chars
        stars = []
        for _ in range(n):
            x = random.randint(0, WIN_W)
            y = random.randint(0, WIN_H - GROUND_H - 20)
            c = random.choice(pchars)
            b = random.randint(100, 255)
            stars.append((x, y, c, (b, b, min(255, b + 30))))
        return stars

    @staticmethod
    def _gen_clouds(n):
        clouds = []
        shapes = ["( ~~ )", "( ~ )", "(~~~)", "~ ~"]
        for _ in range(n):
            x = random.randint(0, WIN_W)
            y = random.randint(20, WIN_H // 2 - 40)
            s = random.choice(shapes)
            clouds.append([x, y, s])
        return clouds

    def update(self):
        self._scroll += 0.4
        if self._scroll >= WIN_W:
            self._scroll = 0.0
        for c in self._clouds:
            c[0] -= 0.5
            if c[0] < -80:
                c[0] = WIN_W + 40
                c[1] = random.randint(20, WIN_H // 2 - 40)

    def draw(self, surface, font_small, font_cloud):
        surface.fill(SKY)
        # Stars
        for (x, y, ch, col) in self._stars:
            s = font_small.render(ch, True, col)
            surface.blit(s, (x, y))
        # Clouds
        for (x, y, txt) in self._clouds:
            sh = font_cloud.render(txt, True, (30, 40, 70))
            surface.blit(sh, (int(x) + 2, y + 2))
            s  = font_cloud.render(txt, True, CLOUD_C)
            surface.blit(s,  (int(x), y))


class Ground:
    CHARS = "~≈~≈~≈~≈"   # wave-like ground pattern

    def __init__(self):
        self._offset = 0.0

    def update(self):
        self._offset = (self._offset + PIPE_SPEED) % (CHAR_W * len(self.CHARS))

    def draw(self, surface, font):
        y_top  = WIN_H - GROUND_H
        y_mid  = y_top + CHAR_H
        # dark fill below
        pygame.draw.rect(surface, GROUND_C, (0, y_top, WIN_W, GROUND_H))
        # top decorative row
        cols_needed = WIN_W // CHAR_W + 2
        row = (self.CHARS * (cols_needed // len(self.CHARS) + 2))
        x = -int(self._offset)
        surf1 = font.render(row, True, GROUND_L)
        surface.blit(surf1, (x, y_top))
        surf2 = font.render(row, True, GROUND_C)
        surface.blit(surf2, (x, y_mid))


# ══════════════════════════════════════════════════════════════════════
#  HUD
# ══════════════════════════════════════════════════════════════════════

def draw_hud(surface, font_big, font_small, score: int, best: int):
    # Score  (top centre)
    sc_txt  = f"[ {score:04d} ]"
    sc_surf = font_big.render(sc_txt, True, SCORE_C)
    sc_rect = sc_surf.get_rect(centerx=WIN_W // 2, top=12)
    # Shadow
    sh = font_big.render(sc_txt, True, (0, 0, 0))
    surface.blit(sh, sc_rect.move(2, 2))
    surface.blit(sc_surf, sc_rect)

    # Best (top right)
    best_txt  = f"BEST {best:04d}"
    best_surf = font_small.render(best_txt, True, DIM)
    surface.blit(best_surf, (WIN_W - best_surf.get_width() - 12, 14))

    # Controls hint (bottom left)
    hint = font_small.render("[SPACE] / [UP] = flap    [ESC] = quit", True, DIM)
    surface.blit(hint, (10, WIN_H - GROUND_H - hint.get_height() - 4))


def draw_countdown(surface, font_big, font_small, count: int):
    """Flash a countdown before the bird is released."""
    if count <= 0:
        return
    overlay = pygame.Surface((WIN_W, WIN_H), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 80))
    surface.blit(overlay, (0, 0))

    msg = ["3", "2", "1", "GO!"][max(0, 3 - count)]
    col = [DANGER_C, (255, 165, 0), SCORE_C, CYAN][max(0, 3 - count)]
    big = font_big.render(msg, True, col)
    rect = big.get_rect(center=(WIN_W // 2, WIN_H // 2))
    shadow = font_big.render(msg, True, (0, 0, 0))
    surface.blit(shadow, rect.move(3, 3))
    surface.blit(big, rect)

    sub = font_small.render("press  SPACE / UP  to start flapping", True, DIM)
    surface.blit(sub, sub.get_rect(centerx=WIN_W // 2, top=rect.bottom + 14))


def draw_flash(surface, alpha: int):
    """White flash on collision."""
    if alpha <= 0:
        return
    fl = pygame.Surface((WIN_W, WIN_H))
    fl.set_alpha(min(255, alpha))
    fl.fill((255, 255, 255))
    surface.blit(fl, (0, 0))


# ══════════════════════════════════════════════════════════════════════
#  MAIN  PYGAME  GAME  LOOP
# ══════════════════════════════════════════════════════════════════════

def run_game(best: int) -> tuple[str, int]:
    """
    Run one round of the pygame game.
    Returns  (action, last_score, new_best)
    action = 'gameover' or 'quit'
    """
    pygame.init()
    screen = pygame.display.set_mode((WIN_W, WIN_H))
    pygame.display.set_caption("Flappy Bird  –  ASCII Edition")
    clock  = pygame.time.Clock()

    # ── Fonts ─────────────────────────────────────────────────────────
    mono        = pygame.font.SysFont("Courier New", CHAR_H,    bold=True)
    mono_small  = pygame.font.SysFont("Courier New", 13,        bold=False)
    mono_cloud  = pygame.font.SysFont("Courier New", 16,        bold=False)
    mono_big    = pygame.font.SysFont("Courier New", 34,        bold=True)
    mono_score  = pygame.font.SysFont("Courier New", CHAR_H,    bold=True)

    # ── Objects ───────────────────────────────────────────────────────
    bg     = Background()
    ground = Ground()
    bird   = Bird()
    pipes  : list[Pipe] = []

    score       = 0
    frame_count = 0
    state       = "countdown"   # countdown | playing | dead
    countdown   = 3 * FPS       # 3-second countdown
    flash_alpha = 0
    dead_timer  = 0             # how long since death

    def spawn_pipe():
        pipes.append(Pipe(float(WIN_W + 10)))

    # Pre-spawn first pipe slightly sooner
    spawn_pipe()
    next_spawn = SPAWN_EVERY

    # ── Main loop ─────────────────────────────────────────────────────
    running = True
    while running:
        dt = clock.tick(FPS)

        # ── Events ────────────────────────────────────────────────────
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return "quit", score, best

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return "quit", score, best

                flap_keys = (pygame.K_SPACE, pygame.K_UP, pygame.K_w)
                if event.key in flap_keys:
                    if state == "countdown":
                        state = "playing"
                    if state == "playing":
                        bird.flap()

        # ── Logic ─────────────────────────────────────────────────────
        bg.update()

        if state == "countdown":
            countdown -= 1
            if countdown <= 0:
                state = "playing"

        elif state == "playing":
            bird.update()
            ground.update()
            frame_count += 1

            # Spawn pipes
            next_spawn -= 1
            if next_spawn <= 0:
                spawn_pipe()
                next_spawn = SPAWN_EVERY

            # Move + score pipes
            for p in pipes:
                p.update()
                if not p.scored and p.x + PIPE_COLS * CHAR_W < bird.x:
                    p.scored = True
                    score += 1
            pipes = [p for p in pipes if not p.offscreen()]

            # Collision: ground / ceiling
            if bird.y + CHAR_H // 2 >= WIN_H - GROUND_H or bird.y < 0:
                state      = "dead"
                flash_alpha = 220
                dead_timer  = 0
                bird.alive  = False

            # Collision: pipes (shrink bird rect slightly for fairness)
            br = bird.rect.inflate(-4, -4)
            for p in pipes:
                if br.colliderect(p.top_rect) or br.colliderect(p.bottom_rect):
                    state       = "dead"
                    flash_alpha = 220
                    dead_timer  = 0
                    bird.alive  = False
                    break

        elif state == "dead":
            dead_timer += 1
            flash_alpha = max(0, flash_alpha - 12)
            # After 1.6 s auto-exit to game-over screen
            if dead_timer >= int(FPS * 1.6):
                best = max(best, score)
                pygame.quit()
                return "gameover", score, best

        # ── Draw ──────────────────────────────────────────────────────
        bg.draw(screen, mono_small, mono_cloud)

        for pipe in pipes:
            pipe.draw(screen, mono_score)

        ground.draw(screen, mono)
        bird.draw(screen, mono)

        draw_hud(screen, mono_big, mono_small, score, best)
        draw_countdown(screen, mono_big, mono_small,
                       countdown // FPS + (1 if countdown % FPS else 0)
                       if state == "countdown" else 0)
        draw_flash(screen, flash_alpha)

        # Dead overlay
        if state == "dead":
            ov = pygame.Surface((WIN_W, WIN_H), pygame.SRCALPHA)
            ov.fill((0, 0, 0, min(160, dead_timer * 4)))
            screen.blit(ov, (0, 0))
            txt = mono_big.render("x_x  you crashed", True, DANGER_C)
            screen.blit(txt, txt.get_rect(center=(WIN_W // 2, WIN_H // 2 - 20)))
            sub = mono_small.render(f"Score: {score}", True, SCORE_C)
            screen.blit(sub, sub.get_rect(center=(WIN_W // 2, WIN_H // 2 + 24)))

        pygame.display.flip()

    pygame.quit()
    return "quit", score, best


# ══════════════════════════════════════════════════════════════════════
#  ENTRY  POINT
# ══════════════════════════════════════════════════════════════════════

def main():
    best = 0

    # Show start screen
    if not show_start_screen():
        sys.exit(0)

    while True:
        action, last_score, best = run_game(best)

        if action == "quit":
            sys.exit(0)

        # action == "gameover"
        choice = show_gameover_screen(score=last_score, best=best)
        if choice == "quit":
            sys.exit(0)
        # choice == "play"  → loop back and run again


if __name__ == "__main__":
    main()
