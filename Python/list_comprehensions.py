import itertools

def perm_list(lst_arg, x, y, z, n):
    perms = set(itertools.permutations(lst_arg, 3))
    lst = [list(t) for t in perms if (sum(t) != n) and t[0] <= x and t[1] <= y and t[2] <= z]
    lst.sort()
    print (lst)


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    my_list = list(range(0, x + 1))
    my_list.extend(range(0, y + 1))
    my_list.extend(range(0, z + 1))
    perm_list(my_list, x, y, z, n)

