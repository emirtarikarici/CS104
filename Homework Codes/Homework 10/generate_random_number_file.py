import random

n = 1000000  # Modify this for n = 10, 100, 1000, 10000, 100000, 1000000
f = open("numbers.dat", "w")
for i in range(n):
    a = random.randint(1, 10000000)
    f.write(str(a) + "\n")

f.close()
