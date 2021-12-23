if __name__ == "__main__":
    l_a = int(input())
    s_a = set(map(int, input().split())) 
    n_sets = int(input())

    for i in range(n_sets):
        cmd = (input().split())[0]
        s = set(map(int, input().split()))
        exec("s_a." + cmd + "(s)")
    print(sum(s_a))
