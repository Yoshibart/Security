import pandas as pd
import numpy as np

def monoalpabetic(letters):
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
	mapped = mapping(frequency,occur)
	return 

def createSeries(letters, name):
 	return pd.Series(letters,name = name).sort_values(ascending=False)

def mapping(frequency, occur):
	return {a:b for a,b in zip(frequency, occur)}

cipher = "UZQSOVUOHXMOPVGPOZPEVSGZWSZOPFPESXUDBMETSXAIZVUEPHZHMDZSHZOWSFPAPPDTSVPQUZWYMXUZUHSXEPYEPOPDZSZUFPOMBZWPFUPZHMDJUDTMOHMQ"
print(monoalpabetic(cipher))