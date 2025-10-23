class Teacher:
    def __init__(self, name):
        self.name = name
        self.students = {}
    def add_student(self, student_name, initial_grade = 0):
        self.students[student_name] = initial_grade
    def grade_student(self, student_name, grade):
        if student_name in self.students:
            self.students[student_name] = grade
    def class_average(self):
        sum = 0
        for grade in self.students.values():
            sum += grade
        return sum / (len(self.students.values()))
    