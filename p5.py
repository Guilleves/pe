#2520 is the smallest number that can be divided 
#by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isEvenlyDivisible(n):
	flag = False
	for i in range(1, 20):
		if n%i == 0:
			flag = True
		else:
			flag = False
			break
	return flag

def problem():
	result = False
	i = 1
	while result == False:
		result = isEvenlyDivisible(i)
		i += 1
	return (i-1)

#print (isEvenlyDivisible(232792561))
print (problem())