# COP3502C 
# Whackamole Game!
# Natalie Ortiz
# Professor Aggarwal

# Youtube Link: https://youtu.be/bmaiYYmeMzI?si=1wik6CZ-vLYYgeBt


import pygame
import random

CELL_SIZE = 32
COLS = 20
ROWS = 16

def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")

        mole_image = pygame.transform.scale(mole_image, (CELL_SIZE - 2, CELL_SIZE -2))
        mole_col, mole_row = 0, 0

        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mx, my = event.pos
                    if (mole_col * CELL_SIZE <= mx < (mole_col + 1) * CELL_SIZE and mole_row * CELL_SIZE <= my < (mole_row + 1) * CELL_SIZE):
                        new_col, new_row = mole_col, mole_row
                        while new_col == mole_col and new_row == mole_row:
                            new_col = random.randrange(0, COLS)
                            new_row = random.randrange(0, ROWS)
                        mole_col, mole_row = new_col, new_row

            screen.fill("light green")

            # draws the 20x16 grid !
            for col in range(COLS + 1):
                pygame.draw.line(screen, "dark green", (col * CELL_SIZE, 0), (col * CELL_SIZE, 512))
            
            for row in range(ROWS + 1):
                pygame.draw.line(screen, "dark green", (0, row * CELL_SIZE), (640, row * CELL_SIZE))

            # draws the mole :)
            x = mole_col * CELL_SIZE + 1
            y = mole_row * CELL_SIZE + 1
            screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
            
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
