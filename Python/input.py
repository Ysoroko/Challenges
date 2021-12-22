# Print True if P(k) = x. Otherwise, print False.

# INPUT
#1 4
#x**3 + x**2 + x + 1

# OUTPUT
# True

# Explanation:
# 1**3 + 1**2 + 1 + 1 = 4
# 4 = 4
# True

if __name__ == "__main__":
    l = input().split()
    x = l[0]
    solution = int(l[1])
    p = input().replace("x", x)
    
    # In python:
    # "exec(expression)" will execute it (Example: exec("print("Hello World!")"))
    # "eval(expression)" will calculate the result. Example: eval("1**3 + 1**2 + 1 + 1") will return 4
    print(eval(p) == solution)