from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups_no = [group.Group("a", 960 * 3, .1), 
                 group.Group("b", 320 * 3, .2)]

    groups_lo = [group.Group("a", 320 * 3, .1),
                 group.Group("a", 640 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2)]

    groups_hi = [group.Group("a", 640 * 3, .1), 
                 group.Group("a", 320 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2)]

    groups_all = [group.Group("a", 960 * 3, .1), 
                  group.Group("b", 320 * 3, .2)]

    city_no = city.City(groups_no, 16)
    city_no.generate_uniform()

    city_no_p = city.City(groups_no, 16)
    city_no_p.generate_uniform_p()

    city_lo = city.City(groups_lo, 16)
    city_lo.generate_mixed([[("a", 0)], [("a", 1), "b"]])

    city_lo_p = city.City(groups_lo, 16)
    city_lo_p.generate_mixed_p([[("a", 0)], [("a", 1), "b"]])

    city_hi = city.City(groups_hi, 16)
    city_hi.generate_mixed([[("a", 0)], [("a", 1), "b"]])

    city_hi_p = city.City(groups_hi, 16)
    city_hi_p.generate_mixed_p([[("a", 0)], [("a", 1), "b"]])

    city_all = city.City(groups_all, 16)
    city_all.generate_segregated()

    city_all_p = city.City(groups_all, 16)
    city_all_p.generate_segregated_p()

    cities = [city_no, city_no_p, city_lo, city_lo_p, 
              city_hi, city_hi_p, city_all, city_all_p]
    # cities = [city_no_p, city_lo_p, city_hi_p, city_all_p]

    for c in cities:
        print("{:.4f} {:.4f}".format(analyzer.entropy_index(c), analyzer.entropy_index(c, True)))

        visualizer.plot(c)
