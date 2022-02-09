# Codingame challenge
# Print the sum of ascii values of the characters in the given string
from functools import reduce

s = map(ord, input())

r = reduce(lambda x, y : x + y, s)

print(r)
