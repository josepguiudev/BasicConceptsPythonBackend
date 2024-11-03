# Regular expresions

#MATCH
import re

my_string = "Esta es la lección número 7: Lección llamada Expresiones regulares"
my_other_string = "Esta no es la lección número 7: Expresiones regulares"

#Empieza a buscar desde el principio de la cadena
match = re.match("esta es la lección", my_string, re.I)#Ignora el upper y lower
print("---------------------------------------")
print(match)
start, end = match.span() 
print(start, end)
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
#if not(match == None):
#if match != None:
if match is not None:
    print(match)
    start, end = match.span() 
    print(my_other_string[start:end])

print(re.match("Expresiones regulares", my_string))
print(re.match("Expresiones regulares", my_string))


#SEARCH
print("---------------------------------------")
search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span() 
print(my_string[start:end])

#Findall
print("---------------------------------------")
find_all = re.findall("lección", my_string, re.I)
print(find_all)

#Split
print("---------------------------------------")
split = re.split(":", my_string, re.I)
print(split)

#SUB
print("---------------------------------------")
sub = re.sub("Expresiones regulares", "REGEX", my_string)
sub = re.sub("[l|L]ección", "LECCION", my_string)
print(sub)


#Patrones Propios

pattern_a = r"[l|L]ección"
print(re.findall(pattern_a, my_string))

pattern_a = r"[l|L]ección|Expresiones"
print(re.findall(pattern_a, my_string))

pattern_a = r"[a-z]"
print(re.findall(pattern_a, my_string))

pattern_a = r"[0-9]"
print(re.findall(pattern_a, my_string))
print(re.search(pattern_a, my_string))

pattern_a = r"\d"
print(re.findall(pattern_a, my_string))

pattern_a = r"\D"
print(re.findall(pattern_a, my_string))

pattern_a = r"[l]."
print(re.findall(pattern_a, my_string))

pattern_a = r"[l].*"
print(re.findall(pattern_a, my_string))

pattern_a = r""
print(re.findall(pattern_a, my_string))

#email validatio regex

email = "josep.guiu.s@gmail.com"
#pattern_email = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$" #para nacionalizar [com|es|cat] --> $
#modificacion propia
pattern_email = r"^[a-zA-Z0-9_.%+-ñÑáéíóúÁÉÍÓÚ]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
print(re.match(pattern_email, email))
print(re.search(pattern_email, email))
print(re.findall(pattern_email, email))

email = "josep@gmail.com"
print(re.findall(pattern_email, email))

#https://regex101.com/ mejor web