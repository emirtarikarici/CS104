class Student:
    def __init__(self, name, surname, birth_place, department, gpa):
        self.name = name
        self.surname = surname
        self.birth_place = birth_place
        self.department = department
        self.gpa = gpa

    def print_name(self):
        print(self.name)

    def print_surname(self):
        print(self.surname)

    def print_birth_place(self):
        print(self.birth_place)

    def print_department(self):
        print(self.department)

    def print_gpa(self):
        print(self.gpa)


students = dict()
with open("./students.dat", "r") as f:
    f.readline()
    f.readline()
    for record in f.readlines():
        fields = record.split()
        students[int(fields[0])] = Student(*fields[1:])

students[13726146].print_name()  # "Luisa"
students[30730594].print_surname()  # "Connelly"
students[81709043].print_birth_place()  # "Detroit"
students[23937852].print_department()  # "CS"
students[43447560].print_gpa()  # "3.52"
