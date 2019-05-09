from massey import group
from massey import nbhd

if __name__ == "__main__":
    groups0 = [group.Group("humans", 20, .3), 
               group.Group("elves", 20, 0)]
               
    groups1 = [group.Group("humans", 18, .3), 
               group.Group("elves", 6, 0),
               group.Group("orcs", 12, .5)]

    city0 = nbhd.City(groups0, 5)

    # print(city0.generate_uniform())
    # print(city0.generate_segregated())

    city1 = nbhd.City(groups1, 6)

    # print(city1.generate_uniform())
    # print(city1.generate_segregated())
    # print("")
    # print(city1.generate_mixed([["humans"], ["elves", "orcs"]]))
    print(city1.generate_mixed_p([["humans"], ["elves", "orcs"]]))

    

