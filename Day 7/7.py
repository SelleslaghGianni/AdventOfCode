data = open("input.txt", "r").read().splitlines()

bags = {}
for row in data:
    x = row[:-1].split(" contain ")
    new_color = x[0][:-5]
    for i in x[1].split(", "):
        if i != "no other bags":
            color = " ".join(i.split(" ")[1:-1])
            num = int(i.split(" ")[0])
            if new_color not in bags:
                bags[new_color] = set({})
            bags[new_color].add((color, num))
        else:
            bags[new_color] = set({})

my_bag = {"shiny gold"}

adding_bag = True

#while adding_bag:
#    adding_bag = False
#    l = len(my_bag)
#    for color in my_bag:
#        if color in bags:
#            my_bag = my_bag | bags[color]
#    if len(my_bag) > l:
#        adding_bag = True


def add_colors(color):
    total = 0
    for old_color, num in bags[color]:
        total += num * (1 + add_colors(old_color))
    return total

print(add_colors('shiny gold'))