# Exceptions

number_one = 5
number_two = "5"
#number_two = 5

try:
    print(number_one + number_two)
    print("No se ha producido errores logicos")
except:
    print("Problemas --> el tipo de dato de valor 1 es " + str(type(number_one)) + " y el tipo de valor 2 es " + str(type(number_two)))
    print("Los valores tienen que ser " + str(int))

number_two = 5

try:
    print(number_one + number_two)
    print("No se ha producido errores logicos")
except: #no opcional
    print("Problemas --> el tipo de dato de valor 1 es " + str(type(number_one)) + " y el tipo de valor 2 es " + str(type(number_two)))
    print("Los valores tienen que ser " + str(int))
else: #Ejecucion en caso de no error, opcional
    print("Al no fallar la suma entra en el else")
finally: #Ejecucion siempre, opcional
    print("Printeo final")


print("Sigue la ejecucion")

#Excepciones por tipo

number_two = "5"

try:
    print(number_one + number_two)
    print("No se ha producido errores logicos")
except ValueError:
    print("Se ha producido un error de TypeError")
except TypeError: #Solo si es typeerror hay mas, busca por error
    print("Se ha producido un error de TypeError")
    print("Cambiando valores.....")
    print(int(number_one) + int(number_two))
    print("SOLUCIONADO")

# Captura de la informacion del error
print("------------------------------------------------------------------------------------------------------")

try:
    print(number_one + number_two)
    print("No se ha producido errores logicos")
except Exception as e:
    print(e)