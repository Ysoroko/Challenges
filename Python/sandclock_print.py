# Codingame clash of code challenge
# Reversed engineering type
#
# Example:
# ----------
# Input: abc
# Output:
# abc
#  b
# abc
# ----------
# Input: ab
# Output: "Error"
# ----------
# Input: abcde
# Output:
# abcde
#  bcd
#   c
#  bcd
# abcde


message = input()
l = len(message)
if not l % 2:
    print("Error")
else:
    half = l // 2
    
    for i in range(half):
        print(" " * i + message[i: l - i]) # + " " * i)
    for i in range(half, -1, -1):
        print(" " * i + message[i: l - i]) # + " " * i)
