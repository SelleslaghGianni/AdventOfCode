data = open("input.txt", "r").read().splitlines()
    
def prog(program, part1): # Second variable is to check if it's the first or second part.
    seen = set()
    x = 0
    acc = 0
    while True:
        #This was for debugging.
        #print(data[x])
        #print(x)
        #print(acc)
        #print("-------")
        if x == len(data) and not part1:
            return acc
        if x in seen and not part1:
            return None
        if x in seen and part1:
            return acc
        seen.add(x)
        line = program[x]
        inst, arg = line.split()
        arg = int(arg)

        if inst == "jmp":
            x += arg
            continue
        if inst == "acc":
            acc += arg
        if inst == "nop":
            pass
        
        x += 1

        

print(f"Part 1: {prog(data, True)}.")

for i in range(len(data)):
    inp_data = data[:]
    if inp_data[i].startswith("jmp"):
        inp_data[i] = inp_data[i].replace("jmp", "nop")
    elif inp_data[i].startswith("nop"):
        inp_data[i] = inp_data[i].replace("nop", "jmp")
    else:
        continue
    a = prog(inp_data, False)
    if a:
        print(f"Part 2: {a}.")