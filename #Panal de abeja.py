#Panal de abeja
memo = {}

def panal_abeja(n):
    posicion = n
    if posicion in memo:
        return memo[posicion]
    
    if n == 0:
        return 1
    
    if n<0:
        return 0
    
    memo[posicion] = panal_abeja(n-1) + panal_abeja(n-2) + panal_abeja(n-3)

    return memo[posicion]

print(panal_abeja(3))