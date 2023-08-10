from time import sleep
from random import randint
from arrays import *
from sys import argv

empty_field = [[0 for _ in range(50)] for _ in range(50)]


def insert_figure(empty_array, figure):
    array = empty_array
    y_offset = len(array) // 2 - len(figure) // 2
    x_offset = len(array[0]) // 2 - len(figure[0]) // 2
    for y in range(len(figure)):
        for x in range(len(figure[0])):
            arr_y, arr_x = y + y_offset, x + x_offset
            array[arr_y][arr_x] = figure[y][x]
    # print(f'y offset: {y_offset}, x offset: {x_offset} len y,x : {len(array)},{len(array[0])}, fig len y,x : {len(figure)}, {len(figure[0])}')
    return array


def random_array(empty_array):
    array = empty_array
    for y in range(len(array)):
        for x in range(len(array[0])):
            array[y][x] = randint(0, 1)

    return array


def check_neighbor(array, y, x):
    cells = 0

    for i in range(max(0, y - 1), min(y + 2, len(array))):
        for j in range(max(0, x - 1), min(x + 2, len(array[0]))):
            if array[i][j]:
                cells += 1

    return cells


def check_neighbor_borderless(array, y, x):
    cells = 0

    for i in range(y - 1, y + 2):
        if i >= len(array):
            i -= len(array)
        for j in range(x - 1, x + 2):
            if j >= len(array[0]):
                j -= len(array[0])
            if array[i][j]:
                cells += 1

    return cells


def check_neighbor_slice(array, y, x):  # slice method works 0.2 times slower than for loop
    cells = 0

    for i in range(max(0, y - 1), min(y + 2, len(array))):
        cells += sum(array[i][max(0, x - 1):min(x + 2, len(array[0]))])

    return cells


def update_array(array, check_func=check_neighbor_borderless):
    neighbors = [[0 for _ in range(len(array[0]))] for _ in range(len(array))]

    for y in range(len(array)):
        for x in range(len(array[0])):
            neighbors[y][x] = check_func(array, y, x)

    for y in range(len(array)):
        for x in range(len(array[0])):
            if not array[y][x]:
                if neighbors[y][x] == 3:
                    array[y][x] = 1

            elif neighbors[y][x] - 1 > 3 or neighbors[y][x] - 1 < 2:
                array[y][x] = 0


def print_array(array, debug=False):
    print("\033c", end="")
    print('  ', end='')
    print("_ " * len(array))
    for row in array:
        print('|', end='')
        for cell in row:
            if not debug:
                if cell:
                    print(' #', end='')
                else:
                    print('  ', end='')
            else:
                print(f' {cell} ', end='')

        print(' |')
    print('  ', end='')
    print("‾ " * len(array))


if __name__ == '__main__':

    figure = glider_gun

    if '-r' in argv:
        board = random_array(empty_field)
    else:
        board = insert_figure(empty_field, figure)

    if '-b' in argv:
        check = check_neighbor
    else:
        check = check_neighbor_borderless

    if '-t' in argv:
        check = check_neighbor_slice

    while True:
        update_array(board, check)
        print_array(board)
        sleep(0.05)

    # from time import process_time
    # count = 0
    # start_time = process_time()

    # while count < 1000:
    #     game_of_life(board, check)
    #     # print_array(board)
    #     # sleep(0.05)
    #     count += 1

    # print(process_time() - start_time)
