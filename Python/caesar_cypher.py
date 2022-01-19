#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

# 65 = 'A' 90 = 'Z'
# 97 = 'a' 122 = 'z'
def inValidRange(c, k):
    return (c >= 65 and c + k <= 90) or (c >= 97 and c + k <= 122)

def get_start_char(c):
    if c>= 65 and c <= 90:
        return 65
    return 97

def get_end_char(c):
    if c>= 65 and c <= 90:
        return 90
    return 122

def getNewAscii(elem, k):
    if not elem.isalpha():
        return ord(elem)
    ascii_val = ord(elem)  
    if inValidRange(ascii_val, k):
        ascii_val += k
    else:
        start_val = get_start_char(ascii_val)
        end_val = get_end_char(ascii_val)
        diff = end_val - ascii_val
        # print(f"st: {start_val} end: {end_val} ascii: {ascii_val}")
        ascii_val = start_val + k - diff - 1
    return ascii_val

def caesarCipher(s, k):
    ret = ""
    for elem in s:
        ret += chr(getNewAscii(elem, k % 26))
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)
    #print(ord('z'))
    #print(ord('|'))

    fptr.write(result + '\n')

    fptr.close()
