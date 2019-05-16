import random

class Group:

    def __init__(self, name, number, poverty_level, ID=0):
        self.name = name
        self.number = number
        self.poverty_level = poverty_level
        self.ID = ID

    def __str__(self):
        return "{}:{}:{}".format(self.name, self.number, self.poverty_level)

    def __repr__(self):
        return self.__str__()

    def fill_nbhd(self, inv_prop):
        return Group(self.name, self.number // inv_prop, self.poverty_level)

    def split_poverty(self):
        rich = Group(self.name + "_rich", self.number // 2, 0)
        poor = Group(self.name + "_poor", self.number // 2, 
                     self.poverty_level * 2)
        return rich, poor

    def scatter(self, x_off, y_off):
        return [(random.uniform(0, 1) + x_off, random.uniform(0, 1) + y_off) 
                for _ in range(self.number)]
