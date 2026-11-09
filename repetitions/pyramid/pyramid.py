n = int (input())
for i in range (1, n + 1):
    for j in range(n - i):
        print (" ", end = " ") # 4 * and then space and less less ad less
    for k in range (2 * i - 1):
        print ("*", end = " ")
    print () 
    # tag ba tag 