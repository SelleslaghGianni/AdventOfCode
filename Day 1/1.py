array = []

f = open("input.txt", "r")

for row in f:
    array.append(row)

    
for row in array:
    for i in array:
        if (int(row) + int(i)) == 2020:
            print(row)
            print(i)
            exit(0)

