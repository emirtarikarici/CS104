def up():
    """Plot upper part
    """
    for i in range(1,6):
        for j in range(1,6-i):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()

def down():
    """Plot down part
    """
    for i in range(5,0,-1):
        for j in range(1,6-i):
            print(" ", end="")
        for j in range(1, 2*i):
            print("*", end="")
        print()

up()
down()
    
