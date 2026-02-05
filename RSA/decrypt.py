def convertText(bytes_message):
	message = ""
	for _ in range(len(str(bytes_message))):
		message = chr(bytes_message & 255) + message
		bytes_message >>= 8
	return message

def decrypt(cipher, n, d):
	message = pow(cipher, d, n)
	return message

def getCipherMessage():
	with open('cipher_text.txt', 'r') as file:
		cipher = int(file.read())
	return cipher

def getPublicKey():
	with open('public_key.txt', 'r') as file:
		n, e = [int(x) for x in file.read().split(',')]
	return n, e

def getPrivateKey():
	with open('private_key.txt', 'r') as file:
		d = int(file.read())
	return d

def main():
	n, e = getPublicKey()
	d = getPrivateKey()
	cipher = getCipherMessage()
	bytes_message = decrypt(cipher, n, d)
	message = convertText(bytes_message)
	print(f"{cipher}\n↓↓↓\n{message}")

if __name__ == "__main__":
	main()
