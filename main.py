from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups0 = [group.Group("humans", 20, .3), 
               group.Group("elves", 20, 0)]
               
    groups1 = [group.Group("humans", 1800, .3), 
               group.Group("elves", 600, 0),
               group.Group("orcs", 1200, .5)]

    city0 = city.City(groups0, 5)

    city0.generate_uniform()
    print(analyzer.entropy_index(city0))

    # print(city0.generate_segregated())

    city1 = city.City(groups1, 120)

    # print(city1.generate_uniform())
    # print(city1.generate_segregated())
    # print("")
    # print(city1.generate_mixed([["humans"], ["elves", "orcs"]]))
    # print(city1.generate_mixed_p([["humans"], ["elves", "orcs"]]))

    city1.generate_mixed_p([["humans"], ["elves", "orcs"]])
    print(analyzer.entropy_index(city1))

    # for nbhd in city1.matrix:
    #     print(nbhd)

    povs = analyzer.nbhd_poverties(city1)

    for i in povs:
        print(i)

    visualizer.plot(city1)
