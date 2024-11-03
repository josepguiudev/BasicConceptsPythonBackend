#   sets ventajas --> no acepta repetidos y trabajamos rapido con estructuras no ordenadas

my_set = set()
my_other_set = {}

print(type(my_set))
print(type(my_other_set)) #inicialmente esta variable esta instanciada como variable dict

my_other_set = {"Pepe", "Guiu", 30}
print(type(my_other_set)) #Al poner valores se auto instancia como set

print(len(my_other_set))

my_other_set.add("Trinchera")
print(my_other_set) #un set no es una estructura ordenada, la forma de guardar datos es desordenada

my_other_set.add("Trinchera")
print(my_other_set) #un set no admite repetidos

print("Pepe" in my_other_set)
print("Pepi" in my_other_set)

my_other_set.remove("Pepe")
print(my_other_set)

my_other_set.clear()
print(my_other_set)
print(len(my_other_set))


del my_other_set

my_set = {"Pepe", "Guiu", 30}
my_list = list(my_set)

print(my_list)

my_other_set = {"kotin", "swift", "python", "java"}

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"Java", "JavaScript", "C#"}))

print(my_new_set.difference(my_set))