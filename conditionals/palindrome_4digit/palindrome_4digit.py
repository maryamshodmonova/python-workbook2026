n = int(input())
num1 = n // 1000
num2 = (n // 100) % 10
num3 = (n // 10) % 10
num4 = n % 10
if num1 == num4 and num2 == num3:
    print ("polindrome")
else:
    print ("not polindrome")
    
