n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))
n3=int(input("enter number 3: "))
n4=int(input("enter number 4: "))
if(n1>n2 and n1>n3 and n1>n4):
    print("Greater Number is:",n1)
elif(n2>n1 and n2>n3 and n2>n4):
    print("Greater Number is:", n2)
elif(n3>n1 and n3>n2 and n3>n4):
    print("Greater Number is:",n3)
else:
    print("Greater Number is:",n4)