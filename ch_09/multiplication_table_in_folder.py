def generateTable(n):
    table = ""
    for i in range(1,11):
        table += f"{n} X {i} = {n*i}\n"
    with open(f"C:\\Users\\kiran\\OneDrive\\Desktop\\python new\\ch_09\\table\\table_{n}.txt", "w") as f:
        f.write(table)
    
for i in range (2, 21):
    generateTable(i)