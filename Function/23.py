#WAF to print the elements of a list in a single line
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
heroes = ['Superman', 'Batman', 'Flash', 'Aquaman']



def print_length(list):
    print("Length of the list is:", len(list))

def print_list(list):
    for item in list:
        print(item, end=' ')
print_list(cities)
print_list(heroes)
