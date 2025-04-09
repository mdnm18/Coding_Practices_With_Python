# Write a program to find the sum of first n natural numbers using while loop. 
# Write a recursive function to calculate the sum of first n natural numbers. 
'''
def sum_n_digits(n):
    sum=0
    for i in range(1,n+1):
        sum+=i;
    return sum
'''
def sum_n_digits(n):
    if n==1:
        return 1
    else:
        return n+sum_n_digits(n-1)

n=int(input("ENTER A DIGIT : "))
if n>0:
    print("THE SUM OF FIRST",n,"NATURAL NUMBER IS :",sum_n_digits(n))
else:
    print("ENTER POSITIVE DIGIT!")