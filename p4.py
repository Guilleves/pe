def isPalindrome(n):
	n = str(n)
	if len(n) == 5:
		if n[0] == n[4] and n[1] == n[3]:
			return True
		else:
			return False
	elif len(n) == 6:
		if n[0] == n[5] and n[1] == n[4] and n[2] == n[3]:
			return True
		else:
			return False
	else:
		return False

def products():
	for i in range(100, 999):
		for j in range(100, 999):
			prod = i*j
			yield prod

def problem():
	maxPalindrome = 0
	for prod in products():
		if (isPalindrome(prod)):
			if prod > maxPalindrome:
				maxPalindrome = prod
	print (maxPalindrome)

problem()