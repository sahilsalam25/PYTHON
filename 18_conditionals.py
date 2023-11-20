# in python only one conditional statement will execute : at a time only if,elif... will be execute
'''
a=int(input("Enter any Number : "))
# a=900
if(a>30):
    print("The value is greater than  number 30 ")
elif(a>15):
    print("the value is greater than 15 ")
elif(a<10):
    print("The value is less than 10 ")
else:
    print("in-valid")   '''
# Q2 Multiple if
# a=10
''' a=int(input("Enter any Number : "))
if(a<3):
    print("the value of a is less than 3 ")
if(a>14):
    print("the value of a is greater than 14")
if(a>20):
    print("the value of a is greater than 20")
else: # else is optional in conditional statements :
    print("Done :")   '''
# Relational operators ==,>=,<= it is used to evaluate the variable in conditional statements
# Q-1 WAP to find greatest of four numbers entered by the user :
'''
num1 = int(input("enter the number 1 : "))
num2 = int(input("enter the number 2 : "))
num3 = int(input("enter the number3 : "))
num4 = int(input("enter the number 4 :"))
    
if (num1 > num4):
        f1 = num1

else:
        f1 = num4
if (num2 > num3):
        f2 = num2
else:
        f2 = num3
if (f1 > f2):
        print(str(f1) + " is greatest")
else:
     
        print(str(f2) + " is greatest") '''
# Q 2 WAP to calculate the grade of a student from his marks :
marks = int(input('Enter the marks :\n'))
if (marks >= 90):
    grade = "Excellent"
elif (marks >= 80):
    grade = "A"
elif (marks >= 70):
    grade = "B"
elif (marks >= 60):
    grade = "C"
elif (marks >= 50):
    grade = "D"
else:
    grade = "Fail"
print("Your grade is : " + grade)

