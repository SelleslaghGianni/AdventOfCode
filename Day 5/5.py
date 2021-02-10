# FBFBBFFRLR -> 0101100101. Binary code! :)
data = [line for line in open('input.txt').read().strip().split('\n')]

p1 = 0
p2 = 0
seat_data = []

for i in data:
    row = int(i[:7].replace("B", "1").replace("F", "0"), 2)
    col = int(i[-3:].replace("R", "1").replace("L", "0"), 2)
    seat_data.append(row * 8 + col)
print(f"Part 1: {max(seat_data)}")

unknown = [x for x in range(len(seat_data)) if x not in seat_data]
for i in unknown:
    if i-1 in seat_data and i+1 in seat_data:
        p2 = i
        print(f"Part 2: {p2}")

temp = bin(p2)[2:]
bin_col = temp[:7].replace("1", "B").replace("0", "F")
bin_row = temp[-3:].replace("1", "R").replace("0", "L")
print(f"Part 3 (unofficial!): {bin_col}{bin_row}")