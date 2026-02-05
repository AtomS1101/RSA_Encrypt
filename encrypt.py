def sendMessage(cipher):
	with open("cipher_text.txt", "w") as file:
		file.write(str(cipher))

def encrypt(bytes_message, n, e):
	return pow(bytes_message, e, n) # (bytes_message ** e) % n

def getPublicKey():
	with open('public_key.txt', 'r') as file:
		n, e = [int(x) for x in file.read().split(',')]
	return n, e

def convertBytes(message):
	converted = 0
	for letter in message:
		converted = converted << 8 | ord(letter)
	return converted

def main():
	message = "ABC" # only three letters
	bytes_message = convertBytes(message)
	n, e = getPublicKey()
	cipher = encrypt(bytes_message, n, e)
	print(f"{message}\n↓↓↓\n{cipher}")
	sendMessage(cipher)

if __name__ == "__main__":
	main()
