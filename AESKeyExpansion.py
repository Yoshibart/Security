def keyExpansion(key):
	keys = []
	counter = 0

	while(counter < len(key)):
		keys.append([key[counter:counter+8]])
		counter+=8

	for i in range(4, 44):
		tempKey = keys[-1][0]
		if i % 4 == 0:
			tempKey = rotWord(tempKey)
			tempKey = subWord(tempKey)
			tempKey = rCon(tempKey)
		keys[i] = XOR(keys[i - 4], tempKey)
	return keys

key = "0f1571c947d9e8590cb7add6af7f6798"

def rotWord(tempKey):
	return tempKey[2:len(tempKey)] + tempKey[0:2]

def sBox():
	Box =  []
	sBox = {}
	for i in open("subWord.txt"):
		Box.append(i.split(" "))

	for i in range(0, 16):
		for j in range(0, 16):
			sBox[str(i) + "," + str(j)] = Box[i][j]
	return sBox
	
def subWord(tempKey):
	subTemp = ""
	Box = sBox()
	letters = {"a":"10", "b":"11", "c":"12", "d":"13", "e":"14", "f":"15",
				"0":"0", "1":"1", "2":"2", "3":"3", "4":"4", "5":"5", "6":"6",
				"7":"7", "8":"8", "9":"9"}
	for i in range(0,len(tempKey),2):
		f = tempKey[i:i+2]
		key = letters[f[0:1]]+','+letters[f[1:2]]
		subTemp += Box[key]

	return subTemp

for i in keyExpansion(key):
	print(i)
