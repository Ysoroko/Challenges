#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    # Put all chars to lowercase + remove the duplicates by converting string to a set
    s = set(s.lower())

    # Sort the set to see if it will match the alphabet afterwards
    sorted_chars = sorted(s)
    
    # Convert it to string and remove the spaces
    l = (str("".join(sorted_chars)).strip())
    
    # Check if matches the alphabet
    return ("pangram" if l == alpha else "not pangram")
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
