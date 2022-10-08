#Calculadora de ICM
#ICM = Peso /(Altura/Altura)
#< 19 : delgadez
#entre 20 y 25 : normal
#entre 26 y 30 : sobrepeso
#>30 : obesidad

def calcularICM(peso,altura):
    altura_m = altura/100
    icm = peso/(altura_m*altura_m)
    print(f"Su ICM es de: {icm}")

    if icm < 20:
        print("Estado de delgadez")
    if icm >= 20 and icm < 26:
        print("Estado normal")
    if icm >= 26 and icm < 30:
        print("Estado de sobrepeso")
    if icm >= 30:
        print("Estado de obesidad")
        
peso = float(input("Ingese su peso en kg: "))
altura = int(input("Ingese su altura en cm: "))

calcularICM(peso,altura)
