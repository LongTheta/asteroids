"""Animated starfield background."""
import random

import pygame

from constants import SCREEN_HEIGHT, SCREEN_WIDTH, STAR_COUNT


class Starfield:
    def __init__(self):
        self.stars = [
            (
                random.uniform(0, SCREEN_WIDTH),
                random.uniform(0, SCREEN_HEIGHT),
                random.uniform(0.5, 2),
                random.uniform(0.2, 1.0),
            )
            for _ in range(STAR_COUNT)
        ]

    def draw(self, screen):
        for x, y, size, brightness in self.stars:
            alpha = int(255 * brightness)
            color = (alpha, alpha, min(255, alpha + 50))
            r = max(1, int(size))
            pygame.draw.circle(screen, color, (int(x), int(y)), r)
