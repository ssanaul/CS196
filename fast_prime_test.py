#Objective: to prime-test the number 961748941
#with a runtime of less than a second

def detPrime(num):
	if num%2 == 0:
		return False
	count = 3
	num_rng = num**.5
	while count < num_rng:
		#num_rng = int(float(num)/float(count))
		if num%count == 0:
			return False
		count+=2
	return True
#print detPrime(151)
print detPrime(67867979)
print detPrime(100000001)
print detPrime(961748941)