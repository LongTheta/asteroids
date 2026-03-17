import pygame

from circleshape import CircleShape
from constants import LINE_WIDTH, SHOT_LIFETIME_SECONDS, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.lifetime = SHOT_LIFETIME_SECONDS

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        self.position += self.velocity * dt
        self.lifetime -= dt
        if self.lifetime <= 0:
            self.kill()
        else:
            self.wrap_position()
