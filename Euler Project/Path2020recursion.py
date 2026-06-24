#Path 20x20 by myself
memo = {}
def path(x, y):
	
	if x<0 or y<0:
		return 0
		
	if x == 0 and y == 0:
		return 1
		
	if (x,y) in memo:
		return memo[(x,y)]
	memo[(x,y)] = path(x, y-1) + path(x-1, y)
	return memo[(x,y)]

x=20
y=20
print(path(x, y))
