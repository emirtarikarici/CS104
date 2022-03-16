def up2():
    """Plot upper part
    """
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ", end="")
        print("/",end="")
        for j in range(1, 2*i-1):
            print("*", end="")
        print("\\")
        
def down2():
    """Plot down part
    """
    for i in range(5,0,-1):
        for j in range(1,6-i):
            print(" ", end="")
        print("\\", end="")
        for j in range(1, 2*i-1):
            print("*", end="")
        print("/")

down2()
up2()
