##Project Euler Problem 1
##Sum of multiples of 3 or 5 below 1000
counting = 0
total_sum = 0
while counting < 1000:
	module3 = counting % 3
	module5 = counting % 5
	if module3 == 0:
		total_sum += counting
	elif module5 == 0:
		total_sum += counting
	counting += 1

print(total_sum)