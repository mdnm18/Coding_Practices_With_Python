# HALF-PYRAMID : 
def half_pyramid(n):
    for lines in range(1,n+1):
        print("*"*lines)
n=int(input("ENTER THE TOTAL NUMBER OF LINES : "))
print(half_pyramid(n))