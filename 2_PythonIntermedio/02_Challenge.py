# EJERCICIOS
"""
Crear por pantalla salida de numeros del 1 al 100 y:
multiplos de 3 por la palabra fizz
multiplos de 5 por la palabra buzz
multiplos de 3 y 5 a la vez por la palabra fizzbuzz
"""
def multiplo_3 (number):
    return number % 3 == 0

def multiplo_5 (number):
    return number % 5 == 0

def multiplo_3_5 (number):
    return number % 3 == 0 and number % 5 == 0 

def printeo(number, indice):
    match indice:
        case 1:
            print(str(number) + " fizzbuzz")
        case 2:
            print(str(number) + " fizz")
        case 3:
            print(str(number) + " buzz")
        case _:
            print(number)

def fizzbuzz():
    for index in range(1, 101):
        if multiplo_3_5(index):
            printeo(index, 1)
        elif multiplo_3(index):
            printeo(index, 2)
        elif multiplo_5(index):
            printeo(index, 3)
        else:
            printeo(index, 4)
fizzbuzz()


"""
escribir funcion que reciba por parametro una string y devuelva un true o false segun si es un anagrama
- Un anagrama consiste en formar una palabra reordenando todas las letras de otra palabra inicial
- no hace falta comprobar que ambas palabras existan
- dos palabras exactamente iguales no son anagramas
"""
def is_anagram(text_one, text_2):
    if (text_one.lower()) == (text_2.lower()):
        return False
    print(sorted(text_one.lower()))
    print(sorted(text_2.lower()))
    return sorted(text_one.lower()) == sorted(text_2.lower())
print(is_anagram("amor", "roma"))
print(is_anagram("castor", "castro"))


"""
Escribe un programa que imprima los 50 primeros numeros de la sucesion de fibonacciempezando en 0
la serie de fibonacci se compone por una sucesion de numeros en la que el siguiente siempre es
la suma de los anteriores
0, 1, 1, 2, 3, 5, 8, 13...
"""
def fibonacci():
    prev = 0
    next = 1
    for index in range(51):
        print(index)
        print(prev)
        fib = prev + next
        prev = next
        next = fib
fibonacci()    


#Es numero primo? del 1 al 100 marcando cuales son los primos
def is_prime():
    for number in range(1, 101):
            if number >= 2:          
                is_divisible = False
                for index in range(2, number):
                    if number % index == 0:
                        is_divisible = True                  
                if not is_divisible:
                    print(number)
is_prime()


"""
cea un  programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguage que lo hagan de forma automatica
Si le pasamos "Hola mundo" nos tien que devolver "odnum aloH"
"""
def invertir_cadena(text):
    text_len = len(text)
    new_text = ""

    for index in range(0, text_len):
        new_text += text[text_len - index - 1]
    return new_text

print(invertir_cadena("Hola mundo"))