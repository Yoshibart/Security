import pandas as pd
import numpy as np

def monoalpabetic(letters, num):
	letters = letters.upper()
	frequency = {"E":12.7,"T":9.1,"A":8.2,"O":7.5,"I":7.0,"N":6.7,"S":6.3,"H":6.1,"R":6.0,
	"D":4.3,"L":4.0,"C":2.8,"U":2.8,"M":2.4,"W":2.4,"F":2.2,"G":2.0,"Y":2.0,"P":1.9,"B":1.5,
	"V":1.0,"K":0.8,"J":0.2,"X":0.2,"Q":0.1,"Z":0.1}
	occur = {}
	for i in letters:
		if i not in occur:
			occur[i] = 1
		else:
			occur[i]+=1
	for i in occur.keys():
		occur[i] = round((occur[i] / len(letters)) * 100, 2)

	occur = createSeries(occur,"occur").keys()
	frequency = createSeries(frequency,"frequency").keys()
	mapped = mapping(occur,frequency)
	
	swappedletters = ["*"]*len(letters)

	try:
		for i in frequency[0:num]:
			for j in range(len(letters)):
				if letters[j] == i:
					swappedletters[j] = mapped[i]
			print("".join(swappedletters))
	except:
		pass

def createSeries(letters, name):
 	return pd.Series(letters,name = name).sort_values(ascending=False)

def mapping(occur, frequency):
	return {a:b for a,b in zip(occur, frequency)}

cipher = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
num = int(input("Enter the number of possible texts to return: "))
print(cipher)
monoalpabetic(cipher,num)