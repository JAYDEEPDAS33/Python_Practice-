#WARF to print all elements in a list.

def print_list(list, idx):
    if (idx >= len(list)):
        return
    else:
        print(list[idx])
        print_list  (list, idx + 1)
fruits = ["apple", "banana", "cherry", "date"]
print("Fruits in the list:")
print_list(fruits, 0)