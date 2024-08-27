letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
a = input("Enter Name: ")
b = input("Enter Date: ")
print(letter.replace("<|Name|>", a).replace("<|Date|>", b))
#In python string is immutable so following method will not work
# letter.replace("<|Name|>", a)
# letter.replace("<|Date|>", b)
# print (letter)