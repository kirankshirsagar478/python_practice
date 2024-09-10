def great(n1,n2,n3):
    if(n1>n2 and n1>n3):
        return n1
    elif(n2>n1 and n2>n3):
        return n2
    elif(n3>n1 and n3>n2):
        return n3
    else:
        return "Same Numbers"

n1 = int(input("Enter Number 1:"))
n2 = int(input("Enter Number 2:"))
n3 = int(input("Enter Number 3:"))
print("Greater No: ", great(n1,n2,n3))