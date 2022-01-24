from itertools import product

if __name__ == "__main__":
    lines, m = tuple(map(int, input().split()))
    
    l = list()
    for i in range(lines):
        new_elem = list(map(lambda x : int(x) * int(x), input().split()))
        # First element is used to show the number of elements on the line, we don't include it in the calculations
        l.append(new_elem[1:])
    
    # *l allows us to pass every sublist of l as a separate argument to product function
    p = product(*l)
    
    ret = 0
    
    for elem in p:
        s = sum(elem) % m
        if (s > ret):
            ret = s 
    print(ret)
