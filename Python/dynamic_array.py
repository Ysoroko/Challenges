#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
ret = list()

def append(n, xor, value, arr, last_answer):
    idx = (xor ^ last_answer) % n
    arr[idx].append(value)
    return last_answer
    
def assign(n, xor, value, arr, last_answer):
    idx = (xor ^ last_answer) % n
    l = arr[idx][value % len(arr[idx])]
    ret.append(l)
    return l

d = {
    1 : append,
    2 : assign
}

def dynamicArray(n, queries):
    # Initialize a list of empty lists
    arr = [[] for _ in range(n)]
    last_answer = 0

    for elem in queries:
        query_type, xor, value = elem[0], elem[1], elem[2]
        last_answer = d[query_type](n, xor, value, arr, last_answer)
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
