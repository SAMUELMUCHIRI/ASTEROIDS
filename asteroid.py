import pygame
from circleshape import CircleShape
from constants import *
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()  # Remove the asteroid
        if self.radius <= ASTEROID_MIN_RADIUS:
            return  # Don't split if the asteroid is too small
        else:
            rn_angle=random.uniform(20, 50)
            v1=self.velocity.rotate(rn_angle)
            v2=self.velocity.rotate(-rn_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid(self.position.x, self.position.y, new_radius).velocity = v1 *1.2

            Asteroid(self.position.x, self.position.y, new_radius).velocity = v2 *1.2


    


