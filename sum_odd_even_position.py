def sum_odd_even_position(n):
    str_n=str(n)
    odd_sum,even_sum=0,0

    for i in range(len(str_n)):
        if (i+1)%2==0:
            even_sum+=int(str_n[i])
        else:
            odd_sum+=int(str_n[i])
    return odd_sum,even_sum

n=int(input("ENTER THE NUMBER : "))
odd_position, even_position=sum_odd_even_position(n)
print(f"THE SUM OF ODD POSITION IS : {odd_position} \nTHE SUM OF EVEN POSITION IS : {even_position}")