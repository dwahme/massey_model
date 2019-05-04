from massey import group

class City:

    def __init__(self, groups, num_neighborhoods):
        self.groups = groups
        self.num_neighborhoods = num_neighborhoods

        self.matrix = []

    def get_group_by_name(self, name):
        for group in self.groups:
            if group.name == name:
                return group

        return None

    def get_num_people(self):
        return sum([group.number for group in self.groups])

    # Evenly evenly distributes people across a given number of neighborhoods
    def generate_uniform(self, num_neighborhoods=-1, groups=None):
        if num_neighborhoods == -1:
            num_neighborhoods = self.num_neighborhoods
        if groups == None:
            groups = self.groups
        
        matrix = []

        # Build each neighborhood one at a time
        for _ in range(num_neighborhoods):
            neighborhood = []

            # Get an even distribution from each group
            for group in groups:
                neighborhood.append(group.fill_neighborhood(num_neighborhoods))

            matrix.append(neighborhood)

        self.matrix = matrix

        return matrix

    # Segregates all groups
    def generate_segregated(self, num_neighborhoods=-1, groups=None):
        if num_neighborhoods == -1:
            num_neighborhoods = self.num_neighborhoods
        if groups == None:
            groups = self.groups

        matrix = []

        # Determine the total number of people
        # then figure out how many num_neighborhoods each group gets
        num_people = self.get_num_people()
        neighborhood_nums = [num_neighborhoods * group.number // num_people 
            for group in groups]

        print(neighborhood_nums)

        # Distribute according to how many num_neighborhoods the group gets
        for (num, group) in zip(neighborhood_nums, groups):

            for _ in range(num):
                matrix.append(group.fill_neighborhood(num))

        self.matrix = matrix

        return matrix

    # Allows mixing up groupings of neighborhoods
    def generate_mixed(self, mixed_group_names, num_neighborhoods=-1):
        if num_neighborhoods == -1:
            num_neighborhoods = self.num_neighborhoods

        matrix = []

        total_people = self.get_num_people()

        # Get the group mixes by looking up by name
        # Also get their relative proportions
        mixed_groups = []
        mixed_groups_counts = []
        for group_names in mixed_group_names:
            mixed_group = []
            mixed_group_num = 0

            for name in group_names:
                group = self.get_group_by_name(name)

                if group == None:
                    return []

                mixed_group.append(group)
                mixed_group_num += group.number

            mixed_groups.append(mixed_group)
            mixed_groups_counts.append(mixed_group_num)

        # Generate each mixed part of the city uniformly
        for (mix, count) in zip(mixed_groups, mixed_groups_counts):
            matrix += self.generate_uniform(
                num_neighborhoods * count // total_people, mix)

        self.matrix = matrix

        return matrix


