prod = ["asd", "sed", "wasdwa", "ddsdddd", "ddddd"]


for p in prod:
    if "s" in p:
        p = p.replace("s", "aaaaa")


print(prod)