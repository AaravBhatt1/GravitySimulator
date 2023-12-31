import pygame
from object import Object

# Initialize Pygame
pygame.init()

# Set screen dimensions
screenWidth = 1500
screenHeight = 1000
screen = pygame.display.set_mode((screenWidth, screenHeight))

# Set FPS
FPS = 50
# Set game title
pygame.display.set_caption("My Pygame Game")

# Set up game clock
clock = pygame.time.Clock()

# Physics constants
elasticity = 0.7

# Game variables
objectGroup = pygame.sprite.Group()
# This generates the objects
planet = Object(
    x=screenWidth // 2,
    y=screenHeight // 2,
    mass=200,
    xVel=0,
    yVel=0,
)
objectGroup.add(planet)
planet = Object(
    x=screenWidth // 2 + 150,
    y=screenHeight // 2,
    mass=8,
    xVel=0,
    yVel=16,
)
objectGroup.add(planet)
planet = Object(
    x=screenWidth // 2 - 250,
    y=screenHeight // 2,
    mass=3.5,
    xVel=0,
    yVel=12,
)
objectGroup.add(planet)
planet = Object(
    x=screenWidth // 2 - 200,
    y=screenHeight // 2,
    mass=0.8,
    xVel=3,
    yVel=16,
)
objectGroup.add(planet)
planet = Object(
    x=screenWidth // 2,
    y=screenHeight // 2 - 200,
    mass=4,
    xVel=10,
    yVel=-3,
)
objectGroup.add(planet)

# Main game loop
running = True

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic
    # Adds Gravity
    for object in objectGroup:
        object.adjustAcceleration(objectGroup)
    # Makes objects move
    objectGroup.update()
    # Deals with collisions
    for object1 in objectGroup:
        for object2 in objectGroup:
            if object1 == object2:
                continue
            if object1.rect.colliderect(object2.rect):
                # Removes collided objects
                objectGroup.remove([object1, object2])

                # Adds a new one
                newMass = object1.mass + object2.mass
                newXVel = (
                    elasticity
                    * (object1.mass * object1.xVel + object2.mass * object2.xVel)
                    / newMass
                )
                newYVel = (
                    elasticity
                    * (object1.mass * object1.yVel + object2.mass * object2.yVel)
                    / newMass
                )
                if object1.mass > object2.mass:
                    color = object1.color
                else:
                    color = object2.color
                objectGroup.add(
                    Object(
                        mass=newMass,
                        x=object1.rect.centerx,
                        y=object1.rect.centery,
                        xVel=newXVel,
                        yVel=newYVel,
                        color=color,
                    )
                )

    # Draw graphics
    screen.fill("black")  # Fill the screen with black

    # Drawing objects
    for object in objectGroup:
        if (-object.radius < object.rect.centerx < screenWidth + object.radius) or (
            -object.radius < object.rect.centery < screenHeight + object.radius
        ):
            screen.blit(object.image, object.rect)

    # Update display
    pygame.display.update()

    # Limit frames per second
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
