#Problema 6 2022
import math

radio = 2.0
islas = [(-2.0, 1.0), (1.0, 2.0), (2.5, 1.0)]

def min_radars(islands, r):
	intervals = []
	radar_count = 0
	last_radar_pos = float('-inf')
	
	for x,y in islands:
		if y > r:
			return -1
		
		half_width = (r**2 + y**2)**(1/2)
		left = x - half_width
		right = x + half_width
		
		intervals.append((right, left))
		intervals.sort()
			
	for right, left in intervals:
		if left > last_radar_pos:
			radar_count += 1
			last_radar_pos = right
		

		
	
	return radar_count

print(min_radars(islas, radio))
