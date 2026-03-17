import pygame

from circleshape import CircleShape
from shot import Shot
from constants import (
    INVINCIBILITY_SECONDS,
    LINE_WIDTH,
    PLAYER_RADIUS,
    PLAYER_SHOOT_COOLDOWN_SECONDS,
    PLAYER_SHOOT_SPEED,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
)


class Player(CircleShape):
    def __init__(self, x, y, start_invincible=True):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.invincible = start_invincible
        self.invincible_timer = INVINCIBILITY_SECONDS if start_invincible else 0.0
        self.thrusting = False

    def respawn(self, x, y):
        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.invincible = True
        self.invincible_timer = INVINCIBILITY_SECONDS
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y)
        velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        shot.velocity = velocity

    def update(self, dt):
        self.shot_cooldown_timer = max(0, self.shot_cooldown_timer - dt)
        if self.invincible:
            self.invincible_timer -= dt
            if self.invincible_timer <= 0:
                self.invincible = False
        self.wrap_position()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

        self.thrusting = keys[pygame.K_w]

    def draw(self, screen):
        color = "white" if not self.invincible or int(self.invincible_timer * 10) % 2 == 0 else "gray"
        pygame.draw.polygon(screen, color, self.triangle(), LINE_WIDTH)

        if self.thrusting:
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
            flame_length = self.radius * 1.2
            tip = self.position - forward * (self.radius + flame_length)
            left = self.position - forward * self.radius - right * 0.3
            right_pt = self.position - forward * self.radius + right * 0.3
            flame = [tip, left, right_pt]
            pygame.draw.polygon(screen, "orange", flame, 1)
            inner_tip = self.position - forward * (self.radius + flame_length * 0.6)
            inner_flame = [inner_tip, left, right_pt]
            pygame.draw.polygon(screen, "yellow", inner_flame)
