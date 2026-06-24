#Problema 5 2023
#Volteador de palabras con recursion!!

def volteador(palabra):
    if len(palabra) == 1:
        return palabra

    return volteador(palabra[1:]) + palabra[0]

print(volteador("cimat"))
