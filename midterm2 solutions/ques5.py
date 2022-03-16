import math

def getGrades(fname):
    try:
        gradesFile = open(fname, 'r') #open file for reading
    except IOError:
        raise ValueError('getGrades could not open ' + fname)
    grades = []
    for line in gradesFile:
        try:
            grades.append(float(line))
        except:
            raise ValueError('Unable to convert line to float')
    return grades
   
try:
   grades = getGrades('grades.txt')
   if len(grades) <= 1:
       raise ValueError("Zero division error in calculation")
   
   mean_grade = sum(grades) / float(len(grades))

   std = 0.0
   for grade in grades:
       std += (grade-mean_grade)**2
   std /= (len(grades) - 1)
   std = math.sqrt(std)
   print('Standard deviation is', std)
except ValueError as errorMsg:
   print('Whoops.', errorMsg)
   
    
