import pygame
import math
import random

pygame.init()
data = [
    ["A person who develops code", "DEVELOPER"],
    ["Someone who protects people with law", "POLICE"],
    ["A person who teaches students", "TEACHER"],
    ["A medical professional who treats patients", "DOCTOR"],
    ["A person who builds structures", "ENGINEER"],
    ["Someone who delivers mail", "POSTMAN"],
    ["A person who cooks in a restaurant", "CHEF"],
    ["An individual who drives a vehicle", "DRIVER"],
    ["A person who writes books", "AUTHOR"],
    ["Someone who performs on stage", "ACTOR"],
    ["A device used to call someone", "PHONE"],
    ["An animal known as the king of the jungle", "LION"],
    ["A structure where people live", "HOUSE"],
    ["A celestial body that provides light during the day", "SUN"],
    ["An object used to write", "PEN"],
    ["A vehicle that runs on tracks", "TRAIN"],
    ["A fruit known for keeping the doctor away", "APPLE"],
    ["A place where books are kept", "LIBRARY"],
    ["A machine used for computing tasks", "COMPUTER"],
    ["A sport played with a bat and ball", "CRICKET"],
    ["A room where food is prepared", "KITCHEN"],
    ["A tool used to cut paper", "SCISSORS"],
    ["A liquid essential for life", "WATER"],
    ["The largest mammal in the world", "WHALE"],
    ["A vehicle with two wheels", "BICYCLE"],
    ["An insect that makes honey", "BEE"],
    ["The capital city of France", "PARIS"],
    ["A metal used to make coins", "SILVER"],
    ["A season known for falling leaves", "AUTUMN"],
    ["A person who paints pictures", "ARTIST"],
]
# Constants
WIDTH, HEIGHT = 800, 500
FPS = 60
HANGMAN_STATUS = 0
WHEAT = (245, 222, 179)
BLACK = (0, 0, 0)
RADIUS = 20
A = 65
GAP = 15
number = random.choice(data)
WORD = number[1]
GUESSED = []
print(number)
print(data[0][1])

# Font Paths
FONT_PATH_1 = "hangman/Poppins-SemiBold.ttf"
FONT_PATH_2 = "hangman/Oswald-VariableFont_wght.ttf"

# Font Loading
Fonts = pygame.font.Font(FONT_PATH_1, 30)
Fonts2 = pygame.font.Font(FONT_PATH_2, 60)

# Setup Letters (A-Z)
letters = []
startx, starty = round((WIDTH - ((RADIUS * 2) + GAP) * 13) / 2), 400
for i in range(26):
    x = startx + (GAP * 2) + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

# Setup Game Window
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HangMan Game")

# Load Hangman Images
images = []
for i in range(7):
    try:
        img_path = f"hangman/hangman{i}.png"
        images.append(pygame.image.load(img_path))
    except pygame.error as e:
        print(f"Error loading image {img_path}: {e}")
        pygame.quit()
        exit()

# Clock for controlling frame rate
clock = pygame.time.Clock()


# Function to draw the game window
def draw():
    window.fill(WHEAT)

    display_question = number[0]

    # Display the word with guessed letters
    display_word = ""
    for letter in WORD:
        if letter in GUESSED:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = Fonts2.render(display_word, True, BLACK)
    text2 = Fonts.render(display_question, True, BLACK)
    window.blit(text, (WIDTH // 2 - text.get_width() // 2, 250))
    window.blit(text2, (300, 50))

    # Draw the alphabet buttons
    for x, y, alpha, state in letters:
        if state:
            pygame.draw.circle(window, BLACK, (x, y), RADIUS, 3)
            text = Fonts.render(alpha, True, BLACK)
            window.blit(text, (x - text.get_width() // 2, y - text.get_height() // 2))

    # Draw the hangman image
    window.blit(images[HANGMAN_STATUS], (50, 100))

    pygame.display.update()


# Main game loop
run = True
while run:
    clock.tick(FPS)
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos_x, pos_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, alpha, state = letter
                if state:
                    # Check if the mouse click is within the button radius
                    dist = math.sqrt((x - pos_x) ** 2 + (y - pos_y) ** 2)
                    if dist < RADIUS:
                        letter[3] = False  # Mark the letter as used
                        GUESSED.append(alpha)
                        if alpha not in WORD:
                            HANGMAN_STATUS += 1
                            if HANGMAN_STATUS == 6:  # Lose condition
                                window.fill(WHEAT)
                                pygame.display.update()
                                text = Fonts2.render("You Lost!", True, BLACK)
                                window.blit(
                                    text, (WIDTH // 2 - text.get_width() // 2, 300)
                                )
                                pygame.display.update()
                                pygame.time.delay(3000)
                                run = False
                        break

    # Check win condition
    if all(letter in GUESSED for letter in WORD):
        window.fill(WHEAT)
        pygame.display.update()
        text = Fonts2.render("You Won!", True, BLACK)
        window.blit(text, (WIDTH // 2 - text.get_width() // 2, 300))
        pygame.display.update()
        pygame.time.delay(2000)
        break


pygame.quit()
