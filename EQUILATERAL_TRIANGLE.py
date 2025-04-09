# EQUILATERAL TRIANGLE :
def equilateral_triangel(n):
    for lines in range(n):
        for space in range(n-lines-1):
            print(" ", end=" ")
        for stars in range(2*lines+1):
            print("*", end=" ")
        print()
n=int(input("ENTER THE TOTAL NUMBER OF LINES : "))
print(equilateral_triangel(n))
