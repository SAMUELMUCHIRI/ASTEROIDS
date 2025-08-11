import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):  
    def __init__(self, x, y ):
        super().__init__(x, y , PLAYER_RADIUS)
        self.rotation = 0
        self.timer=0
    
    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
            
    def draw(self, screen):    
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle() ,2)
    
    def rotate(self,dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        self.timer -= dt
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] | keys[pygame.K_LEFT]:
            self.rotate(-dt)  # Rotate left
        if keys[pygame.K_d] | keys[pygame.K_RIGHT]:
            self.rotate(dt)  # Rotate right
        if keys[pygame.K_w] | keys[pygame.K_UP]:
            self.move(dt)  # Move forward or backward
        if keys[pygame.K_s] | keys[pygame.K_DOWN]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.timer > 0:

                return  # Prevent shooting if cooldown is active
            else:
                self.shoot()
                self.timer = PLAYER_SHOOT_COOLDOWN  # Reset cooldown timer
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def shoot(self):
        shot= Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED

       