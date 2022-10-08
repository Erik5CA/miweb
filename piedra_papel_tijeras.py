import random

opciones = {
    "ti" : "Tijeras",
    "pi" : "Piedra",
    "pa" : "Papel"
}

def jugar():
    usuario = input("Escoge una opcion: 'pi' para piedra, 'pa' para papel o 'ti' para tijeras.\n").lower()
    computadora = random.choice(['pi','pa','ti'])
    
    # if usuario == computadora:
    #     #return '¡Empate!'
    #     print(f"Empataste. Tu: {opciones[usuario]}. La computadora: {opciones[computadora]}")

    
    res = gano_el_jugador(usuario,computadora)
    if res:
        #return '¡GANASTE!'
        print(f"Ganaste. Tu: {opciones[usuario]}. La computadora: {opciones[computadora]}")
    elif res == None:
        print(f"Perdiste. Tu: {opciones[usuario]}. La computadora: {opciones[computadora]}")
    else:
        print(f"Empataste. Tu: {opciones[usuario]}. La computadora: {opciones[computadora]}")
    #return '¡Perdiste! :('


def gano_el_jugador(jugador,oponente):
    #Retorna true si gana el jugador
    #Piedra gana a Tijera (pi > ti)
    #Tijera gana a Papel (ti > pa)
    #Papel gana a Piedra (pa > pi)
    if ((jugador == 'pi' and oponente == 'ti') or
        (jugador == 'ti' and oponente == 'pa') or
        (jugador == 'pa' and oponente == 'pi')):
        return True
    elif jugador == oponente:
        return False
    else:
        return None


jugar()