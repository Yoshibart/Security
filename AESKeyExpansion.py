def keyExpansion(key):
	if len(key) < 16:
		return "Not a 16 length() key"
		
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
		keys.append(XOR(keys[i - 4][0], tempKey))
	return keys

#Bitwise Excusive OR
def XOR(one, four):
	fi = hex(int(one, 16) ^ int(four, 16))[2:]
	if len(fi) % 2 == 1:
		fi = "0" + fi
	return [fi]

#byte Rotation
def rotWord(tempKey):
	return tempKey[2:len(tempKey)] + tempKey[0:2]

def rCon(tempKey, con):
	return hex(int(tempKey[0:2],16) ^ con)[2:] + tempKey[2:]

#Creates SBox
def sBox():
	Box =  []
	sBox = {}
	for i in open("subWord.txt"):
		Box.append(i.split(" "))

	for i in range(0, 16):
		for j in range(0, 16):
			sBox[str(i) + "," + str(j)] = Box[i][j]
	return sBox

#Byte Subsititution
def subWord(tempKey):
	subTemp = ""
	Box = sBox()
	for i in range(0,len(tempKey),2):
		f = tempKey[i:i+2]
		key = str(int(f[0:1], 16))+','+str(int(f[1:2], 16))
		subTemp += Box[key]

	return subTemp
	
key = "0f1571c947d9e8590cb7add6af7f6798"

#Prints Keys
for i in keyExpansion(key):
	print(i, end="\n")
