"""
    PyGame examples
"""
import pygame
import random

# == Character Class ==
class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # Creates a simple block as sprite
        self.image = pygame.Surface([25, 25])
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
    def draw(self):
        screen.blit(self.image, self.rect)

# == Ghost Class ==
class Ghost(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        sprite = pygame.image.load("sprite.png")
        self.width = 25
        self.height = 25
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# == Character movement with keyboard and mouse input==
def moveCharacterWithKey(chara, event):
    if USE_KEYBOARD and event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            chara.rect.x -= 5
        elif event.key == pygame.K_RIGHT:
            chara.rect.x += 5
        elif event.key == pygame.K_UP:
            chara.rect.y -= 5
        elif event.key == pygame.K_DOWN:
            chara.rect.y += 5

def moveCharacterWithMouse(chara, event):
    if USE_KEYBOARD == False and event.type == pygame.MOUSEMOTION:
        pos = pygame.mouse.get_pos()
        chara.rect.x = pos[0]
        chara.rect.y = pos[1]

# == Makes a sprite group with ghost sprites.
def makeGhosts():
    group = pygame.sprite.Group()
    if MAKE_GROUP:
        random.seed(0)
        for i in range(20):
            x = random.randrange(800)
            y = random.randrange(600)
            ghost = Ghost(x, y)
            group.add(ghost)
    return group

# == Moves each ghost sprite ==
def moveGhosts():
    if GROUP_MOVEMENT == False:
        return
    for ghost in ghosts:
        x = random.randrange(4)
        y = random.randrange(4)
        ghost.rect.x += x - 2
        ghost.rect.y += y - 2

# == Check for collissions ==
def checkCollissions():
    if CHECK_COLLISSIONS:
        collided = pygame.sprite.spritecollide(chara, ghosts, True)
        if len(collided) > 0:
            print(collided)

# == Render text ==
def renderText(screen, text):
    if SHOW_TEXT == False:
        return
    font = pygame.font.SysFont('arial', 24)
    render = font.render(text, True, RED)
    screen.blit(render, (200, 200))


# == CONSTANTS ==
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (128, 0, 0)

# == SETTINGS ==
# Use keyboard controls
USE_KEYBOARD = True
MAKE_GROUP = False
GROUP_MOVEMENT = False
CHECK_COLLISSIONS = False
SHOW_TEXT = False

if __name__ == "__main__":
    pygame.init()
    size = (400, 300)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("PyGame examples")
 
    done = False
    clock = pygame.time.Clock()

    # creates an object for player's character
    chara = Character()

    # creates a set of randomly positioned ghosts and puts them in a sprite group
    ghosts = makeGhosts()

    # Main game loop
    while not done:
        # Mouse, keyboard and quit game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            moveCharacterWithKey(chara, event)
            moveCharacterWithMouse(chara, event)

        # Game logic
        moveGhosts()
        checkCollissions()

        # Rendering
        screen.fill(WHITE)
        renderText(screen, "Hello World!")
        chara.draw()
        ghosts.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
