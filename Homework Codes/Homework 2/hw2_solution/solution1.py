import sys

maximum = float(sys.argv[1])
medium = float(sys.argv[2])
minimum = float(sys.argv[3])

if medium > maximum:
    temporary = maximum
    maximum = medium
    medium = temporary

if minimum > maximum:
    temporary = maximum
    maximum = minimum
    minimum = temporary

if minimum > medium:
    temporary = medium
    medium = minimum
    minimum = temporary

print(minimum)
print(medium)
print(maximum)
