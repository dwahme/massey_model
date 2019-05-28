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

                lab = grp.name + "=" + str(grp.trait_percent)

                if lab in colors.keys():
                    color = colors[lab]
                else:
                    color = choices[0]
                    choices = choices[1:]
                    colors[lab] = color
                
                label = False
                if lab not in names_used:
                    names_used.append(lab)
                    label = True

                marker = "."

                scattered = grp.scatter(x, y)
                xs = [x for x, y in scattered]
                ys = [y for x, y in scattered]

                if label == True:
                    plt.scatter(xs, ys, c=color, label=lab)
                else:
                    plt.scatter(xs, ys, c=color)

    plt.legend(loc="center right", framealpha=1)

    plt.show()
