#!/usr/bin/env python3

fi = open("input.txt", "r")
data = [int(line.strip()) for line in fi.readlines() if line.strip()]

data.append(0)
data = sorted(data)
data.append(max(data)+3)
count_1 = 0
count_3 = 0


for i in range(len(data)):
    if i == 0:
        continue
    if data[i]-data[i-1] == 1:
        count_1 += 1
    if data[i]-data[i-1] == 3:
        count_3 += 1
    print(data[i]-data[i-1])

DP = {}
def dp(inp):
    if inp == len(data)-1:
        return 1
    if inp in DP:
        return DP[inp]
    answer = 0
    for i in range(inp+1, len(data)):
        if data[i]-data[inp]<=3:
            answer += dp(i)
    DP[inp] = answer
    return answer

print(count_1*count_3)
print(dp(0))