
class City:

    def __init__(self, groups, neighborhoods):
        self.groups = groups
        self.neighborhoods = neighborhoods

        self.matrix = []

    # Evenly evenly distributes people across a given number of neighborhoods
    def generate_uniform(self):
        matrix = []

        # Build each neighborhood one at a time
        for _ in range(self.neighborhoods):
            neighborhood = []

            # Get an even distribution from each group
            for group in self.groups:
                neighborhood.append((group[0], group[1] / self.neighborhoods))

            matrix.append(neighborhood)

        self.matrix = matrix

        return matrix

    def generate_segregated(self):
        matrix = []

        # Determine the total number of people
        # then figure out how many neighborhoods each group gets
        num_people = sum([num for (name, num) in self.groups])
        neighborhood_nums = [self.neighborhoods * num // num_people 
            for (name, num) in self.groups]

        print(neighborhood_nums)

        # Distribute according to how many neighborhoods the group gets
        for (num, group) in zip(neighborhood_nums, self.groups):

            for _ in range(num):
                matrix.append([(group[0], group[1] / num)])

        self.matrix = matrix

        return matrix



