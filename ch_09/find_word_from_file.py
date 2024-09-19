f = open("C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\poems.txt")
content = f.read()
if ("twinkle" in content):
    print("Twinkle is in poem")
else:
    print("Twinkle is not present")
f.close()
