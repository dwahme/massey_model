from massey import group
from massey import neighborhood as nbhd
import matplotlib.pyplot as plt
import math

def factor_int(n):
    nsqrt = math.ceil(math.sqrt(n))
    solution = False
    val = nsqrt
    while not solution:
        val2 = int(n/val)
        if val2 * val == float(n):
            solution = True
        else:
            val-=1
    return val, val2

def noisy(neighborhood):
    pass


def plot(city, save=None):
    matrix = city.matrix

    xmax, ymax = factor_int(city.num_neighborhoods)

    pass
