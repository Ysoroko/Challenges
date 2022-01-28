#!/bin/python3

import math
import os
import random
import re
import sys

l = list()

def cutTheSticks(arr):
    if arr:
        l.append(len(arr))
    if not arr or len(arr) <= 1:
        return l
    shortest = min(arr)
    for i in range(len(arr)):
        arr[i] -= shortest
    new_arr = [elem for elem in arr if elem > 0]
    return (cutTheSticks(new_arr))
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
