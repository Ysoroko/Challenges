# Hackerrank challenge
# Implement a Reverse Polish Notation calculator,
# with the following operations:
# + - / * 
# x : binary operator equivalent to n1^2 + n2 (e.g. 5 2 x = 27)
# y : unary operator equivalent to  2*n + 1(e.g. 6 y = 13)
# z : ternary operator equivalent to  n1 + 2n2 + 3n3 (e.g. 1 2 3 z = 14)

d = {
    '+' : lambda x, y       : x + y,
    '-' : lambda x, y       : x - y,
    '*' : lambda x, y       : x * y,
    '/' : lambda x, y       : x // y,
    'x' : lambda x, y       : x**2 + y,
    'y' : lambda x          : 2*x + 1,
    'z' : lambda x, y, z    : x + 2 * y + 3 * z
}

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        error = False
        stack = list()
        line = input().split()
        for elem in line:
            if elem.isdigit():
                stack.append(int(elem))
            else:
                try:
                    res = d[elem](*stack)
                    stack.clear()
                    stack.append(res)
                except:
                    error = True
                    break
        print('NO' if error else stack.pop())
