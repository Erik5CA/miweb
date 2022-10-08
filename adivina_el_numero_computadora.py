import random

def adivina_el_numero_computadora(x):
    print("Bienvenido al juego")
    print(f"Seleciona un número entre 1 y {x} para que la computadora intente adivinarlo")
    
    limite_inferior = 1 
    limete_superior = x
    
    respuesta = ""
    while respuesta != "c":
        #Generar una prediccion
        if limite_inferior != limete_superior:
            prediccion = random.randint(limite_inferior,limete_superior)
        else:
            prediccion = limite_inferior # tambien podria ser el limite superior.
        
        #Obtener una respuesta del usuario
        respuesta = input(f"Mi prediccion es: {prediccion}. Si es muy alta, ingresa (A). Si es muy baja, ingresa (B). Si es correcta, ingresa (C): ").lower()
        print(respuesta)
        if respuesta == "a":
            limete_superior = prediccion - 1
        elif respuesta == "b":
            limite_inferior = prediccion + 1
    
    print(f"La computadora adivino tu numero correctamente: {prediccion}.")
    
adivina_el_numero_computadora(10)
