# search for a number x in this tuple using loop

nums = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100,36)
x = 36
idx = 0
for num in nums:
    if num == x:
        print("Number found at index:", idx)
        break
    idx += 1