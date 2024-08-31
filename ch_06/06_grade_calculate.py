marks=int (input("Enter marks of student: "))

if (marks>= 90 and marks<=100):
    print("Exclent\nMarks :",marks)
elif (marks>= 80 and marks<90):
    print("A Grade\nMarks :",marks)
elif (marks>=70 and marks<80):
    print("B Grade\nMarks :",marks)
elif (marks>=60 and marks<70):
    print("C Grade\nMarks :", marks)
elif (marks>=50 and marks<60):
    print("D Grade\nMarks :", marks)
else:
    print("Fail\nMarks :", marks)