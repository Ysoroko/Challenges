# Codingame challenge
#You must calculate the subnet mask of an IP given an integer N as the number of ones in the subnet mask.
#Print out the subnet mask in Binary and in Decimal mode.
#There is a simple way to do this. For example, if you are given the number 24, you are to create a binary subnet mask with 24 ones and 8 zeroes.
#11111111.11111111.11111111.00000000
#Now, we convert each section of eight bits into decimal.
#255.255.255.0
#Remember, Binary subnet masks ALWAYS HAVE 32 digits. If N is 32 or higher, output "INVALID".

n = int(input())
if n > 32:
    print("INVALID")
else:
    to_decimal = lambda x : int(x, 2)
    count = 0
    s1 = n * "1" + (32 - n) * "0"
    a,b,c,d = s1[:8], s1[8:16], s1[16:24], s1[24:]
    print(".".join([a, b, c, d]))
    print(".".join(map(str, list(map(to_decimal, [a,b,c,d])))))
