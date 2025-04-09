def Inverted_Star_Pattern(n):
    for lines in range(1,n+1):
        print("*"*n)
        n-=1      
    # print()

n=int(input("ENTER THE TOTAL NUMBER OF LINES : "))
print(Inverted_Star_Pattern(n))