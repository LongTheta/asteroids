import sys

import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_event, log_state
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable,)

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    running = True
    while running:
        dt = clock.tick(60) / 1000.0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updatable.update(dt)

        player = next((s for s in drawable if isinstance(s, Player)), None)
        if player:
            for asteroid in asteroids:
                if asteroid.collides_with(player):
                    log_event("player_hit")
                    print("Game over!")
                    sys.exit()

        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.kill()
                    shot.kill()
                    break

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)

        log_state()
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
