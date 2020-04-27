#prints all Kaprekar numbers in a given range,print invalid range if no number is present
#Kaprekar number-representation of whose square can be split into two parts that add up to the original number again
#45 is Kaprekar number 45**2=2025,20+25=45
def kaprekarNumbers(p, q):
    flag=0
    for i in range(p,q+1):
        sq=str(i**2)
        f=sq[:len(sq)//2]
        l=sq[len(sq)//2:]
        if f=="":
            f="0"
        elif l=="":
            l="0"
        if i==int(f)+int(l):
            print(i,end=' ')
            flag=1
    if flag==0:
        print("Invalid Range")

kaprekarNumbers(1,100)



