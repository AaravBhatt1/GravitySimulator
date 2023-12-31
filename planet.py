import pygame
import random
import math

# Physics Constants
densityConstant = 10
gravityConstant = 160


class Planet(pygame.sprite.Sprite):
    def __init__(self, mass, color=None, x=0, y=0, xVel=0, yVel=0):
        super().__init__()

        self.mass = mass
        self.radius = (
            mass ** (1 / 3) * densityConstant
        )  # Mass is proportional to density

        # Create the circular image surface
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)
        self.image.fill((0, 0, 0, 0))  # Fill with transparent color
        if color == None:
            self.color = "#" + "".join(
                random.choice("0123456789ABCDEF") for j in range(6)
            )
        else:
            self.color = color
        pygame.draw.circle(
            self.image, self.color, (self.radius, self.radius), self.radius
        )

        # Create the rectangle around the image
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.xVel = xVel
        self.yVel = yVel
        self.xAcc = 0
        self.yAcc = 0

    def update(self):
        # Updates the displacement and velocity
        self.rect.centerx += self.xVel
        self.rect.centery += self.yVel
        self.xVel += self.xAcc
        self.yVel += self.yAcc

    def adjustAcceleration(self, allPlanets):
        xForce = 0
        yForce = 0

        for planet in allPlanets:
            changeInX = planet.rect.centerx - self.rect.centerx
            changeInY = planet.rect.centery - self.rect.centery
            distance = (changeInX**2 + changeInY**2) ** 0.5  # This uses Pythagoras
            if distance == 0:
                continue  # Cannot divide by 0 or arctan 0/0
            angle = math.atan2(changeInY, changeInX)

            forceMagnitude = (gravityConstant * self.mass * planet.mass) / (
                distance**2
            )  # Newton's gravity formula
            # Converts the magnitude into a vector
            xForce += forceMagnitude * math.cos(angle)
            yForce += forceMagnitude * math.sin(angle)

        self.xAcc = xForce / self.mass
        self.yAcc = yForce / self.mass

    def shift(self, centX, centY, screenWidth, screenHeight):
        self.rect.centerx = self.rect.centerx - centX + screenWidth // 2
        self.rect.centery = self.rect.centery - centY + screenHeight // 2
