"""Particle explosion effect when asteroids are destroyed."""
import random

import pygame

from constants import EXPLOSION_PARTICLES


class Particle:
    def __init__(self, x, y, radius):
        angle = random.uniform(0, 360)
        speed = random.uniform(50, 150)
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 1).rotate(angle) * speed
        self.life = 1.0
        self.decay = random.uniform(0.02, 0.05)
        self.radius = max(1, radius * random.uniform(0.2, 0.5))

    def update(self, dt):
        self.position += self.velocity * dt
        self.life -= self.decay
        return self.life > 0

    def draw(self, screen):
        alpha = int(255 * self.life)
        color = (255, min(200, 255 - alpha // 2), min(150, 200 - alpha))
        r = max(1, int(self.radius))
        pygame.draw.circle(screen, color, (int(self.position.x), int(self.position.y)), r)


def create_explosion(x, y, radius):
    """Create explosion particles at position. Returns list of Particle objects."""
    return [Particle(x, y, radius) for _ in range(EXPLOSION_PARTICLES)]
