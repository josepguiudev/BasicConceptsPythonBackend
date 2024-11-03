### FUNCTIONS ###

def my_function_initial():
    print("HOLA DESDE FUNCION")


def my_function():
    print("HOLA DESDE FUNCION")
    return 3

my_int = my_function()

print("int final " + str(my_int))

def sum_two_values(a, b):
    return a+b

my_suma = sum_two_values(int("2"), int("2"))
print("Funcion de suma --> " + str(my_suma))


def print_name(name, surname):
    print(f"{name} {surname}")


print_name(surname="Guiu", name="Pepe")

def print_name_default(name, surname, alias = "Sin alias"):
    print(f"{name} {surname} {alias}")

print_name_default("Pepe", "Guiu")

def print_texts(*text):
    my_new_chain = ""
    for element in text:
        my_new_chain += element.upper() + " "
    print(my_new_chain)

print_texts("Hola", "mundo", "como", "va")

