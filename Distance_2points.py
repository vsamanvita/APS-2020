# Program to calculate distance between two points 

# Euclidean distance
import math 
 
def distance(x1 , y1 , x2 , y2): 
	return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)) 

print(distance(3, 4, 4, 3)) 

# Manhattan Distance
def manhattan(x1, y1, x2, y2):
	return abs(x1-x2)+abs(y1-y2)

print(manhattan(3, 4, 4, 3))