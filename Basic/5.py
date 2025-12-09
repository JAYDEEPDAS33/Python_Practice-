#WAP to check if a list contains palindrome or not
list1 = [1, 2, 3, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("The list contains palindrome")
else:
    print("The list does not contain palindrome")
