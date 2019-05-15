from massey import group
from massey import city
import math

def tract_pop(nbhd):
    return sum([grp.number for grp in nbhd])

# Calculates the entropy score for a city
def entropy_score_city(city):

    entropy_score = 0
    
    for grp in city.groups:
        if grp.number != 0:
            prop = grp.number / city.get_num_people()
            
            entropy_score += prop * math.log(1 / prop)

        # else add 0
    
    return entropy_score


# Calculates the entropy score for a neighborhood/tract
def entropy_score_nbhd(nbhd):

    entropy_score = 0
    tot_people = tract_pop(nbhd)
    
    for grp in nbhd:
        if grp.number != 0:
            prop = grp.number / tot_people
            
            entropy_score += prop * math.log(1 / prop)

        # else add 0
    
    return entropy_score
        

# Calculates an entropy index of a city
# https://www2.census.gov/programs-surveys/demo/about/housing-patterns/multigroup_entropy.pdf
# Page 7
def entropy_index(city):
    
    index = 0

    city_ent = entropy_score_city(city)
    city_pop = city.get_num_people()

    for nbhd in city.matrix:

        nbhd_pop = tract_pop(nbhd)
        nbhd_ent = entropy_score_nbhd(nbhd)

        index += (nbhd_pop * (city_ent - nbhd_ent)) / (city_ent * city_pop)

    return index

# Helper for nbhd_poverties
def nbhd_poverty_level(nbhd):
    return sum([grp.poverty_level * grp.number for grp in nbhd]) / tract_pop(nbhd)

# Gets the poverty levels for each group in a city
def nbhd_poverties(city):

    poverties = []

    for nbhd in city.matrix:

        # See if we've calculated this one yet
        grp_names = [grp.name for grp in nbhd]
        calced_names = [[grp.name for grp in n] for n, _ in poverties]

        if grp_names not in calced_names:
            nbhd_pov = nbhd_poverty_level(nbhd)
            poverties.append((nbhd, nbhd_pov))

        # else nbhd poverty already calculated

    return poverties
