import sys
import pygame

# Initializing
pygame.init()

# Setting Clock
clock = pygame.time.Clock()

# Create the screen
screen_width = 1070
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("No Retreat")

# Initialize constants
font = pygame.font.SysFont("comicsansms", 30)
smallfont = pygame.font.SysFont("comicsansms", 14)
slategrey = (112, 128, 144)
lightgrey = (165, 175, 185)
blackish = (10, 10, 10)

# Load images
no_retreat = pygame.image.load("No retreat Icon banner long.png")
no_retreat = pygame.transform.scale(no_retreat, (1070, 720))

# Function to create a button
def create_new_game_button(msg, x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            first_level()
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))
    # Start button text
    startbuttontext = smallfont.render(msg, True, blackish)
    screen.blit(startbuttontext, (int(890 + (width / 2)), int(y + (y / 2))))

def create_load_game_button(msg, x, y, width, height, hovercolor, defaultcolor):
    mouse = pygame.mouse.get_pos()
    # Mouse get pressed can run without an integer, but needs a 3 or 5 to indicate how many buttons
    click = pygame.mouse.get_pressed(3)
    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(screen, hovercolor, (x, y, width, height))
        if click[0] == 1:
            load_game()
    else:
        pygame.draw.rect(screen, defaultcolor, (x, y, width, height))
    # Start button text
    loadbuttontext = smallfont.render(msg, True, blackish)
    screen.blit(loadbuttontext, (int(890 + (width / 2)), int(22 + (y / 2))))

# Start menu returns true until we click the Start button
def start_menu():
    startText = font.render("", True, slategrey)

    while True:
        screen.fill((0, 0, 0))

        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        # buttons (left, top, width, height)
        create_new_game_button("Start Game!", screen_width - 130, 7, 125, 26, lightgrey, slategrey)
        create_load_game_button("Load Game!", screen_width - 130, 35, 125, 26, lightgrey, slategrey)
        screen.blit(no_retreat, (1, 40))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu()

        pygame.display.update()
        clock.tick(15)
        return True

def load_game():
    startText = font.render("Load Game", True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                start_menu()

        pygame.display.update()
        clock.tick(15)

def first_level():
    startText = font.render("Starting Town", True, slategrey)

    while True:
        screen.fill((0, 0, 0))
        screen.blit(startText, ((screen_width - startText.get_width()) / 2, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        clock.tick(15)


# Game loop
while True:
    start_menu()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(15)