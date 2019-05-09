from massey import group

class City:

    def __init__(self, groups, num_nbhds):
        self.groups = groups
        self.num_nbhds = num_nbhds

        self.matrix = []

    def get_group_by_name(self, name):
        for group in self.groups:
            if group.name == name:
                return group

        return None

    def get_num_people(self):
        return sum([group.number for group in self.groups])

    # Evenly evenly distributes people across a given number of nbhds
    def generate_uniform(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups
        
        matrix = []

        # Build each nbhd one at a time
        for _ in range(num_nbhds):
            nbhd = []

            # Get an even distribution from each group
            for group in groups:
                nbhd.append(group.fill_nbhd(num_nbhds))

            matrix.append(nbhd)

        self.matrix = matrix

        return matrix

    # Segregates all groups
    def generate_segregated(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        matrix = []

        # Determine the total number of people
        # then figure out how many num_nbhds each group gets
        num_people = self.get_num_people()
        nbhd_nums = [num_nbhds * group.number // num_people 
            for group in groups]

        print(nbhd_nums)

        # Distribute according to how many num_nbhds the group gets
        for (num, group) in zip(nbhd_nums, groups):

            for _ in range(num):
                matrix.append(group.fill_nbhd(num))

        self.matrix = matrix

        return matrix

    # Allows mixing up groupings of nbhds
    def generate_mixed(self, mixed_group_names, num_nbhds=-1):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds

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
                num_nbhds * count // total_people, mix)

        self.matrix = matrix

        return matrix


