array = []

f = open("input.txt", "r")

for row in f:
    array.append(row)

first_part_bool = True
second_part_bool = True
first_part_answer = 0
second_part_answer = 0

for row in array:
    for i in array:
        if (int(row) + int(i)) == 2020 and first_part_bool:
            first_part_answer = int(row)*int(i)
            first_part_bool = False
        for j in array:
            if (int(row) + int(i) + int(j)) == 2020 and second_part_bool:
                second_part_answer = int(row)*int(i)*int(j)
                second_part_bool = False


print(f"First part: {first_part_answer}")
print(f"Second part: {second_part_answer}")