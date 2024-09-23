words = ["Donkey", "bad", "poor"]
with open("C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\file.txt", "r") as f:
   content = f.read()
for word in words:
    newContent = content.replace(word, "#"*len(word)) # number of words, number of #s
with open("C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\file.txt", "w") as f:
   f.write(newContent)