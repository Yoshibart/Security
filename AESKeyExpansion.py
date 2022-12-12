def keyExpansion(key):
	keys = []
	counter = 0

	Rcon = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36]
	con = 0

	while(counter < len(key)):
		keys.append([key[counter:counter+8]])
		counter+=8

	for i in range(4, 44):
		tempKey = keys[-1][0]
		if i % 4 == 0:
			tempKey = rotWord(tempKey)
			tempKey = subWord(tempKey)
			tempKey = rCon(tempKey, Rcon[con])
			con += 1
		keys[i] = XOR(keys[i - 4], tempKey)
	return keys

def XOR(one, four):
	return [hex(int(one, 16) ^ int(four, 16))[2:]]

def rotWord(tempKey):
	return tempKey[2:len(tempKey)] + tempKey[0:2]

def rCon(tempKey, con):
	return hex(int(tempKey[0:2],16) ^ con)[2:] + tempKey[2:]

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
	for i in range(0,len(tempKey),2):
		f = tempKey[i:i+2]
		key = str(int(f[0:1], 16))+','+str(int(f[1:2], 16))
		subTemp += Box[key]

	return subTemp
	
key = "0f1571c947d9e8590cb7add6af7f6798"

for i in keyExpansion(key):
	print(i)
