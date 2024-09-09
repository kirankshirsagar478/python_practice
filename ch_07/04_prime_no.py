a=int(input("Enter a Number: "))
# i=2
# while(i<a):
#     if(a%i==0):
#         print("Not Prime No", a)
#         break
#     i +=1
# else:
#     print("Prime No", a)
    
for i in range (2,a):
    if(a%i==0):
        print("Not Prime No", a)
        break
else:
    print("Prime No: ",a)
