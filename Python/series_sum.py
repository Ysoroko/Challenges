# Codewars challenge
# Recursive solution

# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

def series_sum(n, div = 1, count=0, s = 1):
    if not count and count >= n:
        return "0.00"
    if count > n - 2:
        return "{:.2f}".format(s)
    return series_sum(n, div + 3, count + 1, s + 1 / (div + 3))
