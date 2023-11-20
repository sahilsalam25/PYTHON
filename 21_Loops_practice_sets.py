# Q-1 WAP to print multiplication table using while loops :
''' 
# Method-1 
table=int(input("Enter the number to print Table : "))
i=1
tab=1
while i<=11:
    print("The table of given number is : " + str(tab))
    tab=int(table*i)
    i=i+1 '''
# Method 2
''' table=int(input("Enter the number to print Table : ")) 
i=1
while i<=10:
    print(table*i)
    i=i+1  '''
### Q-1 WAP to print multiplication table using for loops :
''' num=int(input("Enter the Number : "))
for i in range(1,11):
# print(str(num)+ "X" + str(i)+ "=" + str(num*i)) # Method -1
# Using F-String
    print(f"{num}X{i}={num*i}")''' # Method -2
### Q-2 WAP to greet all the persons name stored in a list L1 and which starts with 'S' :
''' L1=["sahil","salam","amir","salman",""]
for name in L1:
    if name.startswith("s"):
            print("Hello :" + name) '''
### Q-2 WAP to find given number is prime or not
''' num=int(input("Enter the Number : "))
prime=True
for i in range(2,num):
    if (num%i==0):
        prime = False
        break
if prime:
        print("Given Number is Prime")
       
else:
        print("Given Number is Not Prime")  '''
          
### Q-3 WAP to print calculate the factorial of a given number using for Loop :
# factorial -  n!= 1*2*3*4...., 4!=4*3*3*1
num=int(input("Enter the Number : "))
factorial=1
for i in range(1,num+1):
   
    print(f"The factorial of the {num} is {factorial}")
    factorial=factorial*i   
        
            
            
    
    
    