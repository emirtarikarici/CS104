import math

with open("./shapes.csv", "r") as f:
    lines_of_interest = [line.strip() for line in f if line.strip() and line.strip()[0] != "#"]

file_for_rectangles = open("rectangles.csv", "w")
file_for_trapezoids = open("trapezoids.csv", "w")
file_for_circles = open("circles.csv", "w")

for line in lines_of_interest:
    fields = line.split(",")
    if len(fields) == 1:  # Circle
        file_for_circles.write("%s,%f\n" % (fields[0].strip(), math.pi * math.pow(float(fields[0].strip()), 2)))

    elif len(fields) == 2:  # Rectangle
        file_for_rectangles.write(
            "%s,%s,%f\n" % (
                fields[0].strip(), fields[1].strip(), float(fields[0].strip()) * float(fields[1].strip())))

    elif len(fields) == 3:  # Trapezoid
        file_for_trapezoids.write("%s,%s,%s,%f\n" % (
            fields[0].strip(), fields[1].strip(), fields[2].strip(),
            0.5 * (float(fields[0].strip()) + float(fields[1].strip())) * float(fields[2].strip())))

file_for_rectangles.close()
file_for_trapezoids.close()
file_for_circles.close()
