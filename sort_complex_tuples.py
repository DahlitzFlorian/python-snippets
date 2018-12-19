student_tuples = [("John", "A", 15), ("Jane", "B", 12), ("Dave", "B", 10)]

sorted_list = sorted(student_tuples, key=lambda student: student[2])

print(sorted_list)
