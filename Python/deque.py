from collections import deque

d = deque()

funcdict = {
    'append': d.append,
    'pop': d.pop,
    'popleft': d.popleft,
    'appendleft': d.appendleft
}

if __name__ == "__main__":
    n = int(input().strip())

    for i in range(n):
        l = input().split()
        command = l[0]
        arg = ("" if len(l) == 1 else int(l[1]))
        funcdict[command](arg) if arg else funcdict[command]()
    
    for elem in d:
        print(elem, end = " ")
    print("")
    
