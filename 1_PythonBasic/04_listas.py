#Listas 
my_list = list()
my_other_list = []

print(len(my_list))

my_list = [10, 11, 12, 13, 14, 15, 11]
print(my_list)
print(len(my_list))
print(type(my_list))

my_other_list = [30, 1.70, "pepe", "guiu"]
print(my_other_list)
print(len(my_other_list))
print(type(my_other_list))

print(my_other_list[0])
print(my_other_list[len(my_other_list)-1])
print(my_other_list[-1])

#count
print(my_list.count(11))

#asignacion a variables por posiciones de la lista tiene que haber tantas var como posiciones
age, height, name, surname = my_other_list
print(name)
name, height, age, surname = my_other_list[2], my_other_list[1], my_other_list[0], my_other_list[3]
print(name)

print(my_list + my_other_list)

my_other_list.append("nuevo elemento")
print(my_other_list)

my_other_list.insert(1, "1.77")
print(my_other_list)

my_other_list[1] = "1.91"
print(my_other_list)

my_other_list.remove("nuevo elemento")
print(my_other_list)

print(my_list)
my_list.remove(11)
print(my_list)

print(my_list.pop())
print(my_list)
print("------------------")
my_pop_element = my_list.pop(2)
print(my_list)

del my_list[2]
print(my_list)

my_new_list = my_list.copy()

my_list.clear()
print(my_list)
print(my_new_list)

my_new_list.reverse()
print(my_new_list)

my_new_list.sort()
print(my_new_list)

print(my_new_list[1:3])

my_list = "Hola Python"
print(my_list)
print(type(my_list))

print(my_other_list.index("pepe"))