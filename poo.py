from multiprocessing.heap import Arena


class Persona():
    def __init__(self,nombre,apellido,dni,telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.telefono = telefono
    
    def __str__(self):
        return self.nombre + " " + self.apellido + " " +self.dni

class Empleado(Persona):
    def __init__(self,nombre,apellido,dni,telefono,salario):
        super().__init__(nombre,apellido,dni,telefono)
        self.salario = salario

    
class Cliente(Persona):
    def __init__(self,nombre,apellido,dni,telefono,categoria):
        super().__init__(nombre,apellido,dni,telefono)
        self.categoria = categoria
        
emp = Empleado("Lucas","Moy","123123","23423423",1000)
emp = Cliente("Lucas","Moy","123123","23423423","vip")

print(emp)