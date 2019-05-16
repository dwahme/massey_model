from massey import group
from massey import city
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

    choices = "bgrcmykw"
    colors = {}
    names_used = []

    for x in range(xmax):
        for y in range(ymax):
            groups = matrix[x + y*xmax]

            for grp in groups:

                stripped_name = grp.name.split("_", 1)[0]

                if stripped_name in colors.keys():
                    color = colors[stripped_name]
                else:
                    color = choices[0]
                    choices = choices[1:]
                    colors[stripped_name] = color
                
                label = False
                if grp.name not in names_used:
                    names_used.append(grp.name)
                    label = True

                marker = "^"
                if "_poor" in grp.name:
                    marker = "."

                scattered = grp.scatter(x, y)
                xs = [x for x, y in scattered]
                ys = [y for x, y in scattered]

                if label == True:
                    plt.scatter(xs, ys, marker=marker, c=color, label=grp.name)
                else:
                    plt.scatter(xs, ys, marker=marker, c=color)

    plt.legend(loc="center right", framealpha=1)

    plt.show()
