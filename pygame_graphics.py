import pygame
from arrays import bee_defence
from game_of_life import insert_figure, update_array

pygame.init()

user_event = pygame.USEREVENT
pygame.time.set_timer(user_event, 50)

game_window = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()

# colors:
black = (0, 0, 0)
dark_gray = (50, 50, 50)
gray = (100, 100, 100)
light_gray = (150, 150, 150)

pygame.display.set_caption('Game of Life')

empty_field = [[0 for _ in range(100)] for _ in range(100)]

board = insert_figure(empty_field, bee_defence)


def draw_board(surface, array, cell_size=(5, 5), color=light_gray, offset=(0, 0)):
    for y, row in enumerate(array):
        for x, cell in enumerate(row):
            if cell:
                y_coord = offset[0] + y * cell_size[0]
                x_coord = offset[1] + x * cell_size[1]
                pygame.draw.rect(surface, color, ((y_coord, x_coord), cell_size))


def main():
    while True:
        game_window.fill(dark_gray)
        clock.tick(60)
        draw_board(game_window, board)

        for event in pygame.event.get():
            if event.type == user_event:
                update_array(board)
            if event.type == pygame.QUIT:
                pygame.quit()
        pygame.display.flip()


if __name__ == '__main__':
    main()
