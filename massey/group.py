
class Group:

    def __init__(self, name, number, poverty_level):
        self.name = name
        self.number = number
        self.poverty_level = poverty_level

    def fill_neighborhood(self, inv_prop):
        return (self.name, self.number // inv_prop, self.poverty_level)
