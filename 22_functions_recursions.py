# WAP to print an average of marks using function :
'''def percent(marks):
    p=((marks[0]+ marks[1]+marks[2]+marks[3])/400)*100
    return p
marks1=[45,75,80,71]
percentage1=percent(marks1)

marks2=[75,95,88,7]
percentage2=percent(marks2)
print(percentage1 , percentage2) '''

# Ex-2 , function call & function defenition


def greet(name):
    print("You Have A Great Day : " + name)  # function defenition


greet("SAHIL")  # it is function call

### Recursion :
# n!=1*2*3*4.....*n
# n!= [1*2*3*4....(n-1)]*n
# n!=n*(n-1)!


''' def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product*(i+1)
        return product


def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)


# f=factorial_iter(5)
f = factorial_recursive(4)
print(f) '''
# Q-1 .WAP to find the maximum of the given number :
''' def maximum(num1, num2, num3):


    if (num1 > num2):
        return num1
    else:
        return num3
    else:
    if (num2 > num3):
            return num2
    else:
            return num3
    m=maximum(20,5,50)
    print("The Value Of Maximum is : " + str(m)) '''
    
### Q-2 WAP to convert Celcius to farhenheit : 
def farh(cel):
    return (cel*(9/5))+32
c=37
farh=farh(c)
print("farhenheit Temperature is : " + str(farh))  

### Q3 WAP to remove space after new line in print finction:
# print("SAHIL")
# print("SALAM") # it will print in new line i.e 4 new line for this we use end function to remove new line in print function :
# print("AMIR")
# print("SALAM")
'''
print("SAHIL",end=" ")
print("SALAM",end=" ")
print("AMIR",end=" ")
print("SALAM",end=" ") '''
### Q4- WAP to print * 
# n=4
# for i in range(n):
#     print("*" * (n-i)) # Prints * (n-i) Times :
     
    
