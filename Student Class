class Student:
    def __init__(self, first_name, last_name, age, grade, student_id, username, courses):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade
        self.student_id = student_id
        self.username = username
        self.courses = courses

    def __str__(self):
        return f"Student Name: {self.first_name} {self.last_name}, Age: {self.age}, Grade: {self.grade}, ID: {self.student_id}, Username: {self.username}, Courses: {', '.join(self.courses)}"
    
    # Method to save student info to a file
    def save_to_file(self, filename='students.txt'):
        with open(filename, 'a') as file:
            file.write(str(self) + '\n')
