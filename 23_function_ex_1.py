### WAP to print temp celcius to farhenheit by taking a random input from user :
temp=int(input("Enter the value of temp : "))
def farh(cel):
    temp_formula=(cel*(9/5))+32
    return temp_formula
# c=37
result=farh(temp)
# print("farhenheit Temperature is : " + str(farh)) 
print(f"farhenheit Temperature is :  {result}") 