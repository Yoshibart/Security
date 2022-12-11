def keyExpansion(key):
	keys = []
	tempKey = []
	counter = 0

	while(counter < len(key)):
		keys.append([key[counter:counter+8]])
		counter+=8
	return keys

key = "0f1571c947d9e8590cb7add6af7f6798"

for i in keyExpansion(key):
	print(i)
