def minBallDropperX(floors, n):
    import math  # needed for find logarithms as well as for rounding up functions
    drops: float

    drops = math.ceil(math.log(floors + 1) / math.log(
        2))  # with each ball drop we divide by two the number of floors on which the  critical floor might be. Number of drops required is found when: (no. of floors) / 2**(no. of drops) is less than 1

    if drops > n:  # if there are not enough balls available for the above method then...
        drops = math.ceil(
            floors / 2 ** (n - 1))  # we keep halving the number of floors by droping balls until we have 1 ball
        # left.
        drops = max(drops - 1,
                    math.ceil(floors / 2 ** (n - 2) - drops))  # This ball is then used to test each floor inbetween
        # the two levels established above.
        drops = drops + n - 1  # answer is the sum of the intital n-1 drops and the number of incremental ball drops
    return drops

print(minBallDropperX(100, 2))