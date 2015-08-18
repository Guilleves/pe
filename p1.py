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