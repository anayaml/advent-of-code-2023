t = 0


for i,x in enumerate(open("input.txt")):
    gs = x.strip().split(": ")[1].split("; ")
    for g in gs:
        j = {"red": 0, "green": 1, "blue": 2}
        for k in g.split(", "):
            a,b = k.split()
            j[b] = int(a)
        if j["red"] > 12 or j["green"] > 13 or j["blue"] > 14:
            break
        else:
            t += 1
print(t)