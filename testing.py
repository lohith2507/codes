from itertools import permutations
from itertools import combinations

# Example: Generate permutations of a list
items = [1, 2, 3]
perms = permutations(items)

for perm in perms:
    print(perm)

# Example: Generate permutations of a string
string = "abc"
string_perms = permutations(string)
for perm in string_perms:    
    print(''.join(perm))

    # Example: Generate combinations of a list
    items = [1, 2, 3]
    combs = combinations(items, 2)

    for comb in combs:
        print(comb)

    # Example: Generate combinations of a string
    string = "abc"
    string_combs = combinations(string, 2)
    for comb in string_combs:
        print(''.join(comb))