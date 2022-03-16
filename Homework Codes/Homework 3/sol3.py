# Your function must accept an argument called height which will be used to figure out the height of the triangle
height = int(input("Height of triangle: "))
# Your function must return the sum of all integers on the last line of the triangle. For example 16 for height=4, 4 for height =2, and 49 for height=7.
sumLast = height ** 2

# Your function must use another function called get_row to figure out the row to be printed. This function must get the row height and return the necessary line. 
# For example, it shall return “1” for row_height=1, “1 2 1” for row_height=2, “1 2 3 4 5 4 3 2 1” for row_height=5.
def get_row():
# Generate general pattern
    for i in range(1,height+1):
    # for spaces 
        for j in range(1,height+1-i):
            print(' ', end='')
    # for increasing pattern
        for j in range(1,i+1):
            print(j, end='')
    # for decreasing pattern 
        for j in range(i-1,0,-1):
            print(j, end='')
    # Moving to next line
        print()

get_row()
print("Sum of all numbers in the last row is " + str(sumLast))