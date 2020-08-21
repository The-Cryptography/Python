# This is a crypto-code for Caeser cipher
def encrypt(text,s):
	result = ""
        # traverse the plain text
	for i in text:
        # Encrypt uppercase characters in plain text      
        	if (i.isupper()):
         		result += chr((ord(i) + s-65) % 26 + 65)
        # Encrypt lowercase characters in plain text
        	else:
         		result += chr((ord(i) + s - 97) % 26 + 97)
	return result
#check the above function
text = "DEMO THE CRYPTOGRAPHY"	#plain text
s = 4	#key value
#displaying results
print("Plain Text : " + text)
print("Shift pattern : ",s)
print("Cipher: " + encrypt(text,s))	#displaying after calling the function

#The Cryptography
