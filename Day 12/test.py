import re

F = open("input.txt", "r").read().splitlines()



for i in range(len(F)):
    SearchStr = r"\d+"
    res = F[i]
    Result = re.search(SearchStr.decode('utf-8'), res.decode('utf-8'), re.I | re.U)
    if Result:
        print(Result.groups())