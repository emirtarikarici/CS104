
def isRowIncreasing(array):
    for i in range(len(array)):
        for j in range(1,len(array[i])):
            if array[i][j] < array[i][j-1]:
                return False
    return True        
    
array = [[0, 1, 1, 2, 3],
		 [-5, 0, 2, 3, 3],
		 [-1, 0, 0, 1, 1],
		 [0, 0, 1, 1, 2],
		 [-1, 0, 1, 1, 1]]

print(isRowIncreasing(array))
    
