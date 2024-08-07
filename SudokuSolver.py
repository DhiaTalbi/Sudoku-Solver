import pygame


def sudoku(puzzle):   
    def valid(grid, r, c, k):
        not_in_row = k not in grid[r]
        not_in_line = k not in [grid[i][c] for i in range(9)]
        not_in_sg = k not in [ grid[i][j] for i in range(r//3*3, r//3*3+3) for j in range(c//3*3, c//3*3+3)]
        
        return not_in_row and not_in_line and not_in_sg
    
        
    def solve(puzzle, r = 0, c = 0):
        
        if r == 9:
            return True
        elif c == 9:
            return solve(puzzle, r+1, 0)
        elif puzzle[r][c] != 0:
            return solve(puzzle, r , c+1)
        else:
            for i in range(1,10):
                
                if valid(puzzle, r, c, i):
                    puzzle[r][c] = i
                    draw_grid()
                    pygame.display.flip()
                    pygame.time.wait(5)
                    if solve(puzzle, r, c+1):
                        return True
                    puzzle[r][c] = 0
                    draw_grid()
                    pygame.display.flip()
                    pygame.time.wait(5)
                    
    solve(puzzle)
    return puzzle


# Initialize Pygame
pygame.init()

# Set up display
size = 9
cell_size = 70
width, height = size * cell_size, size * cell_size
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Solver Algorithm")


# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (192, 192, 192)
RED = (255, 0, 0)
LIGHT_BLUE = (173, 216, 230)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
ORIGINAL_NUM_COLOR = BLUE  
SOLVING_NUM_COLOR = RED   


# Font
font = pygame.font.SysFont(None, 30)


def draw_grid():
    screen.fill(WHITE)
    
    # Draw the grid lines
    for row in range(size):
        for col in range(size):
            rect = pygame.Rect(col * cell_size, row * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, GRAY, rect)
            pygame.draw.rect(screen, BLACK, rect, 1)
            
            if grid[row][col] != 0:
                    if original_grid[row][col] != 0:
                        text_surf = font.render(str(grid[row][col]), True, ORIGINAL_NUM_COLOR)
                    else:
                        text_surf = font.render(str(grid[row][col]), True, SOLVING_NUM_COLOR)
                    text_rect = text_surf.get_rect(center=(col * cell_size + cell_size // 2, row * cell_size + cell_size // 2))
                    screen.blit(text_surf, text_rect)

    # Draw the thicker lines for subgrids
    for i in range(0, size + 1, 3):
        line_width = 3
        pygame.draw.line(screen, BLACK, (0, i * cell_size), (width, i * cell_size), line_width)
        pygame.draw.line(screen, BLACK, (i * cell_size, 0), (i * cell_size, height), line_width) 



grid = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]

original_grid = [row[:] for row in grid]


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            running = False


    sudoku(grid) 
    pygame.display.flip()
    
            

pygame.quit()