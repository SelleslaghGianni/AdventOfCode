from copy import deepcopy
import cmath
F = open("input.txt", "r").read().splitlines()

x = 0
y = 0
ship = complex(0, 0)
wp = complex(10, 1)

for f in F:
    direc, num = f[0], int(f[1:])

    if direc == "N":
        wp += complex(0, num)
    elif direc == "S":
        wp += complex(0, -num)
    elif direc == "E":
        wp += complex(num, 0)
    elif direc == "W":
        wp += complex(-num, 0)
    elif direc == "F":
        ship += wp * num
    elif direc == "R":
        wp *= complex(0, -1)**(num // 90)
    elif direc == "L":
        wp *= complex(0, 1)**(num // 90)

direction_east = True
direction_south = False
direction_north = False
direction_west = False
direction = 5490

for i in range(len(F)):
    if direction % 360 == 0:
        direction_north = True
        direction_east = False
        direction_south = False
        direction_west = False
    elif direction % 360 == 90:
        direction_east = True
        direction_north = False
        direction_south = False
        direction_west = False
    elif direction % 360 == 180:
        direction_south = True
        direction_north = False
        direction_east = False
        direction_west = False
    elif direction % 360 == 270:
        direction_west = True
        direction_north = False
        direction_east = False
        direction_south = False
    #print(F[i])
    if "N" in F[i]:
        temp = F[i].replace("N", "")
        wp_y = wp_y - int(temp)
    if "S" in F[i]:
        temp = F[i].replace("S", "")
        wp_y = wp_y + int(temp)
    if "E" in F[i]:
        temp = F[i].replace("E", "")
        wp_x = wp_x + int(temp)
    if "W" in F[i]:
        temp = F[i].replace("W", "")
        wp_x = wp_x - int(temp)
    if "L" in F[i]:
        temp = F[i].replace("L", "")
        if temp == "90":
            temp_wpx = deepcopy(wp_x)
            temp_wpy = deepcopy(wp_y)
            wp_x = deepcopy(temp_wpy)
            wp_y = deepcopy(temp_wpx)
            wp_x = wp_x * -1
            wp_y = wp_y * -1
        if temp == "180":
            if x == wp_x:
                wp_y = wp_y * -1
            if y == wp_y:
                wp_x = wp_x * -1
        if temp == "270":
            temp_wpx = deepcopy(wp_x)
            temp_wpy = deepcopy(wp_y)
            wp_x = deepcopy(temp_wpy)
            wp_y = deepcopy(temp_wpx)

    if "R" in F[i]:
        temp = F[i].replace("R", "")
        if temp == "90":
            temp_wpx = deepcopy(wp_x)
            temp_wpy = deepcopy(wp_y)
            wp_x = deepcopy(temp_wpy)
            wp_y = deepcopy(temp_wpx)
        if temp == "180":
            if x == wp_x:
                wp_y = wp_y * -1
            if y == wp_y:
                wp_x = wp_x * -1
        if temp == "270":
            temp_wpx = deepcopy(wp_x)
            temp_wpy = deepcopy(wp_y)
            wp_x = deepcopy(temp_wpy)
            wp_y = deepcopy(temp_wpx)
    if "F" in F[i]:
        temp = F[i].replace("F", "")
        x = x + (wp_x * int(temp))
        y = y + (wp_y * int(temp))
        #if direction_north:
        #    y = y - int(temp)
        #elif direction_south:
        #    y = y + int(temp)
        #elif direction_east:
        #    x = x + int(temp)
        #elif direction_west:
        #    x = x - int(temp)

    #print(x)
    #print(y)

print(x)
print(y)
print(x+y)

print(ship)

# N means to move the waypoint north by the given value.
# S means to move the waypoint south by the given value.
# E means to move the waypoint east by the given value.
# W means to move the waypoint west by the given value.
# L means to rotate the waypoint around the ship left (counter-clockwise) the given number of degrees.
# R means to rotate the waypoint around the ship right (clockwise) the given number of degrees.
# F means to move forward to the waypoint a number of times equal to the given value.