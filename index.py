# import pygame
# import sys
# import random

# pygame.init()

# width = 400
# height = 500
# pygame.display.set_caption('Simple Stacking Game')
# display = pygame.display.set_mode((width, height))
# clock = pygame.time.Clock()

# background = (23, 32, 42)

# white = (236, 240, 241)


# color = [(31, 40, 120), (38, 49, 148), (46, 58, 176), (53, 67, 203), (60, 76, 231), (99, 112, 236), (138, 148, 241), (177, 183, 245), (216, 219, 250), (236, 237, 253),
#             (231, 249, 254), (207, 243, 252), (159, 231, 249), (111, 220, 247), (63, 208, 244), (15, 196, 241), (13, 172, 212), (11, 149, 183), (10, 125, 154), (8, 102, 125),
#          (9, 81, 126), (12, 100, 156), (14, 119, 185), (30, 111, 202), (16, 137, 214), (18, 156, 243), (65, 176, 245), (113, 196, 248),(160, 215, 250), (208, 235, 253), (231, 245, 254),
#          (232, 246, 243), (162, 217, 206), (162, 217, 206),
#          (115, 198, 182), (69, 179, 157), (22, 160, 133),
#          (19, 141, 117), (17, 122, 101), (14, 102, 85),
#          (11, 83, 69),
#          (21, 67, 96), (26, 82, 118), (31, 97, 141),
#         (36, 113, 163), (41, 128, 185), (84, 153, 199),
#         (127, 179, 213), (169, 204, 227), (212, 230, 241),
#         (234, 242, 248),
#          (230, 238, 251), (204, 221, 246), (153, 187, 237),
#          (112, 152, 229), (51, 118, 220), (0, 84, 211),
#          (0, 74, 186), (0, 64, 160), (0, 54, 135),
#          (0, 44, 110)
#          ]

# colorIndex = 0

# brickH = 10
# brickW = 100

# score = 0
# speed = 3


# # Define some colors
# BLACK = (0, 0, 0)
# WHITE = (255, 255, 255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
 
# # This sets the WIDTH and HEIGHT of each grid location
# WIDTH = 20
# HEIGHT = 20
 
# # This sets the margin between each cell
# MARGIN = 5
 
# # Create a 2 dimensional array. A two dimensional
# # array is simply a list of lists.
# grid = []
# for row in range(10):
#     # Add an empty array that will hold each cell
#     # in this row
#     grid.append([])
#     for column in range(10):
#         grid[row].append(0)  # Append a cell
 
# # Set row 1, cell 5 to one. (Remember rows and
# # column numbers start at zero.)
# grid[1][5] = 1


# class Brick:
#     def __init__(self, x, y, color, speed):
#         self.x = x
#         self.y = y
#         self.w = brickW
#         self.h = brickH
#         self.color = color
#         self.speed = speed

#     def draw(self):
#         for row in range(10):
#             for column in range(10):
#                 color = WHITE
#                 if grid[row][column] == 1:
#                     color = GREEN
#                 pygame.draw.rect(display,
#                                 color,
#                                 [(MARGIN + WIDTH) * column + MARGIN,
#                                 (MARGIN + HEIGHT) * row + MARGIN,
#                                 WIDTH,
#                                 HEIGHT])

#     def move(self):
#         self.x += self.speed
#         if self.x > width:
#             self.speed *= -1
#         if self.x + self.w < 1:
#             self.speed *= -1



# class Stack:
#     def __init__(self):
#         global colorIndex
#         self.stack = []
#         self.initSize = 25
#         for i in range(self.initSize):
#             newBrick = Brick(width/2 - brickW/2, height - (i + 1)*brickH, color[colorIndex], 0)
#             colorIndex += 1
#             self.stack.append(newBrick)

#     def show(self):
#         for i in range(self.initSize):
#             self.stack[i].draw()

#     def move(self):
#         for i in range(self.initSize):
#             self.stack[i].move()

#     def addNewBrick(self):
#         global colorIndex, speed

#         if colorIndex >= len(color):
#             colorIndex = 0
        
#         y = self.peek().y
#         if score > 50:
#             speed += 0
#         elif score%5 == 0:
#             speed += 1
        
#         newBrick = Brick(width, y - brickH, color[colorIndex], speed)
#         colorIndex += 1
#         self.initSize += 1
#         self.stack.append(newBrick)
        
#     def peek(self):
#         return self.stack[self.initSize - 1]

#     def pushToStack(self):
#         global brickW, score
#         b = self.stack[self.initSize - 2]
#         b2 = self.stack[self.initSize - 1]
#         if b2.x <= b.x and not (b2.x + b2.w < b.x):
#             self.stack[self.initSize - 1].w = self.stack[self.initSize - 1].x + self.stack[self.initSize - 1].w - b.x
#             self.stack[self.initSize - 1].x = b.x
#             if self.stack[self.initSize - 1].w > b.w:
#                 self.stack[self.initSize - 1].w = b.w
#             self.stack[self.initSize - 1].speed = 0
#             score += 1
#         elif b.x <= b2.x <= b.x + b.w:
#             self.stack[self.initSize - 1].w = b.x + b.w - b2.x
#             self.stack[self.initSize - 1].speed = 0
#             score += 1
#         else:
#             gameOver()
#         for i in range(self.initSize):
#             self.stack[i].y += brickH

#         brickW = self.stack[self.initSize - 1].w


# def gameOver():
#     loop = True

#     font = pygame.font.SysFont("ARIAL", 60)
#     text = font.render("Game Over!", True, white)

#     textRect = text.get_rect()
#     textRect.center = (width/2, height/2 - 80)

#     while loop:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 close()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     close()
#                 if event.key == pygame.K_r:
#                     gameLoop()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 gameLoop()
#         display.blit(text, textRect)
        
#         pygame.display.update()
#         clock.tick()


# def showScore():
#     font = pygame.font.SysFont("ARIAL", 30)
#     text = font.render("Score: " + str(score), True, white)
#     display.blit(text, (10, 10))



# def close():
#     pygame.quit()
#     sys.exit()


# def gameLoop():
#     global brickW, brickH, score, colorIndex, speed
#     loop = True

#     brickH = 10
#     brickW = 100
#     colorIndex = 0
#     speed = 3

#     score = 0

#     stack = Stack()
#     stack.addNewBrick()

#     while loop:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 close()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_q:
#                     close()
#                 if event.key == pygame.K_r:
#                     gameLoop()
#                 if event.key == pygame.K_SPACE:
#                     stack.pushToStack()
#                     stack.addNewBrick()

                

#         display.fill(background)

#         stack.move()
#         stack.show()

#         showScore()
        
#         pygame.display.update()
#         clock.tick(60)

# gameLoop()

"""
 Example program to show using an array to back a grid on-screen.
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/mdTeqiWyFnc
"""
import pygame
import copy

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

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


def gameOver():
    loop = True
    done = True

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
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                loop = False
        
        pygame.display.update()
        clock.tick()

 
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
            if currBlock[len(currBlock) - 1] < 9:
                pastHigh = currBlock[-1]
                grid[CURR_ROW][currBlock[0]] = 0
                currBlock.pop(0)
                currBlock.append(pastHigh + 1)
                grid[CURR_ROW][currBlock[len(currBlock) - 1]] = 1
                soundObj = pygame.mixer.Sound('sound.wav')
                soundObj.play()

            else:
                direction = 'r'

        if (direction == 'r'):
            if currBlock[0] > 0:
                pastLow = currBlock[0]
                grid[CURR_ROW][currBlock[len(currBlock) - 1]] = 0
                currBlock.pop(len(currBlock) - 1)
                currBlock.insert(0, pastLow - 1)
                grid[CURR_ROW][currBlock[0]] = 1
                soundObj = pygame.mixer.Sound('sound.wav')
                soundObj.play()
            else:
                direction = 'f'
            
        time_elapsed_since_last_action = 0 # reset it to 0 so you can count again
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # try: 
            newCurrBlock = copy.deepcopy(list(set(lastRowsSquares).intersection(currBlock)))
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
    
            # except: 
            #     done = True

            
            
        #     # User clicks the mouse. Get the position
        #     pos = pygame.mouse.get_pos()
        #     # Change the x/y screen coordinates to grid coordinates
        #     column = pos[0] // (WIDTH + MARGIN)
        #     row = pos[1] // (HEIGHT + MARGIN)
        #     # Set that location to one
        #     grid[row][column] = 1
        #     print("Click ", pos, "Grid coordinates: ", row, column)
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_SPACE:
        #         CURR_ROW += 1
        #         for x in range[0,len(currBlock) - 1]:
        #             grid[CURR_ROW][x] = 1;

                    
 
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
