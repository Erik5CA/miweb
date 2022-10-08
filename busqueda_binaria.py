import random
import time

def busqueda_ingenua(lista,objetivo):
    for i in range(len(lista)): #retorna la secuencia -> 0,1,2,3...,len(lista)
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista,objetivo,limite_inferior=None,limite_superior=None): #La lista tiene que estar ordenada en forma ascendente
    if limite_inferior is None:
        limite_inferior = 0 #Inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista)-1 #Fin de la lista
    
    if limite_superior < limite_inferior:
        return -1
    
    punto_medio = (limite_inferior + limite_superior) // 2  # "//"" Divide entre dos y retorna solo la parte entera
    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista,objetivo,limite_inferior,punto_medio-1)
    elif objetivo > lista[punto_medio]:
        return busqueda_binaria(lista,objetivo,punto_medio+1,limite_superior)


if __name__=='__main__': ##Queremos que el codigo se ejecute solo cuando no importamos este archivo o modulo
    #Crearu una lista ordenada con 10000 numeros aleatorios
    tamaño = 100000
    conjunto_inicial = set()
    
    while len(conjunto_inicial) < tamaño:
        conjunto_inicial.add(random.randint(-3*tamaño,3*tamaño))
    
    lista_ordenada = sorted(list(conjunto_inicial))
    
    #Medir el tiempo de busqueda ingenua.
    # inicio = time.time()
    # for objetivo in lista_ordenada:
    #     busqueda_ingenua(lista_ordenada,objetivo)
    # fin = time.time()
    # print(f"Tiempo de busqueda ingenua: {fin-inicio} segundos.")
    
    #Medir el tiempo de busqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada,objetivo)
    fin = time.time()
    print(f"Tiempo de busqueda binaria: {fin-inicio} segundos.")