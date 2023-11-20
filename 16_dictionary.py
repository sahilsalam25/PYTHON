# Dictionary- it is a collections of key-values pair
# Syntax:
#     a={"key":"value"}
mydictonary={
    "fast":"in a quick manner",
    "sahil":"shore",
    "marks":[12,25,50,15],
    10:35
}
print(mydictonary) # to print a whole dictionary
print(mydictonary["sahil"]) # to print a particular items
mydictonary['marks']=[20,65,80,10] # we can change or update the dictionary elements
print(mydictonary['marks'])
print(mydictonary)

# Methods of Dictionaries :
# Method No-1-- keys() -  it is used to print the keys of the dictionary :
print(mydictonary.keys())
# typecasting into list
print(list(mydictonary.keys())) # typecasting into list 
# Method No-2-- values() -  it is used to print the values of the dictionary :
print(mydictonary.values())
# Method No-3-- items() -  it is used to print the {key,value} for all the contents of the dictionary :
print(mydictonary.items())
# Method No-4-- update() -  it is used to update the elements or contents of the dictionary :
print(mydictonary)
updatedictionary={
    "amir":"brother",
    "sanawwar":"childhood",
    "sahil":"samundar ka kinara"
}
mydictonary.update(updatedictionary) # updates the dictionary by adding key-values pairs from updatedictionary :
print(mydictonary) # it will the value of "sahil" from 'shore' to 'samundar ya darya ka kinara' :
 
