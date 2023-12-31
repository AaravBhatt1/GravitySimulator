import pygame
from planet import Planet
import sys
import json

# Initialize Pygame
pygame.init()

# Set screen dimensions
screenWidth = 1500
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Set FPS
FPS = 50

# Set game title
pygame.display.set_caption("Gravity Simulator")

# Set up game clock
clock = pygame.time.Clock()

# Physics constants
elasticity = 0.7

# This creates a spriteGroup for the planets and generates them from the file
planetGroup = pygame.sprite.Group()
# This generates the planets
# Todo: raise exception arguments do not exist
planetFilePath = sys.argv[1]
# Todo: raise exception if file format incorrect
with open(planetFilePath, "r") as file:
    planets = json.load(file)["planets"]
    for planet in planets:
        planetGroup.add(
            Planet(
                x=screenWidth // 2 + planet["xPos"],
                y=screenHeight // 2 - planet["yPos"],
                mass=planet["mass"],
                xVel=planet["xVel"],
                yVel=-planet["yVel"],
            )
        )

# Main game loop
running = True
paused = False

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused

    # Game logic
    if paused:
        continue
    # Adds Gravity
    for planet in planetGroup:
        planet.adjustAcceleration(planetGroup)
    # Makes planets move
    planetGroup.update()
    # Deals with collisions
    for planet1 in planetGroup:
        for planet2 in planetGroup:
            if planet1 == planet2:
                continue
            if planet1.rect.colliderect(planet2.rect):
                # Removes collided planets
                planetGroup.remove([planet1, planet2])

                # Adds a new one
                newMass = planet1.mass + planet2.mass
                newXVel = (
                    elasticity
                    * (planet1.mass * planet1.xVel + planet2.mass * planet2.xVel)
                    / newMass
                )
                newYVel = (
                    elasticity
                    * (planet1.mass * planet1.yVel + planet2.mass * planet2.yVel)
                    / newMass
                )
                if planet1.mass > planet2.mass:
                    color = planet1.color
                else:
                    color = planet2.color
                planetGroup.add(
                    Planet(
                        mass=newMass,
                        x=planet1.rect.centerx,
                        y=planet1.rect.centery,
                        xVel=newXVel,
                        yVel=newYVel,
                        color=color,
                    )
                )

    # Draw graphics
    screen.fill("black")  # Fill the screen with black

    # Drawing planets
    for planet in planetGroup:
        if (-planet.radius < planet.rect.centerx < screenWidth + planet.radius) or (
            -planet.radius < planet.rect.centery < screenHeight + planet.radius
        ):
            screen.blit(planet.image, planet.rect)

    # Update display
    pygame.display.update()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
