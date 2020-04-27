#prints all the move to move each disk
#'n'disks need (2^n)-1 moves
def toh(source,temp,dest,n):
	if n==1:
		print("Move disk  1 from ",source,"to ",dest)
	else:
		toh(source,dest,temp,n-1)
		print("Move disk ",n,"from ",source,"to ",dest)
		toh(temp,source,dest,n-1)

n=4
toh('A','B','C',n)