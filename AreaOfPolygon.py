# Shoelace formula to evalute the area of the polygon given X and Y co-ordinates.

def polygonArea(X,Y):
	area=0
	n=len(X)
	j=n-1
	for i in range(0,n):
		area+=(X[j]+X[i])*(Y[j]-Y[i])
		j=i

	return int(abs(area/2))