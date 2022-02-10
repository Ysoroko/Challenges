# Codingame challenge
# Given two strings of the same length, your task is to transform one into another by changing one character at a time, from left to right
# For example, if the strings are "bubble gum" and "turtle ham", the transformation goes as follows:
# bubble gum
# tubble gum
# turble gum
# turtle gum
# turtle hum
# turtle ham

# Input: 2 lines, string_a and string b
# Output: every step of the transformation

source = input()
target = input()

last = ""
for i in range(len(source) + 1):
    current = target[0:i] + source[i:]
    if current != last:
        print(current)
    last = current
