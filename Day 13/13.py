import fileinput
from sympy.ntheory.modular import crt

lines = list(fileinput.input())
time = int(lines[0])

bus = [int(x) for x in lines[1].split(",") if x!="x"]

best = None

for b in bus:
    t = time
    while t%b != 0:
        t += 1
    score = t-time
    if best is None or score < best[0]:
        best = (score, b)

with open("input.txt") as f:
    _, buses = f.read().splitlines()

moduli = []
residues = []
for i, bus in enumerate(buses.split(",")):
    if bus != "x":
        bus = int(bus)
        moduli.append(bus)
        residues.append(bus - i)

print(best[0]*best[1])
print(crt(moduli, residues)[0])
