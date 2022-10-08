
from datetime import datetime


def remplazar(text,companyName):
    resultado = text.replace("[COMPANY_NAME]",companyName)
    resultado = resultado.replace("[CURRENT_DATE]",datetime.today().strftime("%Y-%m-%d"))
    resultado = resultado.replace("[EMPLOYEE_NAME]","Erik Castillo")
    resultado = resultado.replace("[CITY]","Ciudad de Mexico")
    resultado = resultado.replace("[COUNTRY]","Mexico")
    resultado = resultado.replace("[PRICE]","1")
    return resultado

contratoArchivo = open("contrato.txt","r")

companyName = input("Cual es el nombre de la Compañia: ")

resultado = ""
for fila in contratoArchivo:
    resultado += remplazar(fila,companyName)

with open("contrato_final.txt","w") as archivo:
    archivo.write(resultado)

