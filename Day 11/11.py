from copy import deepcopy
import fileinput

data = [list(f.strip()) for f in list(fileinput.input())]
R = len(data)
C = len(data[0])


while True:
    change = False
    new_data = deepcopy(data)
    for r in range(R): 
            for c in range(C):
                nocc = 0
                for dr in [-1,0,1]:
                    for dc in [-1,0,1]:
                        if not (dr==0 and dc==0):
                            rr = r+dr
                            cc = c+dc
                            while 0<=rr<R and 0<=cc<C and data[rr][cc]=='.':
                                rr = rr+dr
                                cc = cc+dc
                            if 0<=rr<R and 0<=cc<C and data[rr][cc]=='#':
                                nocc += 1
        
            if data[r][c] == 'L':
                if nocc == 0:
                    new_data[r][c] = '#'
                    change = True
            elif data[r][c] == '#' and nocc >=4:
                new_data[r][c] = 'L'
                change = True

    if not change:
        break
    data = deepcopy(new_data)
    #print(change)

count = 0
for i in range(R):
    for j in range(C):
        if data[i][j] == "#":
            count += 1

print(count)
        