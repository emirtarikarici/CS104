def checkBoard(board):
    n = len(board)
    board[0][0] = 2
    changed = True
    while changed: #if there is still some squares that can be updated enter into loop
        changed = False
        for i in range(0,n):
            for j in range(0,n):
                if board[i][j] == 2:
                    if i+1 < n and board[i+1][j]==0: #if i+1>=n, it is out of boundary
                        board[i+1][j] = 2
                        changed = True
                    if j+1<n and board[i][j+1]==0:
                        board[i][j+1] = 2
                        changed = True
                    if i-1>-1 and board[i-1][j]==0:
                        board[i-1][j] = 2
                        changed = True
                    if j-1>-1 and board[i][j-1]==0:
                        board[i][j-1]=2
                        changed = True
                    
    return board[n-1][n-1] == 2


size = 5
board = [[None for j in range(5)] for i in range(size)]
for i in range(size):
    for j in range(size):
        board[i][j] = int(input())

fname = "abc.txt"
with open(fname, "w") as outfile:
    for i in range(size):
        for j in range(size):
            outfile.write(str(board[i][j]) + " ")
        outfile.write("\n")

if checkBoard(board): #board will be updated
    outfname = "out.txt"
    with open(outfname, "w") as outfile:
        for i in range(size):
            for j in range(size):
                outfile.write(str(board[i][j]) + " ")
            outfile.write("\n")
    print("Path found")
else:
    print("Path not found")
