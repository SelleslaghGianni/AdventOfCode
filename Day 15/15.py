inp =  [6, 4, 12, 1, 20, 0, 16]
num_spoke = {}

for i,n in enumerate(inp):
    if i != len(inp)-1:
        num_spoke[n] = i

while len(inp) < 30000000:
    prev = inp[-1]
    prev_prev = num_spoke.get(prev, -1)
    num_spoke[prev] = len(inp)-1
    if prev_prev == -1:
        next_ = 0
    else:
        next_ = len(inp) - 1 - prev_prev
    inp.append(next_)
    
    
print(inp[-1])