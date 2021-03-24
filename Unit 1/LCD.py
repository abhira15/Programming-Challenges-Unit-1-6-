folder = input()
num = input()
paths = []
Lines = []
for i in num:
    k = ["E:\\LCD\\", folder, "line", "\\", i, ".txt"]
    separator = ''
    n = separator.join(k)
    paths.append(n)
for path in paths:
    file = open(path, 'r')
    Line = file.readlines()
    Lines.append(Line)
lope = len(Lines)
for j in range(0, lope):
    if len(Lines[0]) != len(Lines[j]):
        print("Line hight miss match")
        continue 
for i in range(0, len(Lines[0])):
    for j in range(0, lope):
        if Lines[j][i] == "|\n":
            print(Lines[j][i].strip("\n") + "   \t", end=' ')
           
        else:
            print(Lines[j][i].strip("\n") + "\t", end=' ')
    print(" ")

