#Encryption 
def encrypt(text,key): 
	result = "" 

	for i in range(len(text)): 
		char = text[i] 

		# Encrypt uppercase characters 
		if (char.isupper()): 
			result += chr(ord(char) + key) 

		# Encrypt lowercase characters 
		else: 
			result += chr(ord(char) + key) 

	return result 

#Decryption 
def decrypt(Encrypt,key): 
	result = "" 

	for i in range(len(Encrypt)): 
		char = Encrypt[i] 

		# Encrypt uppercase characters 
		if (char.isupper()): 
			result += chr(ord(char) - key) 

		# Encrypt lowercase characters 
		else: 
			result += chr(ord(char) - key) 

	return result 

text =input("\nEnter your MSg:")
key = int(input("\nEnter Encryption Key:"))
Encrypt=encrypt(text,key) 
Decrypt=decrypt(Encrypt,key)
print("\n Your Msg with Encryption:"+Encrypt)
print("\n Your Msg with Decryption:"+Decrypt)


