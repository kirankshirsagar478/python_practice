#slicing
a = "kiran kshirsagar"
print(a[0:5]) #kiran
print(a[6:])  #kshirsagar
print(a[:5])  #kiran
print(a[0:15:3]) #kakia
print(a[0:-1]) #kiran kshirsaga

#string Functions

#length:
print (len(a)) #16
#endswith:
print(a.endswith("r")) #true
#count:
print(a.count("r")) #3
#capitalize: first character capatalize
print(a.capitalize()) #Kiran kshirsagar
#find:
print(a.find("r")) #2 first occurence
#replace:
print(a.replace("kiran","dipak")) #dipak kshirsagar