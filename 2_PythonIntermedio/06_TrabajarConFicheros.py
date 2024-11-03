# FileHandling

# .txt file
import os

#txt_file = open("./PythonIntermedio/myfile.txt", 'r+') #Leer y escribir
txt_file = open("./PythonIntermedio/myfile.txt", 'w+') #escribir
txt_file.write("Hola me llamo pepe\nMi apellido es Guiu\nTengo 30 años")
#print(txt_file.read())
#print(txt_file.read(10))
#print(txt_file.readline())

#print(txt_file.readlines())

#txt_file.write("\nHola")

for iten in txt_file.readlines():
    print(iten)



txt_file.close()
os.remove("./PythonIntermedio/myfile.txt")


# .json
import json

my_json_file = open("./PythonIntermedio/my_file_json.json", 'w+') #crea y escribir, osea borra

json_test = {
    "name":"pepe",
    "surname":"guiu",
    "age":30,
    "language":["java","Kotlin", "Swift"],
    "alias":"H_Trinchera88"
}

json.dump(json_test, my_json_file, indent = 4)
my_json_file.close()

with open("./PythonIntermedio/my_file_json.json") as my_other_file:
    for iten in my_other_file.readlines():
        print(iten)

my_json_file.close()

#json_dict = json.load(open("./PythonIntermedio/my_file_json.json"))
my_json_file_read = open("./PythonIntermedio/my_file_json.json")
json_dict = json.load(my_json_file_read)
print(json_dict)

my_json_file_read.close()

print(json_dict["name"])


#csv file
import csv
my_csv_file = open("./PythonIntermedio/nuevocsv.csv", 'w+')
csv_writer = csv.writer(my_csv_file)
csv_writer.writerow(["name",  "surname_1", "surname_2", "alias"])
csv_writer.writerow(["Josep",  "Guiu", "Silles", "Trinchera88"])
csv_writer.writerow(["Josepvvvv",  1, "Sillesvvvv", "Trinchera88vvvv"])
my_csv_file.close()

with open("./PythonIntermedio/nuevocsv.csv") as my_other_file:
    for iten in my_other_file.readlines():
        print(iten)

with open("./PythonIntermedio/nuevocsv.csv", mode='r', newline='', encoding='utf-8') as archivo_csv:
    lector = csv.reader(archivo_csv)
    
    # Leer encabezados
    encabezados = next(lector)
    print("Encabezados:", encabezados)
    
    # Leer filas
    iterador = 0
    for fila in lector:
        iterador += 1
        if iterador % 2 == 0:
            print("Objeto:     ", fila)  # Imprimir cada fila


#xml
import xml