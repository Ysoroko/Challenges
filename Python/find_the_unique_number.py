# Codewars challenge
from collections import Counter

def find_uniq(arr):
    c = Counter(arr)
    values = list(c.values())
    position = values.index(1)
    return list(c.keys())[position]
