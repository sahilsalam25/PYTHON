# 1- List Slicing
friends=["SAHIL","ABDUL","AMIR",45,"ABCD"]
print(friends) # print the output without slicing
print(friends[0:4]) # print the output with slicing
print(friends[1:5]) # print the output with slicing

# 2-- sort, for sorting the list
l1=[1,7,4,8,10,15,2]
# l1_sorted=l1.sort()
# print(l1_sorted)
print(l1) # before sorting 
l1.sort()
print(l1) # after sorting no's in serial manner

# 3-- reverse , revere the list
l1.reverse()
print(l1) # it reverse the list

# 4-- Append, add's at  the  end of the list
l1.append(65) # add 65 in the list at the end
print(l1)

# 5-- insert, it is used to insert in the list
l1.insert(1,225) # inserts 225 at index 1
print(l1)
# 6--pop, it is used to remove at given index
l1.pop(3) # it removes the no's list l1= 8 at index 3 ..
print(l1)

# 7--remove ,it is used to remove the no in the given list
l1.remove(15) # it removes 15 from the list l1
print(l1)
