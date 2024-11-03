# condicionales 

my_condition = False

if my_condition:
    print("hola")
print("Primer if realizo")

my_condition = 5*2

if my_condition == 10:
    print("hola")
else:
    print("adios")
print("Segundo if realizo")    

if my_condition == 10:
    print("hola")
elif my_condition == 11:
    print("Es 11!")
else:
    print("adios")

my_condition = 5*3

if my_condition > 10 and my_condition < 20:
    print("Mayor a diez y menor a 20")
else:
    print("Es menor o igual que 10 o mayor o igual que 20")


    print("Es menor o igual que 10 o mayor o igual que 20")


print("hasta aqui la ejecucion")

my_string = ""
if not my_string: #es como el ! de java
    print("Mi cadena de texto es vacia")


# Ejemplo de uso
def case_example(value):
    match value:
        case 1:
            return "Caso 1"
        case 2:
            return "Caso 2"
        case 3:
            return "Caso 3"
        case _:
            return "Caso por defecto"
        
resultado = case_example(2)
print(resultado)  # Salida: Caso 2


