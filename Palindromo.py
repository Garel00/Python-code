#Palindromo

def voltear_palabra(word):
    if len(word) <= 1:
        return word
    return voltear_palabra(word[-1]) + voltear_palabra(word[:-1])

palabra = "taco"
longitud = len(palabra)
palabra_volteada = (voltear_palabra(palabra))

if palabra == palabra_volteada:
    print("Es palindromo!")
else:
    print("No es palindromo")

palabra2 = "perro"
print(palabra2[:-1])