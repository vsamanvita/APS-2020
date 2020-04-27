#Identifies whether a string is pangram or not
def pangrams(s):
    s=s.replace(" ","")
    s=s.lower()
    s=set(s)
    if len(s)==26:
        return "Pangram"
    return "Not Pangram"

a="We promptly judged antique ivory buckles for the prize"
print(pangrams(a))