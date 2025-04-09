def hollow_sq(n):
    for lines in range(1,n+1):
        for items in range(1,n+1):
            if lines==1 or items==1 or lines==n or items==n:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
n=int(input("ENTER THE TOTAL NUMBER OF LINES : "))
print(hollow_sq(n))