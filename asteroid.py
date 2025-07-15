import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, center=self.position, radius=self.radius, width=2, color="white")

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)
        split_angle_one = self.velocity.rotate(random_angle)
        split_angle_two = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        split_asteroid_one = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_two = Asteroid(self.position.x, self.position.y, new_radius)
        split_asteroid_one.velocity = split_angle_one * 1.2
        split_asteroid_two.velocity = split_angle_two * 1.2


