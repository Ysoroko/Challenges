#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar


# >>> from collections import Counter
# >>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
# >>> Counter(z)
# Counter({'blue': 3, 'red': 2, 'yellow': 1})

def sockMerchant(n, ar):
    ret = 0

    c = Counter(ar)

    for elem in c.values():
        ret += c[elem] // 2

    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
