from numba import jit
import random
import math
from time import time

@jit

def pi(sample_size):
    inside_circle = 0
    for n in range(sample_size):
        x, y = random.random(), random.random()
        if (math.sqrt(x * x + y * y) < 1):
            inside_circle = inside_circle + 1
    pi = (inside_circle / sample_size) * 4
    return(pi)

tic = time()
sample_size = 1e6
approxpi = pi(int(sample_size))
toc = time()
print(approxpi, 'at', int(sample_size/(toc-tic)/1e6), 'million points per second')
