class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2*(self.width + self.height)

def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)

print(sum_of_digits(4567))

def safe_divide(a,b):
    if b == 0:
        return "Error: Cannot divide by 0"
    try:
        a = float(a)
        b = float(b)
    except: return "Error: Invalid input"
    else: return a/b

print(safe_divide(10,5))
print(safe_divide(10,0))
print(safe_divide(10,"applesauce"))

def add_letter_grade(student):
    avg = student['average']
    if avg >=90:
        student['letter'] = 'A'
    elif avg >=80:
        student['letter'] = 'B'
    elif avg >=70:
        student['letter'] = 'C'
    else:
        student['letter'] = 'D'
    return student

class1 = [{'name':'Alice','grades':[90,85,95]},{'name':'Bob','grades':[50,45,55]},{'name':'Charlie','grades':[70,75,72]}]

def process_grades(students):
    students = map(lambda x: x.update({'average':(sum(x['grades']) / len(x['grades']))}), students)
    students = filter(lambda x: x['average'] > 60, students)
    map(add_letter_grade,students)
    sorted(students,key=lambda x: x['average'],reverse=True)
    return students

print(process_grades(class1))
    