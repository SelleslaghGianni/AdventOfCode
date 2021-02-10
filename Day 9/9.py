data = open("input.txt", "r").read().splitlines()


def number_checker(data):
    
    number_not_found = True
    for i in range(len(data)):
        number_not_found = True
        for j in range(1, 26):
            if i <= 25:
                break
            if number_not_found:
                for k in range(1, 26):
                    if int(data[i]) == int(data[i-j]) + int(data[i-k]):
                        if int(data[i-j]) == int(data[i-k]):
                            continue
                        number_not_found = False
                        continue
                    elif number_not_found and j == 25 and k == 25:
                        return data[i]

p1 = number_checker(data)
p2 = 0
print(f"Part 1: {p1}")
for i in range(len(data)):
    for j in range(i+2, len(data)):
        inp_range = data[i:j]
            
        if sum(map(int,inp_range)) == int(p1):
            print(min(inp_range))
            print(max(inp_range))
            exit(0)

def number_check(data, p1):
    for i in range(len(data)):
        for j in range(len(data)):
            if int(data[i]) + int(data[j]) == p1:
                print(data[i], data[j])
                exit(0)
            for k in range(len(data)):
                if int(data[i]) + int(data[j]) + int(data[k]) == p1:
                    print(data[i], data[j], data[k])
                    exit(0)
                for l in range(len(data)):
                    if int(data[i]) + int(data[j]) + int(data[k]) + int(data[l]) == p1:
                        print(data[i], data[j], data[k], data[l])
                        exit(0)
                    for m in range(len(data)):
                        if int(data[i]) + int(data[j]) + int(data[k]) + int(data[l]) + int(data[m]) == p1:
                            print(data[i], data[j], data[k], data[l], data[m])
                            exit(0)
                        for n in range(len(data)):
                            if int(data[i]) + int(data[j]) + int(data[k]) + int(data[l]) + int(data[m]) + int(data[n]) == p1:
                                print(data[i], data[j], data[k], data[l], data[m], data[n])
                                exit(0)
                            for o in range(len(data)):
                                for p in range(len(data)):
                                    for q in range(len(data)):
                                        for r in range(len(data)):
                                            for s in range(len(data)):
                                                for t in range(len(data)):
                                                    if int(data[i]) + int(data[j]) + int(data[k]) + int(data[l]) + int(data[m]) + int(data[n]) + int(data[o]) + int(data[p]) + int(data[q]) + int(data[r]) + int(data[s]) + int(data[t]) == p1:
                                                        print(data[i], data[j], data[k], data[l], data[m], data[n], data[o], data[p], data[q], data[r], data[s], data[t])
                                                        exit(0)
