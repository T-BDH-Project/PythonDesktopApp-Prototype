import string
import random

def main():
	#ici le code a éxécuter quand on a tout validé
	size = 3
	chars = string.digits
	id1 = ''.join(random.choice(chars) for _ in range(size))
	id2 = ''.join(random.choice(chars) for _ in range(size))
	id3 = ''.join(random.choice(chars) for _ in range(size))
	id4 = ''.join(random.choice(chars) for _ in range(size))
	idavecpoint = id1 + "." + id2 + "." + id3 + "." + id4
	idsanspoint = id1 + id2 + id3 + id4
	print(idavecpoint)
	print(idsanspoint)
