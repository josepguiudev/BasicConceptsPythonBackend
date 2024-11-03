#operadores aritmeticos de python
print(3+4)
print(3-4)
print(3*4)
print(3/4)
print(10%2)
print(10//3) #aproxima a un numero entero flordivision
print(2**3) #2 elevado a 3
print(2**3 + 3 - 7 / 1 // 4)

print("Hola" + " " + "Python")
print("Hola " + str(5))

print("Hola" * 5 * (2**3))

my_int = 2.5 * 2
print("hola" * int(my_int)) # si lo ponemos sin castear my_int tiene valor de 5.0 cosa que no dej poner la operacion

#Operadores comparativos
print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(3 <= 4)
print(3 == 4)
print(3 != 4)
print(3 < 4 == 2)

#Operadores comparativos
#Comprueba una ordenacion alfabetica por ASCII no por length
print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Python")
print("Hola" != "Python")
print("aa" > "b")
#Comprueba por length mediante la funcion len()
print(len("aa") > len("b"))

#operadores logicos
print(3 > 4 and "Hola" > "Python") #En java &&
print(3 > 4 or "Hola" > "Python")  #En java ||
print(3 < 4 and "Hola" < "Python")  
print(3 < 4 or "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))

print(not(3 > 4)) #En java !