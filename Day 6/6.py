fi = open("input.txt", "r")

data = []

for rows in fi:
    data.append(rows)

p1 = 0
ncount = 0

for i in range(len(data)):
    if data[i] == "\n":
        ncount += 1
        a = True
        b = True
        c = True
        d = True
        e = True
        f = True
        g = True
        h = True
        ib = True
        j = True
        k = True
        l = True
        m = True
        n = True
        o = True
        p = True
        q = True
        r = True
        s = True
        t = True
        u = True
        v = True
        w = True
        x = True
        y = True
        z = True
        continue
    
    if "a" in data[i] and a:
        p1 += 1
        a = False
    if "b" in data[i] and b:
        p1 += 1
        b = False
    if "c" in data[i] and c:
        p1 += 1
        c = False
    if "d" in data[i] and d:
        p1 += 1
        d = False
    if "e" in data[i] and e:
        p1 += 1
        e = False
    if "f" in data[i] and f:
        p1 += 1
        f = False
    if "g" in data[i] and g:
        p1 += 1
        g = False
    if "h" in data[i] and h:
        p1 += 1
        h = False
    if "i" in data[i] and ib:
        p1 += 1
        ib = False
    if "j" in data[i] and j:
        p1 += 1
        j = False
    if "k" in data[i] and k:
        p1 += 1
        k = False
    if "l" in data[i] and l:
        p1 += 1
        l = False
    if "m" in data[i] and m:
        p1 += 1
        m = False
    if "n" in data[i] and n:
        p1 += 1
        n = False
    if "o" in data[i] and o:
        p1 += 1
        o = False
    if "p" in data[i] and p:
        p1 += 1
        p = False
    if "q" in data[i] and q:
        p1 += 1
        q = False
    if "r" in data[i] and r:
        p1 += 1
        r = False
    if "s" in data[i] and s:
        p1 += 1
        s = False
    if "t" in data[i] and t:
        p1 += 1
        t = False
    if "u" in data[i] and u:
        p1 += 1
        u = False
    if "v" in data[i] and v:
        p1 += 1
        v = False
    if "w" in data[i] and w:
        p1 += 1
        w = False
    if "x" in data[i] and x:
        p1 += 1
        x = False
    if "y" in data[i] and y:
        p1 += 1
        y = False
    if "z" in data[i] and z:
        p1 += 1
        z = False

    
print(p1)