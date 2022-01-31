#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    ret = sys.maxsize
    for n in a:
        indexes = [index for index, elem in enumerate(a) if a[index] == n]
        indexes.sort()
        if len(indexes) > 1:
            diff = abs(indexes[0] - indexes[1])
            if diff < ret:
                ret = diff
    if ret == sys.maxsize:
        return -1
    return ret
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
