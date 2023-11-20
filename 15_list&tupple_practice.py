''' 
# Q-1.. WAP to store seven fruits in a list entered by  a user.
f1=input("enter the fruit-1 : ")
f2=input("enter the fruit-2 : ")
f3=input("enter the fruit-3 : ")
f4=input("enter the fruit-4 : ")
f5=input("enter the fruit-5 : ")
f6=input("enter the fruit-6 : ")
f7=input("enter the fruit-7 : ")
fruitlists=[f1,f2,f3,f4,f5,f6,f7]
print("seven fruits in a list entered by  a user are : ")
print(fruitlists) '''

# Q2- WAP to accept marks of 6 students and display them in a sorted manner :

M1 = int(input("Enter the Marks of Student-1 : "))
M2 = int(input("Enter the Marks of Student-2 : "))
M3 = int(input("Enter the Marks of Student-3 : "))
M4 = int(input("Enter the Marks of Student-4 : "))
M5 = int(input("Enter the Marks of Student-5 : "))
M6 = int(input("Enter the Marks of Student-6 : "))
markslist=[M1,M2,M3,M4,M5,M6]
# print(markslist) # it will print as it is given by user 

markslist.sort() # it will sort the list 
print(markslist)
