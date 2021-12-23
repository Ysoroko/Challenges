if __name__ == "__main__":
    n = int(input())
    s = set(map(int, input().split()))
    n_cmds = int(input())
    for i in range(n_cmds):
        l = input().split()
        arg = "" if len(l) == 1 else l[1]
        try:
            exec("s." + l[0] + "(" + arg + ")")
        except KeyError as e:
            pass
    print(sum(s))
