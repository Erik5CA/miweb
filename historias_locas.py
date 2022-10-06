#concatenar cadneas de caracteres
#Supongamos que queresmos crear una cadena que diga:
#Aprende a programar con _________.

# organizacion = "freeCodeCamp"

# print("Aprende a programar con " + organizacion)
# print("Aprende a programar con {}".format(organizacion))
# print(f"Aprende a programar con {organizacion}") #f-string

#Mad Libs (Historias Locas)

adj = input("Adjetivo: ")
verbo1 = input("Verbo 1: ")
verbo2 = input("Verbo 2: ")
sustantivo_plural = input("Sustantivo plural: ")

madLib = f"¡Programar es tan {adj}! Siempre me emociana porque me encanta {verbo1} problemas. ¡Aprende a {verbo2} con freeCodeCamp y alcanza tus {sustantivo_plural}!"

print(madLib)







