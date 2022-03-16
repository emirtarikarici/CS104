
def splitIndex(a):
    for i in range(len(a)-1):
        sum_before = sum([a[j] for j in range(i+1)])
        sum_after = sum([a[j] for j in range(i+1,len(a))])
        if sum_before == sum_after:
            return i+1
        
    return -1

a = [5,2,3]
result = splitIndex(a)
print(result)

a = [2,5,7]
result = splitIndex(a)
print(result)

a = [1,1,3,1]
result = splitIndex(a)
print(result)

