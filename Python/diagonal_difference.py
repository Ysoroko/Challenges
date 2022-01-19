#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr, len_arr):
    main_dia = [arr[i][i] for i in range(len_arr)]

    # i = 2: arr[3 - 2 - 1][2] = '3'
    # i = 1: arr[3 - 1 - 1][1] = '5
    # i = 0: arr[3 - 0 - 1][0] = '9'
    second_dia = [arr[len_arr - i - 1][i] for i in range(len_arr - 1, -1, -1)]
    return (abs(sum(main_dia) - sum(second_dia)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr, n)

    fptr.write(str(result) + '\n')

    fptr.close()
