#Bucles

#While
my_condition = 0

while my_condition <= 10:
    print(my_condition)
    my_condition += 4
else:
    print("mi condicion es igual o mayor a diez --> " + str(my_condition))

print("la ejecucion continua")

while my_condition < 20:
    my_condition += 1
    
    if my_condition == 15:
        print("Mi condicioin es igual a 15")
        break
    else:
        print("Mi condicion supera a 15")

    print("Mi condicion es menor que 20")

print("la ejecucion continua")

#for

my_list = [35, 24, 62, 52, 30, 30, 17]

for element in my_list:
    print(element)
    print(str(element) + " --")

my_tuple = (35, 1.77, "x", "y", "z")
my_set = {"Pepe", "Guiu", 30}
my_dict = {"Nombre":"Pepe", "Apellido":"Guiu", "Edad":30, 1:"Python"}

for element in my_tuple:
    print(element)
for element in my_set:
    print(element)
for element in my_dict:
    print(element)
for element in my_dict.values():
    print(element)
    if(element == 30):
        print("Se ha encontrado")
        break 
else:
    print("Ha finalzado")

    