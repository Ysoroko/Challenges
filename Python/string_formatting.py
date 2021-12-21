def print_formatted(dec):
    for i in range(1, n + 1):
        l = len(bin(dec)[2:]) # padding length
        
        decimal = str(i).rjust(l)
        octal = (oct(i)[2:]).rjust(l)
        hexadecimal = ((hex(i)[2:]).upper()).rjust(l)
        binary = bin(i)[2:].rjust(l)
        print(decimal + octal + hexadecimal + binary)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)