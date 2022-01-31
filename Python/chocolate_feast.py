# Hackerrank challenge
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'chocolateFeast' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c
#  3. INTEGER m
#

# n in candies = n // c

leftovers = 0

def chocolateFeast(n, c, m):
    global leftovers
    
    # can't buy anymore
    if (c > n):
        return 0
    # bars bought + credit left thanks to wrappers
    # credit left thanks to wrappers = (n_bought // m) * c
    n_bought = n // c
    n_bought_as_wrappers_credit = ((n_bought + leftovers) // m) * c
    leftovers = (n_bought + leftovers) % m
    return n_bought + chocolateFeast(n_bought_as_wrappers_credit, c, m)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)
        leftovers = 0

        fptr.write(str(result) + '\n')

    fptr.close()
