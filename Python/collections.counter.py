from collections import Counter

if __name__ == "__main__":
    n_shoes = int(input())
    
    # A counter is a container that stores elements as dictionary keys,
    # and their counts are stored as dictionary values.
    # Example:
    # >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
    # >>> print Counter(myList)
    # Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
    shoes_sizes = Counter(map(int, input().split()))   
    
    n_customers = int(input())
    
    money_earned = 0
    
    for i in range(n_customers):
        l = list(map(int, input().split()))
        size = l[0]
        price = l[1]
        if size in shoes_sizes and shoes_sizes[size] > 0:
            money_earned += price
            shoes_sizes[size] -= 1
    print(money_earned)
