
import pygame
import copy

# Define some colors
BLACK = (0, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 4
CURR_ROW = 8
time_elapsed_since_last_action = 0
offset = 0
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
currBlock = [3,4,5,6]
for row in range(10):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(10):
        grid[row].append(0)  # Append a cell
 
# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
grid[9][3] = 1
grid[9][4] = 1
grid[9][5] = 1
grid[9][6] = 1

grid[8][3] = 1
grid[8][4] = 1
grid[8][5] = 1
grid[8][6] = 1

lastRowsSquares = [3,4,5,6]

direction = 'f'


# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Fair Tower")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0

def restart():
    global score 
    score = 0
    global grid
    for row in range(10):
        for column in range(10):
            grid[row][column] = 0
    global currBlock
    currBlock = [3,4,5,6]

    grid[9][3] = 1
    grid[9][4] = 1
    grid[9][5] = 1
    grid[9][6] = 1

    # grid[8][3] = 1
    # grid[8][4] = 1
    # grid[8][5] = 1
    # grid[8][6] = 1

    global lastRowsSquares
    lastRowsSquares = [3,4,5,6]
    global direction
    direction = 'f'
    global CURR_ROW
    CURR_ROW = 9



# Initialize pygame
pygame.init()
 
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [255, 255]
screen = pygame.display.set_mode(WINDOW_SIZE)
    

def gameOver():

    loop = True
    font = pygame.font.SysFont("ARIAL", 15)
    text = font.render("Game Over! You scored " + str(score), True, (0, 0, 0))
    textRect = text.get_rect()
    textRect.center = (255/2, 255/2 - 80)
    temp_surface = pygame.Surface(text.get_size())
    temp_surface.fill((192, 192, 192))
    temp_surface.blit(text, (255/2, 255/2 - 100))
    screen.blit(temp_surface, (255/2 - 87, 255/2 - 87))
    screen.blit(text, textRect)
    textRect = text.get_rect()
    textRect.center = (255/2, 255/2 - 80)


    while loop:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                else:
                    restart()
                    loop = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                restart()
                loop = False
            if event.type == pygame.QUIT:
                pygame.quit()
        
        pygame.display.update()
        clock.tick()

 
def forwardMove():
    global grid
    global currBlock
    if currBlock[-1] < 9:
        pastHigh = currBlock[-1]
        grid[CURR_ROW][currBlock[0]] = 0
        currBlock.pop(0)
        currBlock.append(pastHigh + 1)
        grid[CURR_ROW][currBlock[-1]] = 1
        soundObj = pygame.mixer.Sound('sound.wav')
        soundObj.play()
    else:
        global direction
        direction = 'r'

def backwardMove():
    global grid
    global currBlock
    if currBlock[0] > 0:
        pastLow = currBlock[0]
        grid[CURR_ROW][currBlock[-1]] = 0
        currBlock.pop(- 1)
        currBlock.insert(0, pastLow - 1)
        grid[CURR_ROW][currBlock[0]] = 1
        soundObj = pygame.mixer.Sound('sound.wav')
        soundObj.play()
    else:
        global direction
        direction = 'f'
        forwardMove()
# -------- Main Program Loop -----------
while not done:
    dt = clock.tick(60) 
    time_elapsed_since_last_action += dt
    # dt is measured in milliseconds, therefore 250 ms = 0.25 seconds
    if score < 4 :
        speed = 100
    elif score < 6:
        speed = 50
    elif score < 9:
        speed = 35
    else:
        speed = 30
    
    if time_elapsed_since_last_action > speed:
        
        if (direction == 'f'):
            forwardMove()
        if (direction == 'r'):
            backwardMove()
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            pygame.quit()  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.KEYDOWN:
            
            newCurrBlock = copy.deepcopy(list(set(lastRowsSquares).intersection(set(currBlock))))
            fallOffSquares = copy.deepcopy(list(set(currBlock) - set(lastRowsSquares)))
            print(fallOffSquares)
            for x in fallOffSquares:
                grid[CURR_ROW][x] = 0;
            lastRowsSquares = copy.deepcopy(newCurrBlock)
            currBlock = copy.deepcopy(list(newCurrBlock))
            print(len(currBlock))
            if len(currBlock) > 0:
                score +=1
            else:
                print("CurrRow " + str(CURR_ROW))
                for column in range(10):
                    grid[CURR_ROW][column] = 0
                for x in fallOffSquares:
                    print("I should be turning on "+ str(x))
                    grid[CURR_ROW][x] = 1
                    for row in range(10):
                        for column in range(10):
                            color = (47,79,79)
                            if grid[row][column] == 1:
                                color = (100,149,237)
                            pygame.draw.rect(screen,
                                            color,
                                            [(MARGIN + WIDTH) * column + MARGIN,
                                            (MARGIN + HEIGHT) * row + MARGIN,
                                            WIDTH,
                                            HEIGHT])
                    gameOver()
            CURR_ROW -= 1
            if CURR_ROW == -1 :
                for row in range(10):
                    for column in range(10):
                        if row == 9 and column in currBlock:
                            grid[row][column] = 1
                        else:
                            grid[row][column] = 0

                CURR_ROW = 8   
            for x in currBlock:
                grid[CURR_ROW][x] = 1;
                    
 
    # Set the screen background
    screen.fill(BLACK)
 
    # Draw the grid
    for row in range(10):
        for column in range(10):
            color = (47,79,79)
            if grid[row][column] == 1:
                color = (100,149,237)
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
