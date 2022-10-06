
class Animal:
    def __init__(self):
        self.edad = None
        self.especie = None
        self.pelaje = None
    
    def comer(self):
        print("El animal esta comiendo")
    
    
    def reproducirse(self):
        print("El animal se esta reproduciondo")
    
class Perro(Animal):
    def __init__(self):
        super().__init__()
        self.tamaño = None
        self.raza = None
        self.nombre = None
    
    def ladra(self):
        print("{} esta ladrando".format(self.nombre))
        
    def jugar(self):
        print("{} esta jugando".format(self.nombre))
    
    def comer(self):
        print("{} quiere comer".format(self.nombre))
        
    def check_hambre(self,hambre):
        if hambre:
            self.comer()
        else:
            print("{} no esta hambriento".format(self.nombre))

tommy = Perro()
tommy.reproducirse()
print(tommy.edad)
tommy.check_hambre(True)
tommy.check_hambre(False)