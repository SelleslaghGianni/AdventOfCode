import numpy as np
import re

array = []
count = 0
pwdcount = 0
part2counter = 0

filename = "input.txt"
f = open(filename, "r")

for row in f:
    array.append(row)

arr = np.array(array)

for x in arr:
    max = 0
    #Checking if there are 1 or 2 digits. If true 1 digit, false 2 digits.
    if "-" in x[0:2]:
        min = int(x[0])
        max = int(x[2:4])
        count = x.count(x[5])
        #Checking if there are 1 or 2 digits in the max.
        if " " in x[2:4]:
            max = int(x[2])
            count = x.count(x[4])
    else:
        min = int(x[0:2])
        #Setting the max if there are 2 first digits.
        max = int(x[3:5])
        count = x.count(x[6])
        
    if min <= (count - 1) <= max:
        pwdcount = pwdcount + 1

    regex = r"(: )"

    matches = re.search(regex, x)

    if matches:
        temp = x[matches.end():]
        if (temp[min-1] == x[matches.end()-3]) ^ (temp[max-1] == x[matches.end()-3]):
            part2counter = part2counter + 1


print(f"Final pwd count: {pwdcount}")
print(f"Part 2 counter: {part2counter}")