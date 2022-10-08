
def encriptar(texto):
    print(f"El texto a encriptar es: {texto}")
    textoFinal = ""    
    for letra in texto:
        ascii = ord(letra)
        ascii +=1
        textoFinal += chr(ascii)
    return textoFinal

def desencriptar(texto):
    print(f"El texto a desencriptar es: {texto}")
    textoFinal = "" 
    for letra in texto:
        ascii = ord(letra)
        ascii -=1
        textoFinal += chr(ascii)
    return textoFinal

# desencriptar("Pxrxuxexbxax xdxex xtxexxxtxox")

def encriptarArchivo():
    archivo = open("texto.txt","r")
    texto = archivo.read()
    archivo.close()
    textoEncriptado = encriptar(texto)
    
    archivo = open("texto.txt","w")
    archivo.write(textoEncriptado)
    archivo.close()
    print("El archivo fue encriptado correctamente")
    
def desencriptarArchivo():
    archivo = open("texto.txt","r")
    texto = archivo.read()
    archivo.close()
    textoDesencriptado = desencriptar(texto)
    
    archivo = open("texto.txt","w")
    archivo.write(textoDesencriptado)
    archivo.close()
    print("El archivo fue desencriptado correctamente")

resultado = input("Presione 'E' para encriptar, o 'D' para des encriptar")

if resultado == 'E':
    encriptarArchivo()
else:
    desencriptarArchivo()