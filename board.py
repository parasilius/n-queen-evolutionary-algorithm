import pygame

class Board:
    def __init__(self, s, board_size=400):
        self.board_size = board_size
        self.s = s
        self.n = len(self.s)

    def show(self):
        #initalize the PYGAME
        pygame.init()
        #Setting screen size & NAME
        screen = pygame.display.set_mode((self.board_size, self.board_size))
        pygame.display.set_caption(f'solution to {self.n}-queen')
        #Making Board
        rows = cols = int(self.n)
        square_size = self.board_size//self.n
        white_colour = (250,250,250)
        black_colour = (0,0,0)
        image = pygame.image.load('images/wQ.png').convert_alpha()
        image = pygame.transform.scale(image, (square_size, square_size))
        #main
        def draw_squares(screen):
            screen.fill(white_colour)
            for row in range(rows):
                for colm in range(cols):
                    if (row % 2 == 0 and colm % 2 != 0) or (row % 2 != 0 and colm % 2 == 0):
                        rect = pygame.draw.rect(screen, black_colour, (colm * square_size, row*square_size, square_size, square_size))       
                    else:
                        rect = pygame.draw.rect(screen, white_colour, (colm * square_size, row*square_size, square_size, square_size))       
                    if self.n - row - 1 == self.s[colm]:
                        screen.blit(image, rect)

        draw_squares(screen)
        #loop
        i = True
        while i:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    i = False
            pygame.display.update()
        pygame.quit()
