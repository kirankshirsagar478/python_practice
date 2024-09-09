n= int(input("Enter Number: "))
fact=1
for i in range(1,n+1): #range should (1, n+1) not (1,n) ; range always goes till n-1
    fact= fact*i
print(fact)