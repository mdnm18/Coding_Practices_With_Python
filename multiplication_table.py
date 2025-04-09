# Write a program to print multiplication table of a given number using for loop.
print("LET'S CREATE A MULTIPLICATION TABLE :-")
n=int(input("WHICH NUMBER TABLE YOU WANT TO SEE : "))
print("THE MULTIPLICATION TABLE OF",n,"IS : ")

# for i in range(0,10):
    # print(n,"x",i+1,"=",n*(i+1))

i=1
while(i<=10):
    print(n,"x",i,"=",n*i)
    i+=1