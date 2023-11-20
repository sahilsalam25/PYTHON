# prg to print fruits from a list
fruits=['apple','guava','mango','grape','papaya','kiwi','banana']
## method 1
''' i=0
for items in fruits:
    print(fruits[i])
    i=i+1 '''
## method 2
# for item in fruits:
#     print(item)
    
### Range funtion in for loop :
# for i in range(1,10):
#     print(i)   
# else:
#     print("The Else will execute  when the for condition is false :")   
 
### Break Statement : it is used terminate the loop codnition at particular given break conmdtions
# for i in range(1,15):
#     print(i) 
#     if i==10: 
#        break     # it will break the loop at 10, if==10 
### Continue statement , it is used to ignore that particular conditions :
''' for i in range(20):
    if i==5:
        continue # it skip/ignore [5] the particular value condition , if i==5,
    print(i) '''
## Ex- WAP to print Power of a Number Using for loop and "Function"...:
def raise_to_power(base_num,power_num):
    result=1
    for index in range(power_num):
        result = result * base_num
    return result
print(f"The Power of given number is : {raise_to_power(5,2)}")    
    
   
    