# Codingame challenge

#Turn an input name into a palindrome using this simple concept:

#Take a name like "Abe Simpson" and alternate each letter with the reverse name "nospmiS ebA" to get:

#Abe Simpson +
#nospmiS ebA =
#Anboes pSmiimSp seobnA

#Now you have your name Palindromified!

#Take an input string (name) and Palindromify it!

n=input()
print("".join([a+b for a,b in zip(n,n[::-1])]))
