import random

def savePrivateKey(d):
	with open('private_key.txt', 'w') as file:
		file.write(f"{d}")

def savePublicKey(n, e):
	with open('public_key.txt', 'w') as file:
		file.write(f"{n},{e}")

def gcd(a, b):
	while b:
		a, b = b, a % b
	return a

def chooseE(phi):
	e = random.randint(2, phi - 1)
	while gcd(e, phi) != 1:
		e = random.randint(2, phi - 1)
	return e

def findD(phi, e):
	for d in range(2, phi):
		if (d * e) % phi == 1:
			return d

def generatePrime():
	primeArray = []
	for n in range(1001, 10000, 2):
		for i in range(2, int(n**0.5)+1):
			if n % i == 0:
				break
		else:
			primeArray.append(n)
	return random.choice(primeArray)

def main():
	p = generatePrime()
	q = generatePrime()
	n = p * q
	phi = (p - 1) * (q - 1)
	e = chooseE(phi)
	savePublicKey(n, e)
	print(f"<Public Key>\n n: {n}, e: {e}")
	d = findD(phi, e)
	savePrivateKey(d)
	print(f"<Private Key>\nd: {d}")

if __name__ == "__main__":
	main()
