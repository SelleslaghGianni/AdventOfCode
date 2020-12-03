# 323 lijnen naar beneden
# 31 tekens per lijn.
# 0-3-6-9-12-15-18-21-24-27-30-2-5-8-11-14-17-20-23-26-29-1-4-7-10-13-16-19-22-25-28-0
# 0-7-14-21-28-4-11-18-25-1-8-15-22-29-5-12-19-26-2-9-16-23-30-6-13-20-27-3-10-17-24-0
# 0-5-10-15-20-25-30-4-9-14-19-24-29-3-8-13-18-23-28-2-7-12-17-22-27-1-6-11-16-21-26-0


fi = open("input.txt", "r")

input_array = []
TREE = '#'
# OPEN_SQUARE = '.'
right3_down1_counter = 0
right1_down1_counter = 0
right7_down1_counter = 0
right5_down1_counter = 0
right1_down2_counter = 0
x = 0
y = 0
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0

set_to_0 = False
set_to_1 = False
set_to_2 = False
set_to_3 = False
set_to_4 = False
set_to_5 = False
set_to_6 = False

for row in fi:
    input_array.append(row)

#First part: Right 3, down 1
while x < 323:
    if y == 30:
        set_to_2 = True
    if y == 29:
        set_to_1 = True
    if y == 28:
        set_to_0 = True
    if input_array[x][y] == TREE:
        right3_down1_counter = right3_down1_counter + 1
        
    
    x = x + 1
    y = y + 3

    if set_to_0:
        y = 0
        set_to_0 = False
    if set_to_1:
        y = 1
        set_to_1 = False
    if set_to_2:
        y = 2
        set_to_2 = False

# Right 1, Down 1
while a < 323:
    if b == 30:
        set_to_0 = True
    if input_array[a][b] == TREE:
        right1_down1_counter = right1_down1_counter + 1
        
    a = a + 1
    b = b + 1

    if set_to_0:
        b = 0
        set_to_0 = False

# Right 7, down 1
while c < 323:
    if d == 28:
        set_to_4 = True
    if d == 25:
        set_to_1 = True
    if d == 29:
        set_to_5 = True
    if d == 26:
        set_to_2 = True
    if d == 30:
        set_to_6 = True
    if d == 27:
        set_to_3 = True
    if d == 24:
        set_to_0 = True
    if input_array[c][d] == TREE:
        right7_down1_counter = right7_down1_counter + 1
    
    c = c + 1
    d = d + 7

    if set_to_0:
        d = 0
        set_to_0 = False
    if set_to_1:
        d = 1
        set_to_1 = False
    if set_to_2:
        d = 2
        set_to_2 = False
    if set_to_3:
        d = 3
        set_to_3 = False
    if set_to_4:
        d = 4
        set_to_4 = False
    if set_to_5:
        d = 5
        set_to_5 = False
    if set_to_6:
        d = 6
        set_to_6 = False
    
# Right 5, down 1
while e < 323:
    if f == 30:
        set_to_4 = True
    if f == 29:
        set_to_3 = True
    if f == 28:
        set_to_2 = True
    if f == 27:
        set_to_1 = True
    if f == 26:
        set_to_0 = True
    if input_array[e][f] == TREE:
        right5_down1_counter = right5_down1_counter + 1
        print(e)
        print(f)
         
    e = e + 1
    f = f + 5

    if set_to_0:
        f = 0
        set_to_0 = False
    if set_to_1:
        f = 1
        set_to_1 = False
    if set_to_2:
        f = 2
        set_to_2 = False
    if set_to_3:
        f = 3
        set_to_3 = False
    if set_to_4:
        f = 4
        set_to_4 = False

# Right 1, down 2
while g < 323:
    if g == 322:
        set_to_1 = True
    if h == 30:
        set_to_0 = True
    if input_array[g][h] == TREE:
        right1_down2_counter = right1_down2_counter + 1
         
    g = g + 2
    h = h + 1

    if set_to_0:
        h = 0
        set_to_0 = False
    if set_to_1:
        break
    
    

print(f"First part: {right3_down1_counter}")
print(f"Second part: {right1_down1_counter}")
print(f"Second part: {right7_down1_counter}")
print(f"Second part: {right5_down1_counter}")
print(f"Second part: {right1_down2_counter}")
second_answer = right1_down1_counter * right1_down2_counter * right3_down1_counter * right5_down1_counter * right7_down1_counter
print(f"Second answer: {second_answer}")


