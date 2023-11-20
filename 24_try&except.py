# Try and Except error is used to ignore the Error caused by the program error, to neglect that error we are using try & except error :
'''
number=int(input("Enter the Number : ))
print(number)
# output - Enter the Number : sahil
it will through an error because sahil is a string not a int Number :
File "c:\Users\Hp\Desktop\S1_PYTHON\24_try&except.py", line 9, in <module>
    number=int(input("Enter the Number : "))
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
ValueError: invalid literal for int() with base 10: 'sahil'
PS C:\Users\Hp\Desktop\S1_PYTHON>
'''
try:
   # value=10/0 # 0 is not divisible by any number
    number=int(input("Enter the Number : "))
    print(number)
except:
    print("Invalid Input : ")    