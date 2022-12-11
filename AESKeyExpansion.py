def keyExpansion(key):
	keys = []
	counter = 0

	while(counter < len(key)):
		keys.append([key[counter:counter+8]])
		counter+=8

	for i in range(4, 44):
		tempKey = keys[-1]
		if i % 4 == 0:
			tempKey = rotWord(tempKey)
			tempKey = subWord(tempKey)
			tempKey = rCon(tempKey)
		keys[i] = XOR(keys[i - 4], tempKey)
	return keys

key = "0f1571c947d9e8590cb7add6af7f6798"

for i in keyExpansion(key):
	print(i)
