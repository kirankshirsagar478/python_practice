l1=[1,2,5,75,12,34,65,2]
#sort
l1.sort()
print(l1)

#reverse
l1.reverse()
print(l1)

#append
l1.append(8)
print(l1)

#insert
l1.insert(3,8)
print(l1)
#added 8 at index 3

print(l1.pop(2)) #return pop element i.e 34
print(l1) #print list without 34 element

#remove
l1.remove(2)
print(l1) #it will delete 2 from list. if there are two element then it delets only first element

#tuple in Python
a = () # empty tuple
a = (1,) # tuple with only one element needs a comma
a = (1,7,2,1,3,1) # tuple with more than one element
#count
print(a.count(1)) # 3  returned count of 1s in tuple
#index
print(a.index(1)) # 0  retruned index of 1 (first occurence)
