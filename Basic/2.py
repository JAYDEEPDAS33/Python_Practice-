#WAP to find the greater number among two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))         
c = int(input("Enter third number: "))

if(a >= b) and (a >= c):
    print("largest")
elif(b >= c):
    print("second NO largest")
else:
    print("third NO largest")