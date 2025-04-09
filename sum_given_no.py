n=int(input("ENTER THE NUMBER : "))
sum=0
while n!=0:
    sum+=n%10
    n//=10
print(f"THE SUM OF THE GIVEN NUMBER IS : {sum}")