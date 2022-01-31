# Hackerrank challenge
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'taumBday' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER b
#  2. INTEGER w
#  3. INTEGER bc
#  4. INTEGER wc
#  5. INTEGER z
#

# b --> needs to buy b black gifts --> bc = cost of black
# w --> needs to buy w white gifts --> wc = cost of white
# z = price to convert b-->w and w-->b
# find min cost
# Price to pay if simply buy: b * bc + w * wc
# Price to pay if convert: 
# 1) b * bc + w * z * bc
# 2) w * wc + b * z * wc
def taumBday(b, w, bc, wc, z):
    simply_buy = b * bc + w * wc
    convert_b = b * (wc + z) + w * wc
    convert_w = w * (bc + z) + b * bc
    return min([simply_buy, convert_b, convert_w])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
