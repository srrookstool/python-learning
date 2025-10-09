import numpy as np
import re

def add_student(gradebook,name,grade):
    if grade <= 100 and grade >=0:
        gradebook[name] = grade
        return True
    else: return False
def get_class_average(gradebook):
    if len(gradebook) == 0:
        return 0
    sum = 0
    for name in gradebook:
        sum += gradebook[name]
    return (sum/len(gradebook))
def get_passing_students(gradebook):
    passing = []
    for name in gradebook:
        if gradebook[name] >=60:
            passing.append(name)
    return passing

def find_common_students(course1_students,course2_students):
    return course1_students & course2_students

def find_all_students(course1_students,course2_students):
    return course1_students | course2_students

def find_unique_to_course1(course1_students, course2_students):
    return course1_students - course2_students

def check_enrollment(student_name, *course_lists):
    for course in course_lists:
        if student_name in course:
            return True
    return False

def calculate_daily_averages(temps):
    return np.mean(temps, axis=1)

def find_hottest_day(temps):
    return np.argmax(calculate_daily_averages(temps))

def count_cold_readings(temps,threshold):
    count = 0
    for row in temps:
        for num in row:
            if num < threshold:
                count += 1
    return count

def normalize_temperatures(temps):
    min_temp = np.min(temps)
    max_temp = np.max(temps)
    return (temps - min_temp) / (max_temp - min_temp) * 100

def clean_name(name):
    return name.strip().title()

def validate_email(email):
    if email.count("@") == 1:
        if email.split("@")[1].count(".") == 1:
            return True
    return False

def format_phone(phone):
    newphone = ""
    for x in phone:
        if x.isdigit():
            newphone += x
    if len(newphone) == 10:
        return f"({newphone[0:3]}) {newphone[3:6]}-{newphone[6:10]}"
    else: return "Invalid"

def process_registration(data_string):
    datalist = data_string.split(",")
    name = clean_name(datalist[0])
    if validate_email(datalist[1]):
        email = datalist[1]
    else: return "Invalid"
    phone = format_phone(datalist[2])
    return {"name":name,"email":email,"phone":phone}

def find_all_phones(text):
    pattern = r"(?:\d{3}-|\(\d{3}\) )\d{3}-\d{4}"
    return re.findall(pattern,text)

def find_all_prices(text):
    pattern = r"\$\d{1,3}\.\d{2}"
    return re.findall(pattern,text)

def extract_emails(text):
    pattern = r"\w+\@\w+\.\w+"
    return re.findall(pattern,text)

def validate_student_id(student_id):
    pattern = r"[a-zA-Z]{2}\d{4}$"
    if re.search(pattern,student_id):
        return True
    else: return False
    
if __name__ == "__main__":
    gradebook = {}
    print(add_student(gradebook, "Alice", 85)) # Should print True
    print(add_student(gradebook, "Bob", 150)) # Should print False
    print(add_student(gradebook, "Charlie", 45)) # Should print True
    print(f"Average: {get_class_average(gradebook):.2f}")
    # Bonus -- 10 pints
    print(f"Passing: {get_passing_students(gradebook)}")
    cs_students = {"Alice", "Bob", "Charlie", "David"}
    math_students = {"Bob", "Charlie", "Eve", "Frank"}
    physics_students = {"Alice", "Eve", "George"}
    print("Common:", find_common_students(cs_students, math_students))
    print("All:", find_all_students(cs_students, math_students))
    print("CS only:", find_unique_to_course1(cs_students, math_students))
    # Bonus
    print("Alice enrolled?", check_enrollment("Alice", cs_students,
    math_students))
    # Bonus
    print("Henry enrolled?", check_enrollment("Henry", cs_students, math_students,
    physics_students))
    temps = np.array([
    [65, 75, 70],
    [68, 78, 72],
    [70, 80, 75],
    [62, 73, 68],
    [67, 77, 71],
    [69, 79, 74],
    [64, 74, 69]
    ])
    print("Daily averages:", calculate_daily_averages(temps))
    print("Hottest day index:", find_hottest_day(temps))
    print("Cold readings (< 70):", count_cold_readings(temps, 70))
    print("Normalized (first day):", normalize_temperatures(temps)[0])
    # Test individual functions
    print(clean_name(" john smith ")) # Should print "John Smith"
    print(validate_email("test@email.com")) # Should print True
    print(validate_email("bad.email")) # Should print False
    print(format_phone("555-123-4567")) # Should print "(555) 123-4567"
    print(format_phone("123")) # Should print "Invalid"
    # Test complete processing
    test_data = " alice jones ,alice@example.com,9871234567"
    print(process_registration(test_data))   
    test_text = """
    For info, call 555-123-4567 or (555) 987-6543.
    Email us at info@school.edu or admin@college.com
    Course fees: $50.00 for materials, $150.50 for tuition
    """
    print("Phones:", find_all_phones(test_text))
    print("Prices:", find_all_prices(test_text))
    print("Emails:", extract_emails(test_text))
    print("Valid ID 'CS1234'?", validate_student_id("CS1234"))
    print("Valid ID '12ABCD'?", validate_student_id("12ABCD"))
    print("Valid ID 'AB12345'?", validate_student_id("AB12345"))