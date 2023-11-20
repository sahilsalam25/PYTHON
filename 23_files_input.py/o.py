# Use Open function to Read the Content of a file :
# f = open('sample.txt','r') # 'r' means read mode :
# f = open('sample.txt','w') # 'w' means write mode :
# f = open('sample.txt','r+') # 'r +' means both read and write mode :
# f = open('sample.txt','a') # 'a' means append mode(add something) i.e you can change anything in that particluar file :
# f = open('sample.txt') # by default the mode is in 'r' i.e read mode
''' f = open('sample.txt','r')
data = f.read()
# data = f.read(5) # read only 5 character 
print(data)
f.close() '''
# Read Line function :
''' f=open('sample.txt') # read 1st line 'sample.txt'
data=f.readline()
print(data)
data=f.readline() # read 2nd line of 'sample.txt'
print(data)
f.close() '''
# Write function :
''' f=open('another.txt','w')
f.write("Hello !  This is Abdul Salam :\n")
f.write("Hello !  This is Amir Salam :\n")
f.write("Hello !  This is Sahil Salam :\n")
f.close() '''
# With function : no need to use "f.close()"" statement in with function
''' 
with open('another.txt','r') as f:
    a=f.read()
    print(a) '''  # read mode
''' with open('another.txt','w') as f:
     a=f.write("Me :")
     print(a) '''  # write mode
# print a multiplication table using file :
''' for i in range(2,11):
    # with open(f"Tables/Multiplication Table of {i}",'w') as f:
    with open(f"another {i}.txt",'w') as f:
        for j in range(1,11):
          f.write(f"{i}X{j}={i*j}\n") 
        break '''
# simple program to open a file in read or write mode :
sahil_file = open("sample_1.txt", "w") # 'w' sample.txt to create a new file sample_1.txt by using 'w' write function :
sahil_file.write("Hey Amir How Are You , Fine")
# print(sahil_file)
sahil_file.close()
# using for loop  to open a file in read or write mode :
''' sahil_file=open("sample.txt","r")
for data in sahil_file.readlines():
    print(data)
sahil_file.close()   '''
