s={3,6,8,1,4}
print(s)
print(len(s)) #5

#remove from set
s.remove(3)
print(s) #{1, 4, 6, 8}

#pop: remove arbitary(starting) element
s.pop()
print (s) #{4, 6, 8}

#union intersectio:
s1 = {1, 45, 6, 78}  
s2 = {7, 8, 1, 78}

print(s1.union(s2)) #{1, 6, 7, 8, 45, 78}
print(s1.intersection(s2)) #{1, 78}