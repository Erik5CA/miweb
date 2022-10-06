class User:
    def __init__(self):
        self.email = input("Introduce tu email: ")
        self.__passwpord = input("Introduce tu contraseña: ")
        self.permissions = ["edit","create","update"]
        
    def setear_username(self):
        self.username = input("Introduzca el username que desea tener: ")
        print("Username cambiado exitoxamente a: {}".format(self.username))
    
    
class UserPro(User):
    def __ini__(self):
        super().__init__()
        self.permissions += ["delete","download"]
    
    def pay_suscription(self):
        print("Usted ha pagado correctamente la suscripcion")
        
    
class UserManager:
    def create_user(self,suscripcion):
        if suscripcion:
            user = UserPro()
        else:
            user = User()
        
        print("Se a creado exitosamente su usuario, Sus permisos son: {}".format(user.permissions))

UserManager().create_user(False)

