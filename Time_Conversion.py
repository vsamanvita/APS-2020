# Given a time in 12-hour AM/PM format, converts it to military (24-hour) time.
def timeConversion(s):
    t=s.split(':')
    at=s[len(s)-2:]
    if at=="PM" and t[0]!="12":
        t[0]=str(int(t[0])+12)
    if at=="AM" and t[0]=="12":
        t[0]="00"
    c=":".join(t)
    c=c[:len(c)-2]
    return(c)

print(timeConversion("08:05:45PM"))