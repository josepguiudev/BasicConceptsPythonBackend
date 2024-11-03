# Strings

my_string = "Mi string"
my_other_string = 'Mi otra string'

print(len(my_string))
print(len(my_other_string))

print(my_string + " @@@@ " + my_other_string)

my_new_line_string = "Este es un string \ncon salto de linia"
print(my_new_line_string)

my_tab_string = "\teste es un string con tabulacion"
print(my_tab_string)

#Formateo
name, surname, edad = "pepe", "guiu", 30

print("Mi nombre es {} {} y mi edad es {}".format(name, surname, edad))
print("Mi nombre es %s %s y mi edad es %d" %(name, surname, edad))
print(f"Mi nombre es {name} {surname} y mi edad es {edad}")#inferencia de datos

#Desempaquetado de caracteres
language = "python"
a, b, c, d, e, f = language
print(a)
print(b)
print(a, b, c, d, e, f)

#Division o acceso por posiciones
language_slice = language[1:4]
print(language_slice)
language_slice = language[1:]
print(language_slice)
language_slice = language[-2]
print(language_slice)
language_slice = language[0:5:2]
print(language_slice)

#reverse
reversed_language = language[::-1]
print(reversed_language)

#Funciones
print(language.capitalize()) #pone mayus en la primera posición
print(language.upper())
print(language.count("t"))
print(language.isnumeric())
print("1".isnumeric())
print(language.lower())
print(language.lower().isupper())
print(language.startswith("py")) #case sensitive
print(language.startswith("Py"))