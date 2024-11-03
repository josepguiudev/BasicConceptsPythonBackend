# Funciones de orden superior
from functools import reduce

def sum_one(param_a):
    return param_a + 1

def sum_five(param_a):
    return param_a + 5

def sum_two_values_and_add_value(param_a, param_b, f_sum):
    return f_sum(param_a + param_b)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))


#Closures
print("---------------------------------------")
def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))

def sum_ten(original_values):
    def add(value):
        return value + 10 + original_values
    return add

add_closure = sum_ten(1)

print(add_closure(5))

print((sum_ten(8))(7))

print("---------------------------------------")

# built_in higher order function

numbers = [2, 5, 10, 21, 3, 30]

#map

def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

#Filter

def filter_grater_than_ten(number):
    if number > 10:
        return True
    else:
        return False
    
print(list(filter(filter_grater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


#Reduce

def sum_two_values(param_a, param_b):
    print(param_a)
    print(param_b)
    return param_a + param_b

print(reduce(sum_two_values, numbers))