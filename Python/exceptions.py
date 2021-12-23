if __name__ == "__main__":
    '''
    First input line = number of divisions to do
    Next n lines = 2 integers separated by spaces
    Performs division between these two integers (1st / 2nd) and prints the result
    Catches the exeception of case and division by zero and prints the error code otherwise
    '''
    n_tests = int(input())
    for i in range(n_tests):
        try:
            l = [int(i) for i in input().split()]
            a = l[0]
            b = l[1]
            print (a // b)
        except (ValueError, ZeroDivisionError) as e:
            print("Error Code:",e) 