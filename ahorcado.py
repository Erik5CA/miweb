import imp
from palabras import palabras
import random
import string #Modulo para trabajar con strings
from ahorcado_diagramas import vidas_diccionario_visual

def obtener_palabra_valida(palabras):
    #selecionar una palabra al azar de la lista de palabras
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def ahorcado():
    print("===============================")
    print("Bienvenido a juego del ahorcado")
    print("===============================")
    
    palabra = obtener_palabra_valida(palabras)
    
    letras_por_adivinar = set(palabra) #Conjunto con las letras a adivinar
    letras_adivinadas = set() #Conjunto vacio
    abecedario = set(string.ascii_uppercase) ##No contiene la ñ 
    
    vidas = 7
    
    while len(letras_por_adivinar) > 0 and vidas > 0:
        #Letras adivinadas
        #' '.join({'A','B','C'}) -> 'A B B'
        print(f"Te quedan {vidas} vidas y has usado estas letras: {' '.join(letras_adivinadas)}")
        #Mostrar el estado actual de la palabra
        palabra_lista = [letra if letra in letras_adivinadas else '-' for letra in palabra]
        #Mostrar esta del ahorcado
        print(vidas_diccionario_visual[vidas])
        #Mostrar letras separadas por -
        print(f"Palabra: {' '.join(palabra_lista)}")
        
        letra_usuario = input("Escoge una letra: ").upper()
        
        #Si la letra escogidfa por el usuario esta en el abecedario y no esta en el conjunto de letras que ya se han ingresado se añade la letra a el conjunto de letras ingresadas
        if letra_usuario in abecedario - letras_adivinadas:
            letras_adivinadas.add(letra_usuario)
            #Si la letra esta en la palabra, quitar la letra del conjunto de letras por adivinar, si no quitar una vida
            if letra_usuario in letras_por_adivinar:
                letras_por_adivinar.remove(letra_usuario)
                print("")
            else:
                vidas -= 1
                print(f"\nTu letra, {letra_usuario} no esta en la palabra.")
        elif letra_usuario in letras_adivinadas: #Si la letra escogida por el usuario ya fue ingresada
            print("\nYa escogiste esa letra. Por favor escoge una letra nueva.")
        else:
            print("\nEsta letra no es valida")
    #El juego llega a esta linea cuando se adivina todas la letras de la palabra o cuando se agotan las vidas del jugador
    if vidas == 0:
        print(vidas_diccionario_visual[vidas])
        print(f"AHORCADO. Perdiste. La palabra era: {palabra}")
    else:
        print(f"Excelente. Adivinaste la palabra: {palabra}")


ahorcado()