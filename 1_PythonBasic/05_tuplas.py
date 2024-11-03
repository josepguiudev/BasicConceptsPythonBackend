# tuplas

my_tuple = tuple()
my_other_tuple = ()

my_tuple = (30, 1.77, "Pepe", "Guiu", "Pepe")
my_other_tuple = (35, 60, 30)

print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])

print(my_tuple.count("Pepe"))
print(len(my_tuple))
print(my_tuple.index("Guiu"))
print(my_tuple.index("Pepe"))

#En las tuplas no se pueden modificar ni añadir valores

#my_tuple[1] = 1.80 --> 'tuple' object does not support item assignment
my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

print(my_sum_tuple[3:6]) #mostrar elementos entre esos indices 3 y 6 --> posiciones 3, 4 y 5

my_tuple = list(my_tuple) #lo pasamos a lista y aqui ya se puede modificar valores
print(my_tuple)
print(type(my_tuple))

my_tuple[4] = "email"
my_tuple.insert(1, "Azul")

my_tuple = tuple(my_tuple)
print(my_tuple)
print(type(my_tuple)) #lo devolvemos a tipo tupla 

#borrado incoherente pero funciona
del my_tuple
