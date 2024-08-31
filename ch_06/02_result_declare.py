s1=int(input("Enter subject 1 marks:"))
s2=int(input("Enter subject 2 marks:"))
s3=int(input("Enter subject 3 marks:"))
total=(s1+s2+s3)/3
if(s1>30 and s2>33 and s3>30 and total>40):
    print("passed ! Percentages: ",total)
else:
    print("fail ! Percentages: ", total)