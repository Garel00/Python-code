#Reversin a string

def reverse(word):
    if len(word) == 1:
        return word
    return word[-1] + reverse(word[:-1])

print(reverse("hola"))
palabra = "hellouu"
print(palabra[1:])