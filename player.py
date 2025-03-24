from circleshape import *
from constants import *
from shoot import *


class Player(CircleShape):          #player looks like triangle, actually a circle hitbox
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.x = x
        self.y = y
        self.timer = 0


    # in the player class
    def triangle(self):             #describes player triangle
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):         #draws player
        pygame.draw.polygon(screen, "white", self.triangle(), 2)

    def rotate(self, dt):           #rotate formula
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):           #updates player on key presses
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-1 * dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-1 * dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
        self.timer -= dt
    
    def move(self, dt):             #formula for moving
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            self.timer = PLAYER_SHOOT_COOLDOWN
            shoot = Shot(self.position.x, self.position.y, SHOT_RADIUS)
            shoot.velocity = pygame.Vector2(0, 1).rotate(self.rotation)
            shoot.velocity *= PLAYER_SHOOT_SPEED
