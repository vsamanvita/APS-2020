#Gives whether a given year is leap year or not.
def leap(i):
	if i%400==0 or (i%100!=0 and i%4==0):
		print("Leap year")
	else:
		print("Not leap year")
         

# y=1000
# leap(y)