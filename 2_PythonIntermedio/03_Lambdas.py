# LAMBDAS son funciones anonimas

sum_two_values = lambda first_value, second_value: first_value + second_value
print(sum_two_values(2, 3))
    
multiply_values = lambda first_value, second_value: (first_value * second_value) -3
print(multiply_values(2, 4))

def sum_three_values(param_a):
    return lambda first_value, second_value: first_value + second_value + param_a
 
print(sum_three_values(5)(2,4))
