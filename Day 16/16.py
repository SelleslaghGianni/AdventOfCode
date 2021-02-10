ranges = open("ranges.txt", "r").read().splitlines()
nearby_tix = open("input.txt", "r").read().splitlines()
my_tick = open("myticket.txt", "r").read().splitlines()

val_list = []
line_count = 0
valid = 0

for i in range(len(nearby_tix)):
    if i == 0:
        continue
    values = nearby_tix[i].split(",")
    val_list.append(values)

print(val_list)
exit(0)

for line in ranges:
    tick_not_valid = True
    temp, temp_rang = line.split(": ")
    first, second = temp_rang.split(" or ")
    first_min, first_max = first.split("-")
    second_min, second_max = second.split("-")
    for i in range(len(nearby_tix)):
        if not int(first_min) <= int(val_list[line][line_count]) <= int(first_max):
            if not int(second_min) <= int(val_list[line][line_count]) <= int(second_max):
                tick_not_valid = False
                continue
    if tick_not_valid:
        valid += 1
    line_count += 1

print(valid)
