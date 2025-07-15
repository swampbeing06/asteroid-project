from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, center=self.position, radius=SHOT_RADIUS, width=2, color="white")

    def update(self, dt):
        self.position += self.velocity * dt