#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    changed_chars = 0
    # List comprehension for:
    # 1) For each i, we take a substring of [s[i], s[i + 3]]
    # 2) The third argument in range() says how much we need increment i each time (= "i+=3" here)
    l = [ s[i:i + 3] for i in range(0, len(s) - 2, 3) ]
    for elem in l:
        for i, char in enumerate(elem):
            if (((i == 0 or i == 2) and char != "S") or (i == 1 and char != "O")):
                changed_chars += 1
    return changed_chars
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
