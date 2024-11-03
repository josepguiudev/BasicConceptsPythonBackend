# Error Types

#Syntax Error

#print "(1 + "")"
print("HELLO")

# Name error

my_untz_variable = 0
try:
    print(my_variable)
except NameError as e:
    print(e)
finally:
    print(my_untz_variable)

# IndexError

my_untz_list = [2, 3, 4]
try:
    print(my_untz_list[5])
except IndexError as e:
    print(e)

# ModulenotFoundError

try:    
    import maths
except ModuleNotFoundError as e:
    print(e)

# AtributeError

import math
try:
    print(math.PI) #El modulo math tiene un atributo per es en minus
except AttributeError as e:
    print(e)

# KeyError

my_other_dict = {"Nombre":"Pepe", "Apellido":"Guiu", "Edad":30, 1:"Python"}

try:
    print(my_other_dict["Edad"])
    print(my_other_dict["Apelido"])
except KeyError as e:
    print(e)

#TypeError

try:
    print(my_untz_list["0"])
except TypeError as e:
    print(e)

# ImportError

try:
    from math import pii
except ImportError as e:
    print(e)

# ValueError

try:
    my_int = int("10 Años")
    print(my_int)
except ValueError as e:
    print(e)


#ZeroDivisioError

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print(e)

print("Se acaba el codigo")