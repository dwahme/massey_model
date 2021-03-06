from massey import group

class City:

    def __init__(self, groups, num_nbhds):
        self.groups = groups
        self.num_nbhds = num_nbhds

        self.matrix = []

    def get_group(self, name, ID=-1, groups=None):
        if groups == None:
            groups = self.groups

        if ID == -1:
            for group in groups:
                if group.name == name:
                    return group
        else:
            for group in groups:
                if group.name == name and group.ID == ID:
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

                if isinstance(name, str):
                    group = self.get_group(name, groups=groups)
                else:
                    group = self.get_group(name[0], name[1], groups)

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

    def generate_uniform_seg(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_trait() for group in groups]

        groups_n = []
        groups_m = []
        for n, m in splits:
            groups_n.append(n)
            groups_m.append(m)

        matrix = (self.generate_uniform(int(num_nbhds / 2), groups_n) + 
            self.generate_uniform(int(num_nbhds / 2), groups_m))

        self.matrix = matrix

        return matrix

    def generate_segregated_seg(self, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_trait() for group in groups]

        groups_n = []
        groups_m = []
        for r, p in splits:
            groups_n.append(r)
            groups_m.append(p)

        matrix = (self.generate_segregated(int(num_nbhds / 2), groups_n) + 
            self.generate_segregated(int(num_nbhds / 2), groups_m))

        self.matrix = matrix

        return matrix

    def split_mix_groups(self, item):
        
        if isinstance(item, str):
            return (item, item)
        else:
            return ((item[0], item[1]), (item[0], item[1]))


    def generate_mixed_seg(self, mixed_group_names, num_nbhds=-1, groups=None):
        if num_nbhds == -1:
            num_nbhds = self.num_nbhds
        if groups == None:
            groups = self.groups

        splits = [group.split_trait() for group in groups]

        groups_n = []
        groups_m = []
        for n, m in splits:
            groups_n.append(n)
            groups_m.append(m)

        names_n = []
        names_m = []
        for sublist in mixed_group_names:
            nested = [self.split_mix_groups(name) for name in sublist]

            names_n_tmp = []
            names_m_tmp = []
            for r, p in nested:
                names_n_tmp.append(r)
                names_m_tmp.append(p)

            names_n.append(names_n_tmp)
            names_m.append(names_m_tmp)

        matrix = (self.generate_mixed(names_n, int(num_nbhds / 2), groups_n) + 
            self.generate_mixed(names_m, int(num_nbhds / 2), groups_m))

        self.matrix = matrix

        return self.matrix

    def shock_group_rates(self, group_name, rate_change):
        for nbhd in self.matrix:
            for grp in nbhd:

                if grp.name == group_name:
                    if grp.concentrated == -1:
                        grp.trait_percent += rate_change
                    elif grp.concentrated == 1:
                        grp.trait_percent += 2 * rate_change
        
        for grp in self.groups:
            if grp.name == group_name:
                grp.trait_percent += rate_change
