import numpy as np
import re

array = []
pwd_count = 0
first_final_count = 0
second_final_count = 0

fi = open("input.txt", "r")

for row in fi:
    array.append(row)

arr = np.array(array)
for x in arr:
    #Slicing the row (x) to make it clean.
    max = 0
    #Checking if there are 1 or 2 digits. If true 1 digit, false 2 digits.
    if "-" in x[0:2]:
        min = int(x[0])
        max = int(x[2:4])
        #Checking if there are 1 or 2 digits in the max.
        if " " in x[2:4]:
            max = int(x[2])
    else:
        #Setting the max if there are 2 first digits.
        min = int(x[0:2])
        max = int(x[3:5])

    #Estabilishing regex stuff, then checking for the conditions as set in the exercise.
    regex = r"(: )"
    matches = re.search(regex, x)
    temp = x[matches.end():]
    #First part
    pwd_count = temp.count(x[matches.end()-3])
    if min <= pwd_count <= max:
        first_final_count = first_final_count + 1
    #Second part
    if (temp[min-1] == x[matches.end()-3]) ^ (temp[max-1] == x[matches.end()-3]):
        second_final_count = second_final_count + 1
    
    
print(f"Part 1 counter: {first_final_count}.")
print(f"Part 2 counter: {second_final_count}.")