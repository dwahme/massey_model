from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups_no = [group.Group("whites", 9600, .1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13),
                 group.Group("hispanics", 1600, .17),
                 group.Group("hispanics", 1600, .17, 1)]

    groups_lo = [group.Group("whites", 3200, .1),
                 group.Group("whites", 6400, .1, 1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13),
                 group.Group("hispanics", 800, .17),
                 group.Group("hispanics", 800, .17, 1),
                 group.Group("hispanics", 800, .17, 2),
                 group.Group("hispanics", 800, .17, 3)]

    groups_hi = [group.Group("whites", 6400, .1), 
                 group.Group("whites", 3200, .1, 1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13),
                 group.Group("hispanics", 800, .3),
                 group.Group("hispanics", 800, .3, 1),
                 group.Group("hispanics", 800, .3, 2),
                 group.Group("hispanics", 800, .3, 3)]

    groups_all = [group.Group("whites", 9600, .1), 
                  group.Group("blacks", 3200, .2),
                  group.Group("asians", 4000, .13),
                  group.Group("hispanics", 800, .3),
                  group.Group("hispanics", 800, .3, 1),
                  group.Group("hispanics", 800, .3, 2),
                  group.Group("hispanics", 800, .3, 3)]

    city_no = city.City(groups_no, 50)
    city_no.generate_mixed([["whites", "blacks", ("hispanics", 0)], ["asians", ("hispanics", 1)]])

    city_no_p = city.City(groups_no, 50)
    city_no_p.generate_mixed_p([["whites", "blacks", ("hispanics", 0)], ["asians", ("hispanics", 1)]])

    city_lo = city.City(groups_lo, 50)
    city_lo.generate_mixed([[("whites", 0), ("hispanics", 0)], [("whites", 1), "blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    city_lo_p = city.City(groups_lo, 50)
    city_lo_p.generate_mixed_p([[("whites", 0), ("hispanics", 0)], [("whites", 1), "blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    city_hi = city.City(groups_hi, 50)
    city_hi.generate_mixed([[("whites", 0), ("hispanics", 0)], [("whites", 1), "blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    city_hi_p = city.City(groups_hi, 50)
    city_hi_p.generate_mixed_p([[("whites", 0), ("hispanics", 0)], [("whites", 1), "blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    city_all = city.City(groups_all, 50)
    city_all.generate_mixed([[("whites", 0), ("hispanics", 0)], ["blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    city_all_p = city.City(groups_all, 50)
    city_all_p.generate_mixed_p([[("whites", 0), ("hispanics", 0)], ["blacks", ("hispanics", 1)], ["asians", ("hispanics", 2)], [("hispanics", 3)]])

    cities = [city_no, city_no_p, city_lo, city_lo_p,
              city_hi, city_hi_p, city_all, city_all_p]

    for c in cities:
        print(analyzer.entropy_index(c), analyzer.entropy_index(c, True))

        # visualizer.plot(c)
