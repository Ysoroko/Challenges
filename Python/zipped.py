if __name__ == "__main__":
    l = list(map(int, input().split()))
    x_subjects = l[1]
    n_students = l[0]
    
    lists = list()
    for _ in range(x_subjects):
        lists.append(list(map(float, input().split())))
    
    # *prefix allows to unpack the list into several elements
    # lst = [0, 1, 2 ,3]
    # *lst = 0 1 2 3
    # We can pass the unpacked list as multiple arguments to "zip"
    grades = zip(*lists)
    for elem in grades:
        print(f"{sum(elem) / x_subjects}")
    
