import numpy as np


def minBrokeInWorstCase(balls, floors):
    table = np.zeros((balls + 1, floors + 1))
    # If there is only the 0th floor or the first floor
    for i in range(balls + 1):
        table[i][0] = 0
        table[i][1] = 1
        # If there is only one ball
    for j in range(floors + 1):
        table[1][j] = j
        # Other cases, table (balls, floors) = 1 + Max (table (balls-1, floors-1), table (balls, floors-x))
    for i in range(2, balls + 1):
        for j in range(2, floors + 1):
            table[i][j] = 2 ** 63 - 1
            for x in range(1, j):
                # table [i-1] [x-1] indicates that the ball was broken in the X floor and reduced by one. table [balls] [j-x] indicates that the ball is still the beginning
                # Floor becomes j-x
                maxtable = 1 + max(table[i - 1][x - 1], table[i][j - x])
                if maxtable < table[i][j]:
                    table[i][j] = maxtable
    print(table[balls][floors])


if __name__ == '__main__':
    minBrokeInWorstCase(2, 100)
