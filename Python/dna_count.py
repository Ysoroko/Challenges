# Codingame challenge
# The program:
# The nucleotides inside a DNA sequence can be represented by a string composed by A, C, G and T.
# A sample string representing a DNA sequence is "ATGCTTCAGAAAAGGTCAGCG".

# Your task is to count how many times the symbols A, C, G and T appear in the string s.

s=input()
c=lambda s,x:s.count(x)
print(*[c(s,x)for x in"ACGT"])
