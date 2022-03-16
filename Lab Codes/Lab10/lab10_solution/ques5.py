def rreverse(s):
    if s == "":
        return s
    else:
        return rreverse(s[1:]) + s[0]

print(rreverse("string"))
