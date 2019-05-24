from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups_no = [group.Group("a", 960 * 3, .1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13),
                 group.Group("d", 160 * 3, .3),
                 group.Group("d", 160 * 3, .3, 1)]

    groups_lo = [group.Group("a", 320 * 3, .1),
                 group.Group("a", 640 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13),
                 group.Group("d", 80 * 3, .3),
                 group.Group("d", 80 * 3, .3, 1),
                 group.Group("d", 80 * 3, .3, 2),
                 group.Group("d", 80 * 3, .3, 3)]

    groups_hi = [group.Group("a", 640 * 3, .1), 
                 group.Group("a", 320 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13),
                 group.Group("d", 80 * 3, .3),
                 group.Group("d", 80 * 3, .3, 1),
                 group.Group("d", 80 * 3, .3, 2),
                 group.Group("d", 80 * 3, .3, 3)]

    groups_all = [group.Group("a", 960 * 3, .1), 
                  group.Group("b", 320 * 3, .2),
                  group.Group("c", 400 * 3, .13),
                  group.Group("d", 80 * 3, .3),
                  group.Group("d", 80 * 3, .3, 1),
                  group.Group("d", 80 * 3, .3, 2),
                  group.Group("d", 80 * 3, .3, 3)]

    city_no = city.City(groups_no, 50)
    city_no.generate_mixed([["a", "b", ("d", 0)], ["c", ("d", 1)]])

    city_no_p = city.City(groups_no, 50)
    city_no_p.generate_mixed_p([["a", "b", ("d", 0)], ["c", ("d", 1)]])

    city_lo = city.City(groups_lo, 50)
    city_lo.generate_mixed([[("a", 0), ("d", 0)], [("a", 1), "b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    city_lo_p = city.City(groups_lo, 50)
    city_lo_p.generate_mixed_p([[("a", 0), ("d", 0)], [("a", 1), "b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    city_hi = city.City(groups_hi, 50)
    city_hi.generate_mixed([[("a", 0), ("d", 0)], [("a", 1), "b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    city_hi_p = city.City(groups_hi, 50)
    city_hi_p.generate_mixed_p([[("a", 0), ("d", 0)], [("a", 1), "b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    city_all = city.City(groups_all, 50)
    city_all.generate_mixed([[("a", 0), ("d", 0)], ["b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    city_all_p = city.City(groups_all, 50)
    city_all_p.generate_mixed_p([[("a", 0), ("d", 0)], ["b", ("d", 1)], ["c", ("d", 2)], [("d", 3)]])

    cities = [city_no, city_no_p, city_lo, city_lo_p, 
              city_hi, city_hi_p, city_all, city_all_p]
    # cities = [city_no_p, city_lo_p, city_hi_p, city_all_p]

    for c in cities:
        print("{:.4f} {:.4f}".format(analyzer.entropy_index(c), analyzer.entropy_index(c, True)))

        visualizer.plot(c)
