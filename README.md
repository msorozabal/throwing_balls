# throwing_balls

Suppose that you have an N-story building and plenty of balls. Suppose also that a ball is broken if it is thrown off floor F or higher, and unhurt otherwise. First, devise a strategy to determine the value of F.  Is there a way to do it in ~lg N throws ? Is there a way to reduce the cost to ~2lg F ?


## Analysis, assuming that x is the maximum number of optimal solutions.

Then the first ball is thrown from the xth layer for the first time (regardless of whether it is broken or not, there are x-1 attempts).

If it is broken, the second ball is searched linearly in layers 1 to x-1, at most x-1 times;

If not broken, the first ball is thrown from the x + (x-1) layer a second time (now there are x-2 attempts left).

If it is broken this time, the second ball is searched linearly in the x + 1 ～ x + (x-1) -1 layers, at most x-2 times;

If the first ball has not been broken, throw it from the x + (x-1) + (x-2) layer, and so on.

The maximum number of floors that can be determined by x attempts is x + (x-1) + (x-2) + ... + 1 = x (x + 1) / 2.

### 1. Two balls problem f [n] = min {1 + max (i-1, f [ni]) | i = 1..n} Initial condition: f [0] = 0 (or f [1] = 1)

### 2.m balls problem f [n, m] = min {1 + max (f [i-1, m-1], f [ni, m]) | i = 1..n} Initial condition: f [i, 0] = 0 (or f [i, 1] = i)
