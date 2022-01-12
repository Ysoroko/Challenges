#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

# [0 0] [0 l]   [l 0]   [l l]
# [0 1] [0 l-1] [l 1]   [l l-1]
# [1 0] [1 l]   [l-1 0] [l-1 l]

def getMax(matrix, l, i, j):
    a = matrix[0 + j][0 + i]
    b = matrix[0 + j][l - i]
    c = matrix[l - j][0 + i]
    d = matrix[l - j][l - i]

    m = max(a, b, c, d)
    # print("[" + str(i) + "]" + " " + "[" + str(j) + "]" + " m: " + str(m))
    return m
    

def flippingMatrix(matrix):
    l = len(matrix) - 1
    half = l // 2
    n = 0
    
    for i in range(half + 1):
        for j in range(half + 1):
            n += getMax(matrix, l, i, j)
    return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()
