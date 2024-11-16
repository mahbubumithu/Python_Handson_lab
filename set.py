my_set = {1, 2, 3}
print(my_set)
my_set.add(4)  # Adds 4 to the set
my_set.update([5, 6])  # Adds 5 and 6 to the set

print(my_set)

my_set.remove(3)  # Removes 3 from the set

print(my_set)
other_set = {3, 4, 7}
union_set = my_set.union(other_set)  # {1, 2, 4, 5, 6, 7}

print(union_set)
intersection_set = my_set.intersection(other_set)  # {4}

print(intersection_set)