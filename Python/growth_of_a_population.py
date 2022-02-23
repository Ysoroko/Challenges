# Codewars challenge
# Recursive answer
#
# In a small town the population is p0 = 1000 at the beginning of a year.
# The population regularly increases by 2 percent per year and moreover 50 new inhabitants per year come to live in the town.
# How many years does the town need to see its population greater or equal to p = 1200 inhabitants?

def nb_year(p0, percent, aug, p, n_years=0):
    if int(p0) >= p:
        return n_years
    return nb_year(int(p0 + p0/100 * percent + aug), percent, aug, p, n_years + 1)
