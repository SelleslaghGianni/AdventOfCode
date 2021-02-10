import fileinput
import re

def solve(p1):
    shining = set()
    L = list([l.strip() for l in fileinput.input()])
    for r,l in enumerate(L):
        for c,ch in enumerate(l):
            if ch == '#':
                shining.add((r,c,0,0))

    for _ in range(6):
        new_shining = set()
        check = set()
        for (x,y,z,w) in shining:
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            if w+dw==0 or (not p1):
                                check.add((x+dx, y+dy, z+dz, w+dw))

        for (x,y,z,w) in check:
            neighbour_count = 0
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    for dz in [-1,0,1]:
                        for dw in [-1,0,1]:
                            if dx!=0 or dy!=0 or dz!=0 or dw!=0:
                                if (x+dx, y+dy, z+dz, w+dw) in shining:
                                    neighbour_count += 1
            if (x,y,z,w) not in shining and neighbour_count == 3:
                new_shining.add((x,y,z,w))
            if (x,y,z,w) in shining and neighbour_count in [2,3]:
                new_shining.add((x,y,z,w))
        shining = new_shining

    return len(shining)

print(solve(True))
print(solve(False))