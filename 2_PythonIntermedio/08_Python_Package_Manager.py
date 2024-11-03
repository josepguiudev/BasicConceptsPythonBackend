# Modulos de fuera python

# vamos a usar una herramienta, pip --> https://pypi.org/project/pip/

#"""
#Primero comprobar si tenemos pip (por consola)
#    pip --version
#En caso de no tenerlo
#    curl -O https://bootstrap.pypa.io/get-pip.py
#    intalar con python
#    ponerse en la ruta c:\Users\josep\AppData\Local\Programs\Python\Python312\Scrips
#    poner comando .\py ya que no hay ruta de la path 

#    SINO PONER EN VARIABLES DE ENTORNO DEL SISTEMA PATH estas dos rutaas
#    c:\Users\josep\AppData\Local\Programs\Python\Python312
#    c:\Users\josep\AppData\Local\Programs\Python\Python312\Scrips
#"""

import numpy

import mypackage.arithmetics

print(numpy.version.version)

num = numpy.array([23, 23, 32, 32, 435, 566])
print(num * 2)

import requests
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
print(response)
print(response.status_code)
print(response.json())


#Paquete arithmetics
from mypackage import arithmetics

print(arithmetics.sum_two_values(5,5))