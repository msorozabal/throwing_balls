def minBrokeInWorstCase(floor, balls):
    minBallDrops_with_1_ball = list(range(floor + 1))
    minBallDrops_with_2_ball = list(range(floor + 1))

    for i in range(balls, floor + 1):
        floorsBr = minBallDrops_with_1_ball[:i]  # Case ball breaks
        floorsBd = minBallDrops_with_2_ball[:i][::-1]  # Case ball don't break
        minBallDrops_with_2_ball[i] = 1 + min(map(max, zip(floorsBr, floorsBd)))

    print('minBrokeInWorstCase =', minBallDrops_with_2_ball[-1])

minBrokeInWorstCase(100, 2)