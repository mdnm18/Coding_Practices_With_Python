# Write a program using functions to find greatest of three numbers. 
def largest_num(a,b,c):
    if a>b and a>c:
        print(a,"IS THE LARGEST NUMBER.")
    elif b>a and b>c:
        print(b,"IS THE LARGEST NUMBER.")
    else:
        print(c,"IS THE LARGEST NUMBER.")

a=int(input("ENTER THE FIRST NUMBER : "))
b=int(input("ENTER THE SECOND NUMBER : "))
c=int(input("ENTER THE THIRD NUMBER : "))
largest_num(a,b,c)