# List Comprehension -- crear lista rapido o en base a listas que ya temos

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_list = [i for i in range(8)]
my_range = range(8)
print(my_range)
print(list(my_range))

print(my_list)


def sum_file(number):
    return number + 5

my_other_list = [sum_file(i) for i in range(8)]
#my_other_list = [i + 1 for i in range(8)]
print(my_other_list)