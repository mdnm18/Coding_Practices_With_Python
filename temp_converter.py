# Write a python program using function to convert Celsius to Fahrenheit. 
def celsius_fahrenheit(c):
    f=(c*9)/5+32
    return f
cel=float(input("ENTER THE TEMPERATURE IN CELSIUS :"))
print("THE TEMPERATURE IN FAHRENHEIT IS : ",celsius_fahrenheit(cel))
