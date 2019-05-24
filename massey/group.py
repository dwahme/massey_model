import random

class Group:

    def __init__(self, name, number, trait_percent, ID=0):
        self.name = name
        self.number = number
        self.trait_percent = trait_percent
        self.ID = ID

    def __str__(self):
        return "{}:{}:{}".format(self.name, self.number, self.trait_percent)

    def __repr__(self):
        return self.__str__()

    def fill_nbhd(self, inv_prop):
        return Group(self.name, self.number // inv_prop, self.trait_percent, self.ID)

    def split_trait(self):
        no_trait = Group(self.name, self.number // 2, 0, self.ID)
        maybe_trait = Group(self.name, self.number // 2, 
                     self.trait_percent * 2, self.ID)
        return no_trait, maybe_trait

    def scatter(self, x_off, y_off):
        return [(random.uniform(0, 1) + x_off, random.uniform(0, 1) + y_off) 
                for _ in range(self.number)]
