import os

def readfile(fname):
    out = {}
    with open(fname, "r") as infile:
        for line in infile:
            key, value = line.rstrip().split(",")
            out[key] = value
    return out

fname1 = "A.csv"
A = readfile(fname1)
fname2 = "B.csv"
B = readfile(fname2)

C = {}
for key, value in A.items():
    if value in B:
        C[key] = B[value]

if not os.path.exists("out"):
    os.makedirs("out")

os.chdir("out")
outfname = "C.csv"
with open(outfname, "w") as outfile:
    for key in C:
        outfile.write("{0},{1}\n".format(key,C[key]))
    
