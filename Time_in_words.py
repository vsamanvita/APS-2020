#given hours h and minutes m returns the time in words
def timeInWords(h, m):
    li=[
        'one','two','three','four','five','six','seven','eight','nine','ten',
        'eleven','twelve','thirteen','fourteen','quarter','sixteen','seventeen',
        'eighteen','nineteen','twenty','twenty one','twenty two','twenty three',  
        'twenty four','twenty five','twenty six','twenty seven','twenty eight',                  
        'twenty nine','half'
        ]
    res=""
    # res=li[h-1]
    if m==0:
        res=li[h-1]+" o' clock"
    elif m==1:
        res='one minute past '+li[h-1]
    elif m<31:
        res=li[m-1]+' minutes past '+li[h-1]
    elif m==59:
        res='one minute to '+li[h]
    else:
        res=li[60-(m+1)]+' minutes to '+li[h]

    if m==15 or m==45 or m==30:
        res=res.replace(' minutes','',1)

    return res

h=5
m=47
print(timeInWords(h,m))

