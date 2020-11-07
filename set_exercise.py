all_numbers_list = [i for i in range(0, 10)]
even_numbers_list = [i for i in range(0, 10) if i % 2 == 0]

all_numbers_set = set(all_numbers_list)
even_numbers_set = set(even_numbers_list)


# all_numbers_set.add(7)
# all_numbers_set.remove(3)
# all_numbers_set.update([11, 12, 13])

# odd_numbers_set = all_numbers_set - even_numbers_set
odd_numbers_set = all_numbers_set.difference(even_numbers_set)

new_set = all_numbers_set.intersection(even_numbers_set)

print(all_numbers_set)
print(even_numbers_set)
print(odd_numbers_set)
print(new_set)
