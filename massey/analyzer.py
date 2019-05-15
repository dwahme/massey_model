from massey import group
from massey import city
import math

def get_nbhd_pop(nbhd):
    return sum([grp.number for grp in nbhd])

# Calculates the entropy score for a city
def entropy_score_city(city, poverty=False):

    entropy_score = 0
    
    for grp in city.groups:
        if grp.number != 0:
            prop = grp.number / city.get_num_people()

            if poverty == True:
                prop *= grp.poverty_level

            if prop != 0:
                entropy_score += prop * math.log(1 / prop)

        # else add 0
    
    return entropy_score


# Calculates the entropy score for a neighborhood/tract
def entropy_score_nbhd(nbhd, poverty=False):

    entropy_score = 0
    tot_people = get_nbhd_pop(nbhd)
    
    for grp in nbhd:
        if grp.number != 0:
            prop = grp.number / tot_people

            if poverty == True:
                prop *= grp.poverty_level
            
            if prop != 0:
                entropy_score += prop * math.log(1 / prop)

        # else add 0
    
    return entropy_score
        

# Calculates an entropy index of a city
# https://www2.census.gov/programs-surveys/demo/about/housing-patterns/multigroup_entropy.pdf
# Page 7
def entropy_index(city, poverty=False):
    
    index = 0

    city_ent = entropy_score_city(city, poverty)
    city_pop = city.get_num_people()

    for nbhd in city.matrix:

        nbhd_pop = get_nbhd_pop(nbhd)
        nbhd_ent = entropy_score_nbhd(nbhd, poverty)

        index += (nbhd_pop * (city_ent - nbhd_ent)) / (city_ent * city_pop)

    return index

def nbhd_poverty_level(nbhd):
    return sum([grp.poverty_level * grp.number for grp in nbhd]) / get_nbhd_pop(nbhd)

def nbhd_poverties(city):

    poverties = []

    for nbhd in city.matrix:

        # See if we've calculated this one yet
        nbhd_pov = nbhd_poverty_level(nbhd)

        if (nbhd, nbhd_pov) not in poverties:
            poverties.append((nbhd_pov, nbhd))

        # else nbhd poverty already calculated

    return poverties
