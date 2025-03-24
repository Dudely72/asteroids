from circleshape import *
from player import *
from constants import *
import random
from shoot import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        old_radius = self.radius
        random_angle = random.uniform(20, 50)
        vector_one = self.velocity.rotate(random_angle)
        vector_two = self.velocity.rotate(-random_angle)
        new_radius = old_radius - ASTEROID_MIN_RADIUS
        old_x = self.position.x
        old_y = self.position.y
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            asteroid1 = Asteroid(old_x, old_y, new_radius)
            asteroid2 = Asteroid(old_x, old_y, new_radius)
            asteroid1.velocity = vector_one * 1.2
            asteroid2.velocity = vector_two * 1.2

    def explode(self):
        self.split()
        random_angle_blast = random.uniform(0,360)
        blast1 = Burst(self.position.x, self.position.y, SHOT_RADIUS)
        blast2 = Burst(self.position.x, self.position.y, SHOT_RADIUS)
        blast3 = Burst(self.position.x, self.position.y, SHOT_RADIUS)
        blast4 = Burst(self.position.x, self.position.y, SHOT_RADIUS)
        blast1_vector = self.velocity.rotate(random_angle_blast)
        blast2_vector = self.velocity.rotate(-random_angle_blast)
        blast3_vector = self.velocity.rotate(random_angle_blast / 2)
        blast4_vector = self.velocity.rotate(-random_angle_blast / 2)
        blast1.velocity = blast1_vector * 2
        blast2.velocity = blast2_vector * 2
        blast3.velocity = blast3_vector * 2
        blast4.velocity = blast4_vector * 2
        






        