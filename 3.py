#WAP to check if a number is a multiple of 7 or not
x = int(input("Enter a number: "))

if (x % 7 == 0):
    print(f"{x} is a multiple of 7")    
else:
    print(f"{x} is not a multiple of 7")