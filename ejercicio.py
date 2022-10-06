
from unittest import result


def f_max(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2
    
# print(f_max(2,5))

def funcion_max_de_tres(n1,n2,n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
    
# print(funcion_max_de_tres(8,5,2))
# print(funcion_max_de_tres(2,9,4))
# print(funcion_max_de_tres(1,2,3))

def vocal(caracter):
    lista_vocales = ['a','e','i','o','u']
    if caracter in lista_vocales:
        return True
    else:
        return False
    
# print(vocal('a'))
# print(vocal('z'))

def invertir(cadena):
    long = len(cadena)-1 
    cad_inv = str()
    for i in range(-long,1):
        cad_inv += cadena[abs(i)]
    return cad_inv

# invertir("saludos")

def es_palindromo(cadena):
    if cadena == invertir(cadena):
        return True
    else: 
        return False
    
# print(es_palindromo("hola"))

def superposicion(lista1,lista2):
    for elem in lista1:
        if elem in lista2:
            return True
        
    return False

# print(superposicion([1,2,3],[4,4,5]))

def generar_n_caracteres(caracter,n):
    cad = caracter
    for i in range(1,n):
        cad += caracter
    print(cad)
    
# generar_n_caracteres("x",5)

def histograma(lista):
    for i in lista:
        print("*"*n)
        

def tres_cinco():
    for i in range(1,101):
        res = ""
        if i % 3 == 0:
            res = "tres"
        if i % 5 ==0:
            res += " cinco"  
        if res == "":
            print(i)
        else:
            print(res)

# tres_cinco()


def check_palindrome(cadena):
    chars = {}
    for cadena_input in cadena:
        if cadena_input in chars.keys():
            chars[cadena_input] += 1
        else:
            chars[cadena_input] = 1
            cont = 0
    for char_value in chars.values():
        if char_value % 2 != 0:
            cont += 1
        if cont > 1:
            return False
    return True

# print(check_palindrome("civic"))
# print(check_palindrome("ivicc"))
# print(check_palindrome("civil"))
# print(check_palindrome("livci"))
# print(check_palindrome("frafa"))
# print(check_palindrome("dw"))

def check_input(str_input: str):
    chars_result = [0,0,0]
    for char_input in str_input:
        if char_input == "(":
            chars_result[0] += 1
            last_char = char_input
        elif char_input == ")":
            chars_result[0] -= 1
            if chars_result[0] < 0:
                return False
        elif char_input == "[":
            chars_result[1] += 1
            last_char = char_input
        elif char_input == "]":
            chars_result[1] -= 1
            if chars_result[1] < 0:
                return False
        elif char_input == "{":
            chars_result[2] += 1
            last_char = char_input
        elif char_input == "}":
            chars_result[2] -= 1
            if chars_result[2] < 0:
                return False
        else:
            return False
        
    return True

print(check_input("{}"))
print(check_input("{}()[]"))
print(check_input("[{]}"))  
print(check_input("{([])}"))
print(check_input("{(((((()"))