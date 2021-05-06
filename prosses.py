import string
import random
import sqlite3
import os


def main(nbre_core, nbre_ram, nbre_stock, bp, final_per, per):
	#ici le code a éxécuter quand on a tout validé
	size = 3
	chars = string.digits
	id1 = ''.join(random.choice(chars) for _ in range(size))
	id2 = ''.join(random.choice(chars) for _ in range(size))
	id3 = ''.join(random.choice(chars) for _ in range(size))
	id4 = ''.join(random.choice(chars) for _ in range(size))
	idavecpoint = id1 + "." + id2 + "." + id3 + "." + id4
	idsanspoint = id1 + id2 + id3 + id4

	create_new_table(idsanspoint, nbre_core, nbre_ram, nbre_stock, bp, final_per, per)



def create_new_table(idsanspoint, nbre_core, nbre_ram, nbre_stock, bp, final_per, per):
	if not os.path.exists(f'{idsanspoint}.db'):
		path = './'
		open(f'{idsanspoint}.db', 'w').close()


		

	con = sqlite3.connect(f'{idsanspoint}.db')
	cur = con.cursor()
	print("Opened database successfully")



	cur.execute('''CREATE TABLE USER
		(ID INT PRIMARY KEY NOT NULL,
		CORE_NUMBER INT NOT NULL,
		RAM_NUMBER INT NOT NULL,
		STOCK_NUMBER INT NOT NULL,
		BP REAL NOT NULL,
		PRICE_PROP REAL NOT NULL,
		PRICE_IND REAL NOT NULL);''')
	cur.execute(f"INSERT INTO USER VALUES ({idsanspoint}, {nbre_core}, {nbre_ram}, {nbre_stock}, {bp}, {final_per}, {per})")

	con.commit()
	print("Table created successfully")