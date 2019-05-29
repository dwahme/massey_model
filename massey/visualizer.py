from massey import group
from massey import city
import matplotlib.pyplot as plt
import math
import random

plot_num = 0

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


def plot(city, save=False, name="fig", title=""):
    global plot_num

    matrix = city.matrix

    xmax, ymax = factor_int(city.num_nbhds)

    choices = list("bgrcmyk") + ["0.75"]
    colors = {}
    names_used = []

    plt.figure(plot_num)
    plt.title(title)

    for x in range(xmax):
        for y in range(ymax):
            groups = matrix[x + y*xmax]

            for grp in groups:

                lab = "{} ({:.0f}%)".format(grp.name, grp.trait_percent * 100)

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

    handles, labels = plt.figure(plot_num).gca().get_legend_handles_labels()
    labels, handles = zip(*sorted(zip(labels, handles), key=lambda t: t[0]))
    plt.figure(plot_num).legend(handles, labels, loc="center right", framealpha=1, title="Group (Trait Level)")

    plt.box(on=None)
    plt.axis("off")

    if save:
        plt.savefig("{}.png".format(name))
    else:
        plt.show()
