if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        # Set A
        n_a = int(input())
        s_a = set(map(int, input().split()))
        
        # Set B
        n_b = int(input())
        s_b = set(map(int, input().split()))
        
        # If A is a subset of B, by combining them B won't change and will keep the same length
        ret = s_a.union(s_b)
        print(len(ret) == n_b)
