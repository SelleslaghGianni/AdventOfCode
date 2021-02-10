import re

fi = open("input.txt", "r")

input_array = []

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False
byr_counter = 0
iyr_counter = 0
eyr_counter = 0
hgt_counter = 0
hcl_counter = 0
ecl_counter = 0
pid_counter = 0
iteration_counter = 0


for row in fi:
    input_array.append(row)

for i in range(len(input_array)):
    if input_array[i] == "\n":
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
        continue

    if "byr" in input_array[i]:
        regex = r"(byr:[0-9]{4})"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if 1920 <= int(match.group().replace("byr:", "")) <= 2002:
                byr = True
                byr_counter += 1
    if "iyr" in input_array[i]:
        regex = r"(iyr:[0-9]{4})"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if 2010 <= int(match.group().replace("iyr:", "")) <= 2020:
                iyr = True
                iyr_counter += 1
    if "eyr" in input_array[i]:
        regex = r"(eyr:[0-9]{4})"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if 2020 <= int(match.group().replace("eyr:", "")) <= 2030:
                eyr = True
                eyr_counter += 1
    if "hgt" in input_array[i]:
        regex = r"(hgt:(\d\din|\d\d\dcm))"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if "in" in match.group():
                temp = match.group().replace("in", "")
                if 59 <= int(temp.replace("hgt:", "")) <= 76:
                    hgt = True
                    hgt_counter += 1
            if "cm" in match.group():
                temp = match.group().replace("cm", "")
                if 150 <= int(temp.replace("hgt:", "")) <= 193:
                    hgt = True
                    hgt_counter += 1
    if "hcl" in input_array[i]:
        regex = r"(hcl:#[0-9a-f]{6})"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if matches:
                hcl = True
                hcl_counter += 1
    if "ecl" in input_array[i]:
        if "amb" in input_array[i]:
            ecl = True
            ecl_counter += 1
        if "blu" in input_array[i]:
            ecl = True
        if "brn" in input_array[i]:
            ecl = True 
        if "gry" in input_array[i]:
            ecl = True
        if "grn" in input_array[i]:
            ecl = True
        if "hzl" in input_array[i]:
            ecl = True
        if "oth" in input_array[i]:
            ecl = True
    if "pid" in input_array[i]:
        regex = r"(pid:\d{9})"
        matches = re.finditer(regex, input_array[i])
        for matchNum, match in enumerate(matches, start=1):
            if matches:
                print(match.group().replace("pid:", ""))
                pid = True
                pid_counter += 1
    if "cid" in input_array[i]:
        cid = True
    
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        iteration_counter = iteration_counter + 1
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False
        cid = False
    

print(iteration_counter)
