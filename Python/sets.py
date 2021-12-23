def average(array):
    '''
    If we convert a list to a set,
    it becomes unordered and loses all the duplicate values!
    '''
    s = set(array)
    return (sum(s) / len(s))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
