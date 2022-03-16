
def prefixSum(filename):
    numbers = []
    with open(filename, "r") as infile:
        for line in infile:
            number = int(line.rstrip())
            numbers.append(number)

    P = []
    for i in range(len(numbers)):
        prefix = 0
        for j in range(i+1):
            prefix += numbers[j]
        P.append(prefix)
        
    return P

filename = "ques2input.txt"
result = prefixSum(filename)
print(result)

