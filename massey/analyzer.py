from massey import group
from massey import city
import math

def get_nbhd_pop(nbhd):
    return sum([grp.number for grp in nbhd])

# Calculates the entropy score for a city
def entropy_score_city(city, by_trait=False):

    entropy_score = 0

    if by_trait:
        # Get the total number of people with/without the trait

        with_trait = 0

        for grp in city.groups:
            if grp.number != 0:
                with_trait += grp.number / city.get_num_people() * grp.trait_percent

        if with_trait != 0:
            entropy_score += with_trait * math.log(1 / with_trait)

        tot_people = city.get_num_people()
        if with_trait != tot_people:
            prop_without = (tot_people - with_trait) / tot_people
            entropy_score += (prop_without) * math.log(1 / prop_without)

    else:
        for grp in city.groups:
            if grp.number != 0:
                prop = grp.number / city.get_num_people()

                if prop != 0:
                    entropy_score += prop * math.log(1 / prop)

                # else add 0
    
    return entropy_score


# Calculates the entropy score for a neighborhood/tract
def entropy_score_nbhd(nbhd, by_trait=False):

    entropy_score = 0
    tot_people = get_nbhd_pop(nbhd)
    
    for grp in nbhd:
        if grp.number != 0:
            prop = grp.number / tot_people

            if by_trait == True:
                prop *= grp.trait_percent
            
            if prop != 0:
                entropy_score += prop * math.log(1 / prop)

        # else add 0
    
    return entropy_score
        

# Calculates an entropy index of a city
# https://www2.census.gov/programs-surveys/demo/about/housing-patterns/multigroup_entropy.pdf
# Page 7
def entropy_index(city, by_trait=False):
    
    index = 0

    city_ent = entropy_score_city(city, by_trait)
    city_pop = city.get_num_people()

    for nbhd in city.matrix:

        nbhd_pop = get_nbhd_pop(nbhd)
        nbhd_ent = entropy_score_nbhd(nbhd, by_trait)

        index += (nbhd_pop * (city_ent - nbhd_ent)) / (city_ent * city_pop)

    return index

# Helper for nbhd_rates
def nbhd_trait_percent(nbhd):
    return sum([grp.trait_percent * grp.number for grp in nbhd]) / get_nbhd_pop(nbhd)

# Gets the trait levels for each group in a city
def nbhd_rates(city):

    rates = []

    for nbhd in city.matrix:

        # See if we've calculated this one yet
        grp_names = [grp.name for grp in nbhd]
        calced_names = [[grp.name for grp in n] for n, _ in rates]

        if grp_names not in calced_names:
            nbhd_rate = nbhd_trait_percent(nbhd)
            rates.append((nbhd, nbhd_rate))

        # else nbhd trait already calculated

    return rates
