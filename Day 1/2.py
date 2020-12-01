array = []

f = open("input.txt", "r")

for row in f:
    array.append(row)

    
for row in array:
    for i in array:
        for j in array:
            if (int(row) + int(i) + int(j)) == 2020:
                print(row)
                print(i)
                print(j)
                exit(0)
