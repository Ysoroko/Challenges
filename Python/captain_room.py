if __name__ == "__main__":
    k = input()
    rooms = list(map(int, input().split()))
    one_occurence = set()
    multiple_occurences = set()
    
    for i in rooms:
        one_occurence.add(i) if i not in one_occurence else multiple_occurences.add(i)

    # pop() returns a random element
    print(one_occurence.difference(multiple_occurences).pop())
