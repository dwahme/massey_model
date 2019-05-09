from massey import group
from massey import nbhd
import matplotlib.pyplot as plt
import math
import random

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


def plot(city, save=None):
    matrix = city.matrix

    xmax, ymax = factor_int(city.num_nbhds)

    colors = {}

    for x in range(xmax):
        for y in range(ymax):
            triples = matrix[x + y*xmax]

            groups = [group.Group(i[0], i[1], i[2]) for i in triples]

            for grp in groups:

                if grp.name in colors.keys():
                    color = colors[grp.name]
                    label = False
                else:
                    color = (random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))
                    colors[grp.name] = color
                    label = True

                scattered = grp.scatter(x, y)
                xs = [x for x, y in scattered]
                ys = [y for x, y in scattered]

                if label == True:
                    plt.scatter(xs, ys, c=[color], label=grp.name)
                else:
                    plt.scatter(xs, ys, c=[color])

    plt.legend(loc="center right", framealpha=1)

    plt.show()
