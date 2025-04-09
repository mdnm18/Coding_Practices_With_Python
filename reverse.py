n=int(input("ENTER THE NUMBER : "))
rev=0
lastdigit=0
while n!=0:
    lastdigit=n%10
    rev=(rev*10)+lastdigit
    n//=10
print(f"THE REVERSE OF THE GIVEN NUMBER IS : {rev}")