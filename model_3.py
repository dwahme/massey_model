from massey import analyzer
from massey import group
from massey import city
from massey import visualizer

if __name__ == "__main__":
    groups_no = [group.Group("whites", 9600, .1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13)]

    groups_lo = [group.Group("whites", 3200, .1),
                 group.Group("whites", 6400, .1, 1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13)]

    groups_hi = [group.Group("whites", 6400, .1), 
                 group.Group("whites", 3200, .1, 1), 
                 group.Group("blacks", 3200, .2),
                 group.Group("asians", 4000, .13)]

    groups_all = [group.Group("whites", 9600, .1), 
                  group.Group("blacks", 3200, .2),
                  group.Group("asians", 4000, .13)]

    city_no = city.City(groups_no, 42)
    city_no.generate_mixed_p([["whites", "blacks"], ["asians"]])

    city_lo = city.City(groups_lo, 42)
    city_lo.generate_mixed_p([[("whites", 0)], [("whites", 1), "blacks"], ["asians"]])

    city_hi = city.City(groups_hi, 42)
    city_hi.generate_mixed_p([[("whites", 0)], [("whites", 1), "blacks"], ["asians"]])

    city_all = city.City(groups_all, 42)
    city_all.generate_segregated_p()

    cities = [city_no, city_lo, city_hi, city_all]

    for c in cities:
        print(analyzer.entropy_index(c))

        # visualizer.plot(c)
