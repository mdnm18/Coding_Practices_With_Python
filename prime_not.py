# Write a program to find whether a given number is prime or not. 
def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

n=int(input("ENTER A DIGIT TO CHECK WHETHER IT IS PRIME OR NOT : "))
if isprime(n):
    print(n,"IS A PRIME NUMBER.")
else:
    print(n,"IS NOT A PRIME NUMBER.")