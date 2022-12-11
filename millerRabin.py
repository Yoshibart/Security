import random

def Test(number):
	K, Q = find_kq(number)
	if(K < 1) or (Q % 2 == 0):
		return "K is either less than 1 or Q is not Odd"
	
	if number - 1 != pow(2, K) * Q:
		return str(number) + " - 1 is not equal pow(2, "+ str(K) +") * " + str(Q)

	A = a_random(number)
	print("K = " + str(K)+  ", Q = " + str(Q) +", A = "+str(A)+", Number "+ str(number)+", ", end=" ")
	

	if (pow(A,Q) % number) == 1:
		return "inconclusive"

	for i in range(K):
		if pow(A, pow(2,i) * Q) % number == (number - 1):
			return "inconclusive"

	return "composite"

def a_random(number):
	return int(1 + (random.random()  * number))

def find_kq(number):
	for k in range(10000):
		for q in range(1000000):
			if k > 0 and q % 2 == 1:
				if number - 1 == pow(2, k) * q:
					return (k, q)
	return (0,0)

print(Test(29))
print(Test(1499))
print(Test(7919))