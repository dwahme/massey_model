import massey.neighborhood as nbhd

if __name__ == "__main__":
    groups0 = [("humans", 20), ("elves", 5)]
    groups1 = [("humans", 18), ("elves", 6), ("orcs", 12)]

    city0 = nbhd.City(groups0, 5)

    print(city0.generate_uniform())
    print(city0.generate_segregated())

    city1 = nbhd.City(groups1, 6)

    print(city1.generate_uniform())
    print(city1.generate_segregated())

