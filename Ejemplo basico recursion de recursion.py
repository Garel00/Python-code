#Ejemplo basico recursion de recursion

def countdownenup(number):
    print(number)
    if number == 0:
        #base case
        print("Reched the base case")
        return
    else:
        #Recursive case
        countdownenup(number-1)
        print(number, "returning")
        return
    
countdownenup(3)