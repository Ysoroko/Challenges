from itertools import combinations as cb

if __name__ == "__main__":
    l = input().split()
    len = int(l[1])
    out = list()
    for i in range(len):
        lis = list(cb(l[0], i + 1))
        for elem in lis:
            out.append("".join(sorted(elem)))
        out.sort()
        for elem in out:
            print(elem)
        out = list()
