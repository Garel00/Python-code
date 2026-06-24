#Problem 2 2024

#Valor test
A = (2,3)

def ackerman(m,n):
	if m == 0:
		return n+1
	elif n == 0:
		return ackerman(m-1, 1)
	else:
		return ackerman(m-1, ackerman(m, n-1))
	
	
m = A[0]
n = A[1]
print(ackerman(m, n))
