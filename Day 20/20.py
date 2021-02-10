data = open("input.txt").read().split("\n")

tiles = {}
for l in data:
    if l.startswith("Tile "):
        edges[l[5:9]] = "test"
    
print(edges)