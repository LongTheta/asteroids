import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from explosion import create_explosion
from highscore import load_high_score, save_high_score
from shot import Shot
from starfield import Starfield
from constants import (
    PLAYER_LIVES,
    SCREEN_HEIGHT,
    SCREEN_WIDTH,
)
from logger import log_event, log_state
from player import Player


def draw_ui(screen, score, lives, paused=False, game_over=False, high_score=0):
    """Draw score, lives, and overlay text."""
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, "white")
    lives_text = font.render(f"Lives: {lives}", True, "white")
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (10, 40))

    if paused:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill("black")
        screen.blit(overlay, (0, 0))
        pause_font = pygame.font.Font(None, 72)
        pause_text = pause_font.render("PAUSED", True, "white")
        pause_rect = pause_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30))
        screen.blit(pause_text, pause_rect)
        hint = font.render("Press P or ESC to resume", True, "gray")
        hint_rect = hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 20))
        screen.blit(hint, hint_rect)

    if game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill("black")
        screen.blit(overlay, (0, 0))
        go_font = pygame.font.Font(None, 72)
        go_text = go_font.render("GAME OVER", True, "white")
        go_rect = go_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 60))
        screen.blit(go_text, go_rect)
        score_font = pygame.font.Font(None, 48)
        final_text = score_font.render(f"Final Score: {score}", True, "white")
        final_rect = final_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(final_text, final_rect)
        if high_score > 0:
            hs_text = score_font.render(f"High Score: {high_score}", True, "gold")
            hs_rect = hs_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 40))
            screen.blit(hs_text, hs_rect)
        hint = font.render("Press R or SPACE to restart", True, "gray")
        hint_rect = hint.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 100))
        screen.blit(hint, hint_rect)


def draw_main_menu(screen, high_score):
    """Draw the main menu."""
    screen.fill("black")
    title_font = pygame.font.Font(None, 96)
    title = title_font.render("ASTEROIDS", True, "white")
    title_rect = title.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
    screen.blit(title, title_rect)

    font = pygame.font.Font(None, 48)
    play_text = font.render("Press ENTER or SPACE to Play", True, "white")
    play_rect = play_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
    screen.blit(play_text, play_rect)

    quit_text = font.render("Press Q to Quit", True, "gray")
    quit_rect = quit_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
    screen.blit(quit_text, quit_rect)

    if high_score > 0:
        hs_font = pygame.font.Font(None, 36)
        hs_text = hs_font.render(f"High Score: {high_score}", True, "gold")
        hs_rect = hs_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 120))
        screen.blit(hs_text, hs_rect)

    controls = pygame.font.Font(None, 28).render(
        "WASD: Move | SPACE: Shoot | P/ESC: Pause",
        True,
        "darkgray",
    )
    controls_rect = controls.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 40))
    screen.blit(controls, controls_rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Asteroids")

    high_score = load_high_score()
    starfield = Starfield()
    explosions = []
    game_state = "menu"  # "menu" | "playing"

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    def init_game():
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()
        explosions.clear()
        Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        AsteroidField()
        return next((s for s in drawable if isinstance(s, Player)), None)

    player = None
    score = 0
    lives = PLAYER_LIVES
    paused = False
    game_over = False

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_state == "menu":
                    if event.key in (pygame.K_RETURN, pygame.K_SPACE):
                        game_state = "playing"
                        player = init_game()
                        score = 0
                        lives = PLAYER_LIVES
                        paused = False
                        game_over = False
                    elif event.key == pygame.K_q:
                        running = False
                elif game_state == "playing":
                    if event.key in (pygame.K_p, pygame.K_ESCAPE) and not game_over:
                        paused = not paused
                    if game_over and event.key in (pygame.K_r, pygame.K_SPACE):
                        game_over = False
                        lives = PLAYER_LIVES
                        score = 0
                        player = init_game()

        if game_state == "menu":
            draw_main_menu(screen, high_score)
            pygame.display.flip()
            continue

        if paused or game_over:
            starfield.draw(screen)
            for sprite in drawable:
                sprite.draw(screen)
            for particle in explosions:
                particle.draw(screen)
            draw_ui(screen, score, lives, paused=paused, game_over=game_over, high_score=high_score)
            pygame.display.flip()
            continue

        updatable.update(dt)

        explosions[:] = [p for p in explosions if p.update(dt)]

        player = next((s for s in drawable if isinstance(s, Player)), None)
        if player and not player.invincible:
            for asteroid in list(asteroids):
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    lives -= 1
                    if lives <= 0:
                        game_over = True
                        high_score = max(high_score, score)
                        save_high_score(high_score)
                    else:
                        player.respawn(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                    break

        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    x, y = asteroid.position.x, asteroid.position.y
                    radius = asteroid.radius
                    score += asteroid.split()
                    shot.kill()
                    explosions.extend(create_explosion(x, y, radius))
                    break

        starfield.draw(screen)
        for sprite in drawable:
            sprite.draw(screen)
        for particle in explosions:
            particle.draw(screen)
        draw_ui(screen, score, lives)
        log_state()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
