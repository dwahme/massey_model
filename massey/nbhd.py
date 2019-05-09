from massey import group

class City:

    def __init__(self, groups, num_nbhds):
        self.groups = groups
        self.num_nbhds = num_nbhds

        self.matrix = []

    def get_group_by_name(self, name, groups=None):
        if groups == None:
            groups = self.groups

        for group in groups:
            if group.name == name:
                return group

        return None

    def get_num_people(self, groups=None):
        if groups == None:
            groups = self.groups

        return sum([group.number for group in groups])

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
        num_people = self.get_num_people(groups)
        nbhd_nums = [num_nbhds * group.number // num_people 
            for group in groups]

        # Distribute according to how many num_nbhds the group gets
        for (num, group) in zip(nbhd_nums, groups):

            for _ in range(num):
                matrix.append([group.fill_nbhd(num)])

        self.matrix = matrix

        return matrix

    # Allows mixing up groupings of nbhds
    def generate_mixed(self, mixed_group_names, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        matrix = []

        total_people = self.get_num_people(groups)

        # Get the group mixes by looking up by name
        # Also get their relative proportions
        mixed_groups = []
        mixed_groups_counts = []
        for group_names in mixed_group_names:
            mixed_group = []
            mixed_group_num = 0

            for name in group_names:
                group = self.get_group_by_name(name, groups)

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

    def generate_uniform_p(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_poverty() for group in groups]

        groups_r = []
        groups_p = []
        for r, p in splits:
            groups_r.append(r)
            groups_p.append(p)

        matrix = (self.generate_uniform(int(num_nbhds / 2), groups_r) + 
            self.generate_uniform(int(num_nbhds / 2), groups_p))

        self.matrix = matrix

        return matrix

    def generate_segregated_p(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_poverty() for group in groups]

        groups_r = []
        groups_p = []
        for r, p in splits:
            groups_r.append(r)
            groups_p.append(p)

        matrix = (self.generate_segregated(int(num_nbhds / 2), groups_r) + 
            self.generate_segregated(int(num_nbhds / 2), groups_p))

        self.matrix = matrix

        return matrix

    def generate_mixed_p(self, mixed_group_names, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_poverty() for group in groups]

        groups_r = []
        groups_p = []
        for r, p in splits:
            groups_r.append(r)
            groups_p.append(p)

        names_r = []
        names_p = []
        for sublist in mixed_group_names:
            nested = [(name + "_rich", name + "_poor") for name in sublist]

            names_r_tmp = []
            names_p_tmp = []
            for r, p in nested:
                names_r_tmp.append(r)
                names_p_tmp.append(p)

            names_r.append(names_r_tmp)
            names_p.append(names_p_tmp)

        matrix = (self.generate_mixed(names_r, int(num_nbhds / 2), groups_r) + 
            self.generate_mixed(names_p, int(num_nbhds / 2), groups_p))

        self.matrix = matrix

        return self.matrix
