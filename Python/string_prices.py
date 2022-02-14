# Codingame challenge
# Print the string with the highest price
# Price of a character c: ascii value of c multiplied by its position in the string (starting at 1)

n = int(input())

r = 0
string = ""
for i in range(n):
    s = input()
    summed = sum([ord(c) * (i + 1) for i, c in enumerate(s)])
    if summed > r or (s > string and summed == r):
        r = summed
        string = s
print(string)
