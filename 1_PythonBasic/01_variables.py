my_variable = 'My string variable'
print(my_variable)

my_int_variable = 1
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_int_to_str_varibale = str(my_int_variable)
print(my_int_to_str_varibale)
print(type(my_int_to_str_varibale))

#concatenar variables
print(my_variable, my_int_to_str_varibale , my_bool_variable)
print("Este es el valor de:", my_bool_variable)

#Algunas funciones del sistema
print(len(my_variable))

#variables en una sola linia
name, surname, alias, age = "Mario", "Gonzalez", "Mario_G", 30.01 #NO ES BUENA PRACTICA
print("Edad:", age, ", apellido:", surname, ", nombre:", name, ", alias:" , alias)

#input por consola
input_first_name = input("Whats your name? ")
input_age = input("How old are you? ")

print("El input ha sido realizado, nombre -->", input_first_name, "edad -->", input_age)

#anteriormente se han variado los valores de las variables, pero una variable puede cambiar el tipo
input_first_name = 123
input_age = False

print(input_first_name, type(input_first_name), input_age, type(input_age))

#para hacer un tipo de variable es
address: str = "mi direccion" #--> solo ayuda a que entendamos que queremos esa variable como string
#Tiene mas sentido ponerlo en un input 
#pero se puede volver a cambiar el tipo de la variable
address = 32
print(address, type(address))

