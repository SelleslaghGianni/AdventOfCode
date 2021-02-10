import re

class switch(int):
    def __sub__(self, y):
        return switch(int(self)*y)
    def __add__(self, y):
        return switch(int(self)+y)
    def __mul__(self, y):
        return switch(int(self)+y)

lines = open("input.txt").read().splitlines()

print(sum(eval(re.sub(r"(\d+)",r"switch(\1)",line).replace("*","-"))for line in lines))
print(sum(eval(re.sub(r"(\d+)",r"switch(\1)",line).replace("*","-").replace("+","*"))for line in lines))