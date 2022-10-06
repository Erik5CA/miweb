from ssl import PEM_cert_to_DER_cert


class Perros:
    #constructor
    def __init__(self,nombre,raza,color):
        self.tamaño = None
        self.edad = 0
        self.color = color
        self.raza = raza
        self.nombre = nombre
    
    def ladra(self):
        print("{} esta ladrando".format(self.nombre))
    def comer(self):
        print("{} quiere comer".format(self.nombre))
    def jugar(self):
        print("{} esta jugando".format(self.nombre))

    #Setter
    def cambiar_nombre(self,nombre):
        self.nombre = nombre
        
    def set_edad(self,edad):
        self.edad = edad
        print("{} ahora tiene {} años".format(self.nombre,self.edad))
        
    def cumpleaños(self):
        self.edad += 1
        print("{} ahora tiene {} años".format(self.nombre,self.edad))
        


mi_perro = Perros("Tommy","Dalmata","Blanco y Negro ")
mi_perro.comer()
print(mi_perro.nombre)

mi_perro2 = Perros("Rex","Pitbull","Marron")
mi_perro2.jugar()

mi_perro2.set_edad(10)