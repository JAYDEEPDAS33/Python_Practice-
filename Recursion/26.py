#WARF to calculate sum of first n numbers

def calc_sum(n):
    if n == 0:
        return 0
    else:
        return n + calc_sum(n - 1)
sum = calc_sum(5)
print("Sum of first 5 numbers is:", sum)