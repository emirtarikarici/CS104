students = dict()
with open("./students.dat", "r") as f:
    f.readline()
    f.readline()
    table = f.readlines()
    for record in table:
        fields = record.split()
        students[int(fields[0])] = fields[1:]


def print_name(student_number):
    print(students[student_number][0])


def print_surname(student_number):
    print(students[student_number][1])


def print_birth_place(student_number):
    print(students[student_number][2])


def print_department(student_number):
    print(students[student_number][3])


def print_gpa(student_number):
    print(students[student_number][4])

print(students)
print_name(13726146)  # "Luisa"
print_surname(30730594)  # "Connelly"
print_birth_place(81709043)  # "Detroit"
print_department(23937852)  # "CS"
print_gpa(43447560)  # "3.52"
