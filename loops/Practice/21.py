#WAP to find the factorial of N number (using for)

n = int(input("Enter a number to find factorial: "))
fact = 1

for i in range(1, n+1):
    fact *= i
print("Factorial  is:", fact)
