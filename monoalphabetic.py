import pandas as pd
import string

def monoalpabetic(letters, num):
	letters = letters.upper()

	#frequency distribution from appearance in english
	frequency = {"E":12.7,"T":9.1,"A":8.2,"O":7.5,"I":7.0,"N":6.7,"S":6.3,"H":6.1,"R":6.0,
	"D":4.3,"L":4.0,"C":2.8,"U":2.8,"M":2.4,"W":2.4,"F":2.2,"G":2.0,"Y":2.0,"P":1.9,"B":1.5,
	"V":1.0,"K":0.8,"J":0.2,"X":0.2,"Q":0.1,"Z":0.1}
	
	#Calculate the distribution frequency in the ciphertext
	occur = {}
	for i in letters:
		if i not in occur:
			occur[i] = 1
		else:
			occur[i]+=1
	for i in occur.keys():
		occur[i] = round((occur[i] / len(letters)) * 100, 2)
	
	#Adds keys not in ciphertext for proper mapping of english frequency to cipher frequency
	for i in string.ascii_uppercase:
		if i not in occur:
			occur[i] = 0.00
	#Created Series requires only the keys for proper mapping
	occur = createSeries(occur,"occur").keys()
	frequency = createSeries(frequency,"frequency").keys()

	mapped = mapping(occur,frequency)
	
	#creates a set of equal length to the cipher text for easy swaping
	swappedletters = ["*"]*len(letters)

	#Swaps the ciphertext frequency for english frequency
	try:
		for i in frequency[0:num]:
			for j in range(len(letters)):
				if letters[j] == i:
					swappedletters[j] = mapped[i]
			print("".join(swappedletters))
	except:
		pass

#Creates a series using pandas
def createSeries(letters, name):
 	return pd.Series(letters,name = name).sort_values(ascending=False)

#returns a dictionary that maps ciphertext frequency to english frequency
def mapping(occur, frequency):
	return {a:b for a,b in zip(occur, frequency)}

cipher = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
num = int(input("Enter the number of possible texts to return: "))#Asks for user Input
print(cipher)#Print Cipher
monoalpabetic(cipher,num)
