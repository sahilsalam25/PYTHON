# Sets is a collection of non-repetive type :
''' a={1,2,3,4,5,1}
print(type(a))
print(a)
# Empty set- an empty set can be created using the below syntax :
b=set()
print(type(b))
print(b)
# Methods of Sets :
#Method-1,- .add() adding values to an empty set :
b.add(5)
b.add(10)
b.add((2,4,5,65,40))
# b.add([12,5,6]) # cannot add list or dictionary to sets 
print(b)

# Method-2,.len()
print(len(b)) # print the length of this set:
print(len(a)) 
# method-3, .remove
b.remove(10) # remove 10 from set b
# b.remove(15) # throws an error because 15 is not present in set b:

print(b)
# method 3, .pop()-
print(b.pop()) # it removes the random elements
print(b)
# method 4, .clear()
print(b.clear()) # it clears or empty the whole sets
print(b) '''
 ### PRACTICE SETS QUESTION
 # Q-1. WAP to create a dictionary of hindi words with value as their english translation provide by a user with an option to took it up :
mydictionary={
    "hawa":"air",
    "paani":"water",
    "aasman":"sky",
    "aag":"fire"
}
# print(mydictionary)
print("The Given Options are :\n",mydictionary.keys())
a=input("Enter the Hindi Words : ")
# print("The meaning of your Word is : ",mydictionary[a])
# if the output word is not present in the dictionary then it will throw an error so for this we will .get() to avoid error
print('The meaning of your Word is :',mydictionary.get(a))






