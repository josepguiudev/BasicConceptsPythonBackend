# Clases.py
# Clases van con camel case

class MyEmptyPerson:
    pass

print(MyEmptyPerson())

class MyPerson:
    def __init__(self, name, surname, alias = "Sin alias"):
        self.__name = name #Para hacer publica la propiedad sin los guiones bajos
        self.__surname = surname
        self.__alias = alias

    #GETTER
    def get_name(self):
        return self.__name
    def get_surname(self):
        return self.__surname

    #SETTER
    def set_name(self, new_name):
        self.__name = new_name
    
    def set_alias(self, new_alias):
        self.__alias = new_alias

    def mostrar_info(self):
        return f"{self.__name} {self.__surname} ({self.__alias})"  # Método que devuelve información del person
    
    def walk(self):
        return(f"{self.mostrar_info()} esta andando")