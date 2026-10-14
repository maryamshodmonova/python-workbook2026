def digit_sum(n):
    last = n % 1000
    while last > 0:
        sum = 0 
        sum += n % 10
        n//=10
    first = n // 1000    
    while first > 0:
        fsum = 0
        fsum += n % 10
        n //= 10
    if sum == fsum:
       return True
    return False
print(digit_sum(123321))    
    
 