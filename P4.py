
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
avg_grades = [sum(student) / len(student) for student in grades]
#Пытался сделать без for, выглядело ужасно. Так намного проще.

grade_per_student = dict(zip(sorted(students), avg_grades))

print(grade_per_student)



