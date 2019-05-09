
class Group:

    def __init__(self, name, number, poverty_level):
        self.name = name
        self.number = number
        self.poverty_level = poverty_level

    def fill_nbhd(self, inv_prop):
        return (self.name, self.number // inv_prop, self.poverty_level)

    def split_poverty(self):
        rich = Group(self.name + "_rich", self.number // 2, 0)
        poor = Group(self.name + "_poor", self.number // 2, 
                     self.poverty_level * 2)
        return rich, poor
