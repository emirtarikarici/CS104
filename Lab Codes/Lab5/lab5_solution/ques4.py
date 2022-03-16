def transpose(table):
    """Returns: copy of table with rows and columns swapped
    
    Example:
           1  2          1  3  5
           3  4    =>    2  4  6
           5  6
           
    Precondition: table is a (non-ragged) 2d List"""
    
    # Find the size of the (non-ragged) table
    numrows = len(table)
    numcols = len(table[0]) # All rows have same no. cols
    
    # Build the table
    result = [] # Result accumulator 
    for m in range(numcols):

        # Make a single row
        row = [] # Single row accumulator
        for n in range(numrows):
            row.append(table[n][m])

        #Add the result to the table
        result.append(row)
        
    return result

table = [[1,2],[3,4],[5,6]]
transposed = transpose(table)
print(transposed)