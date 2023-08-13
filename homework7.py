print(sum([x ** 2 for x in range(0, 101)]))  # task 1

print(len([1 for x in range(1, 21) if x % 2 == 0]))  # task 3

a = [64, 8, 72, 1, 56, 78, 7, 59, 9, 80]
a = a[::2]
print(len([x for x in a if x % 2 == 0]))
