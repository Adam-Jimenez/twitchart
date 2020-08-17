from random import randrange
import sys, pygame
from message_queue import message_queue

WHITE=(255,255,255)
size = width, height = 1920,1080 # screen dimensions, in pixels
CELL_SIZE=60 # square cell side in pixels
GRID_WIDTH=width//CELL_SIZE # Width, in cells
GRID_HEIGHT=height//CELL_SIZE # height, in cells


def random_color():
    return tuple([randrange(256) for _ in range(3)])

def run_game():
    pygame.init()
    grid = [[random_color() for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
    screen = pygame.display.set_mode(size)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()

        # Modify grid if command is queued, else just re-render
        try:
            x,y,color = message_queue.get(block=False)
            if 0<=y<len(grid) and 0<=x<len(grid[0]):
                grid[y][x]=color
        except:
            pass

        for i,row in enumerate(grid):
            for j,color in enumerate(row):
                x_coord = j*CELL_SIZE
                y_coord = i*CELL_SIZE
                pygame.draw.rect(screen, color, (x_coord, y_coord, CELL_SIZE, CELL_SIZE))
        pygame.display.flip()

if __name__ == "__main__":
    run_game()
