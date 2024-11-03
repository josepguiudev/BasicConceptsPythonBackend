# diccionarios

my_dict = dict()
my_other_dict = {}

print(type(my_dict))
print(type(my_other_dict))

my_other_dict = {"Nombre":"Pepe", "Apellido":"Guiu", "Edad":30, 1:"Python"}
print(my_other_dict)

my_dict = {
    "Nombre":"Pepe", 
    "Apellido":"Guiu", 
    "Edad":30, 
    "Lenguages": {"Python", "Swift", "Kotlin"},
    1: 1.77
    }

print(my_dict)
print(my_other_dict)

print(len(my_other_dict))
print(len(my_dict))

print(my_dict["Nombre"])
print(my_dict[1])
print(my_dict["Lenguages"])

my_dict["Nombre"] = "Pedro"
print(my_dict["Nombre"])

my_dict["Calle"] = "Calleeeeee" #Si no existe  lo añade
print(my_dict)

del my_dict["Calle"]
print(my_dict)

print("Pepe" in my_dict) #busca por clave
print("Nombre" in my_dict)

print(my_dict.items())
print(my_dict.keys())
print(my_dict.values())

my_new_dict = dict.fromkeys(("Nombre", 1, "Piso")) #Creamos un nuevo diccionario con esas claves
print(my_new_dict)

my_new_dict["Nombre"] = "XXX"
my_new_dict[1]= 1.81
print(my_new_dict)

my_list = ["Nombre", 2, "Letra"]
my_new_dict_from_list = dict.fromkeys((my_list))
print(my_new_dict_from_list)

my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict)

my_new_dict = dict.fromkeys(my_dict, "value") #Añade este valor en todas las claves
print(my_new_dict)

print(list(my_new_dict))
print(list(my_new_dict.values()))
print(tuple(my_new_dict))
print(tuple(my_new_dict.values()))
print(set(my_new_dict))
print(set(my_new_dict.values()))

