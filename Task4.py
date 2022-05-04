

#Task4: breaking the encryption by iterating through each possible rotation
def caesarCipher(integer, string):

	ccipher = ''

	#doing a shift for each letter:
	for char in string:

		if char == ' ': 
			ccipher = ccipher + char
		elif char.isupper():
			ccipher = ccipher + chr( ( ( ord(char) + integer - 65 ) % 26 ) + 65 )
		elif char.islower():
			ccipher = ccipher + chr( ( ( ord(char) + integer - 97) % 26 ) + 97 )

	return ccipher

def menu4():

	print("         Welcome to the encryption-breaker          ")
	rotation = int(input("Choose the rotation factor for symmetric encryption (indicate integer number): "))
	text = input("Please enter your phrase: ")

	encrypted = caesarCipher(rotation, text.lower())
	print("The encrypted text: ", encrypted)

	return encrypted

def encryptionBreaker(encrypted):

	#words = ["apple", "sun", "world", "people", "life", "work", "place",]
	chars = "abcdefghijklmnopqrstuvwxyz"

	print("Iterating through each possible rotation:")
	#going through each rotation possibilities:
	for n in range(26):

		rots = chars[n:] + chars[:n]
		decrypted = ''.join( rots[chars.index(c)] for c in encrypted )
		print("The decrypted text: ", decrypted)

encrypted = menu4()
encryptionBreaker(encrypted)
