# Write a program to calculate the factorial of a given number using for loop. 
'''
def factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
'''
def factorial(n):
    # if n==0 or n==1:
    if n in (0,1):
        return 1
    else:
        return n*factorial(n-1)

n=int(input("ENTER A DIGIT : "))
print("THE FACTORIAL OF",n,"IS : ",factorial(n))