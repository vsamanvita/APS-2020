key=7
def encrypt_text(s):
	global key
	encrypt=""
	for i in s:
		a=(ord(i)^key)
		encrypt+=chr(a)
	return(encrypt)

def decrypt_text(s):
	global key
	decrypt=""
	for i in s:
		a=(ord(i)^key)
		decrypt+=chr(a)
	return(decrypt)


encrypted=encrypt_text("Algorithm Problem Solving")
print(encrypted)
decrypted=decrypt_text(encrypted)
print(decrypted)