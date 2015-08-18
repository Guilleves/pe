#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def isMultiple(number):
    if number%3 == 0 or number%5 == 0:
        return True
    else:
        return False

def problem():
    total = 0
    for i in range (0, 1000):
        if isMultiple(i):
            total = total + i
            
    return total
    
print problem()