from itertools import permutations

# Example: Generate permutations of a list
items = [1, 2, 3]
perms = permutations(items)

for perm in perms:
    print(perm)