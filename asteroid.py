import random

import pygame

from circleshape import CircleShape
from constants import (
    ASTEROID_MIN_RADIUS,
    ASTEROID_POINTS_LARGE,
    ASTEROID_POINTS_MEDIUM,
    ASTEROID_POINTS_SMALL,
    LINE_WIDTH,
)
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def get_points(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            return ASTEROID_POINTS_SMALL
        elif self.radius <= ASTEROID_MIN_RADIUS * 2:
            return ASTEROID_POINTS_MEDIUM
        return ASTEROID_POINTS_LARGE

    def split(self):
        points = self.get_points()
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return points
        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        velocity1 = self.velocity.rotate(angle) * 1.2
        velocity2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = velocity1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = velocity2
        return points

    def update(self, dt):
        self.position += self.velocity * dt
        self.wrap_position()
