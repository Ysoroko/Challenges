import calendar

# Print the name of the day related to the input
# Input: MONTH DAY YEAR
# Example: 12 24 1884
if  __name__ == "__main__":
    l = list(map(int, input().split()))
    n_day = calendar.weekday(l[2], l[0], l[1])
    print(calendar.day_name[n_day].upper())
