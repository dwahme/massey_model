from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups_no = [group.Group("a", 960 * 3, .1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13)]

    groups_lo = [group.Group("a", 320 * 3, .1),
                 group.Group("a", 640 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13)]

    groups_hi = [group.Group("a", 640 * 3, .1), 
                 group.Group("a", 320 * 3, .1, 1), 
                 group.Group("b", 320 * 3, .2),
                 group.Group("c", 400 * 3, .13)]

    groups_all = [group.Group("a", 960 * 3, .1), 
                  group.Group("b", 320 * 3, .2),
                  group.Group("c", 400 * 3, .13)]

    city_no = city.City(groups_no, 42)
    city_no.generate_mixed([["a", "b"], ["c"]])

    city_no_seg = city.City(groups_no, 42)
    city_no_seg.generate_mixed_seg([["a", "b"], ["c"]])

    city_lo = city.City(groups_lo, 42)
    city_lo.generate_mixed([[("a", 0)], [("a", 1), "b"], ["c"]])

    city_lo_seg = city.City(groups_lo, 42)
    city_lo_seg.generate_mixed_seg([[("a", 0)], [("a", 1), "b"], ["c"]])

    city_hi = city.City(groups_hi, 42)
    city_hi.generate_mixed([[("a", 0)], [("a", 1), "b"], ["c"]])

    city_hi_seg = city.City(groups_hi, 42)
    city_hi_seg.generate_mixed_seg([[("a", 0)], [("a", 1), "b"], ["c"]])

    city_all = city.City(groups_all, 42)
    city_all.generate_segregated()

    city_all_seg = city.City(groups_all, 42)
    city_all_seg.generate_segregated_seg()

    cities = [city_no, city_no_seg, city_lo, city_lo_seg, 
              city_hi, city_hi_seg, city_all, city_all_seg]
    # cities = [city_no_seg, city_lo_seg, city_hi_seg, city_all_seg]

    for c in cities:
        print("{:.4f} {:.4f}".format(analyzer.entropy_index(c), analyzer.entropy_index(c, True)))

        visualizer.plot(c)
